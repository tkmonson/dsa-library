'''
Practice scheduler for the NeetCode 150 (easies excluded) plus new problems.

DAILY FLOW
    Every morning at 8 (America/New_York), a GitHub Actions workflow emails
    the day's QUEUE of two problems. Do each one as a timed, from-scratch
    re-solve in a blank file, then record how it went, either way:

        * tap again/hard/good/easy in the email. It opens a prefilled GitHub
          issue; submit it and a workflow records the result.
        * or run `python problems/review/review.py done NUM RATING` locally. It
          pulls, records, commits, and pushes.

    The queue only changes when you record a result. A problem stays in the
    queue, email after email, until you do it. When you finish one of the
    two, the next email keeps the other and adds the next problem in line.

RATINGS
    again   Couldn't solve it, or needed a hint or a peek at a solution.
    hard    Solved, but over the target time (M 20m, H 35m) or buggy.
    good    Solved correctly within the target time.
    easy    Solved quickly and cleanly.

    good/easy are a SUCCESS. again/hard are a MISS: the problem becomes
    eligible again after RETRY_DAYS, ahead of everything else.

PICKING THE NEXT PROBLEM
    Whenever a queue slot opens, there's a `new_chance` chance it goes to a
    NEW problem: a random LeetCode medium or hard that you have not solved
    here or on LeetCode (from leetcode_problems.json; premium problems only if
    `include_premium`). Once recorded, it joins the pool below. Otherwise
    the slot goes to an old problem, chosen by one of two systems. Both read
    the same history of attempts, so switching (`"system"` in
    config.json, or `--system`) only changes what is picked next.

ROTATION (system = "rotation")
    All problems wait in one line, ordered by their last successful solve,
    oldest first (never solved comes first). Each opening takes from the
    front. A success sends the problem to the back of the line; with ~120
    problems at ~2 a day (less retries and new problems), it comes back in
    about three months. A miss brings it back after RETRY_DAYS.

    Best when time is short relative to the number of problems: everything
    gets a turn, and nothing you just did well comes back early.

SPACED REPETITION (system = "srs")
    Each problem has its own review interval that grows after every success
    and shrinks after a miss (SM-2, as in Anki):

        first success    4 days (easy: 10)
        good             max(interval, days since last attempt) x ease
        easy             same, x 1.3 more, and ease +0.15
        hard / again     back to RETRY_DAYS, ease -0.15 / -0.2

    Ease starts at 2.5 and stays within 1.3-3.0; intervals cap at
    MAX_INTERVAL. A problem is due once the days since its last attempt
    reach its interval, and the most overdue relative to their interval go
    first. If nothing is due, the closest to due is pulled forward. Known
    problems drift out to months; weak ones stay frequent.

    Best for long-term maintenance with no deadline: after about a year of
    ramp-up, ~120 problems settle around 1-1.5 reviews a day.

CATEGORY BALANCE (both systems)
    The system shortlists its most urgent problems: every retry, plus the
    next SHORTLIST by urgency. Retries go first. Otherwise the pick goes to
    whichever shortlisted category is furthest behind its fair share of
    attempts over the last BALANCE_DAYS (fair share = its number of
    problems / total), and the two queued problems never share a category.

SEEDING
    Until a problem has a recorded success, its last successful solve is the
    date its solution file was added to git, so problems untouched since
    2023 come up before ones from 2026.

Usage (run from anywhere):

    python review.py today                  Show the queue; make scratch files
    python review.py done NUM RATING [--min M] [--category C]
    python review.py stats                  Queue, retries, category balance
    python review.py email [--dry-run] [--force]   (run by GitHub Actions)

Global options: --system rotation|srs, --date YYYY-MM-DD (pretend today is
another day), --offline (skip git pull/push).
'''

import argparse
import html
import json
import os
import random
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from neetcode150 import NEETCODE_150, PROBLEMS as ALL_PROBLEMS

HERE = Path(__file__).resolve().parent
SOLUTIONS = HERE.parent
REPO = SOLUTIONS.parent
STATE_PATH = HERE / 'state.json'
CONFIG_PATH = HERE / 'config.json'
LEETCODE_PATH = HERE / 'leetcode_problems.json'
SCRATCH = HERE / 'scratch'
IN_CI = bool(os.environ.get('GITHUB_ACTIONS'))

RATINGS = ('again', 'hard', 'good', 'easy')
SUCCESS = ('good', 'easy')
TARGET_MINUTES = {'E': 10, 'M': 20, 'H': 35}
DIFFICULTY = {'E': 'Easy', 'M': 'Medium', 'H': 'Hard'}

RETRY_DAYS = 3
SHORTLIST = 15
BALANCE_DAYS = 30

FIRST_INTERVAL = {'good': 4, 'easy': 10}
START_EASE, MIN_EASE, MAX_EASE = 2.5, 1.3, 3.0
EASE_DELTA = {'again': -0.2, 'hard': -0.15, 'good': 0.0, 'easy': 0.15}
MAX_INTERVAL = 180

DEFAULT_CONFIG = {
    'system': 'rotation',
    'per_day': 2,
    'new_chance': 0.15,
    'include_premium': False,
    'timezone': 'America/New_York',
    'send_hour': 8,
    'github_repo': 'tkmonson/dsa-library',
    'branch': 'master',
}

# NeetCode problems in review; easies aren't worth the time
CORE = {n: p for n, p in ALL_PROBLEMS.items() if p[1] != 'E'}
OTHER = 'Other'


# --- Persistence ------------------------------------------------------------

def load_json(path: Path, default: dict) -> dict:
    if path.exists():
        return json.loads(path.read_text())
    return default

def load_config() -> dict:
    return DEFAULT_CONFIG | load_json(CONFIG_PATH, {})

def load_state() -> dict:
    state = load_json(STATE_PATH, {})
    for key, empty in (('history', {}), ('added', {}), ('queue', [])):
        state.setdefault(key, empty)
    return state

def save_state(state: dict) -> None:
    STATE_PATH.write_text(json.dumps(state, indent=2, sort_keys=True) + '\n')

def git(*args) -> subprocess.CompletedProcess:
    return subprocess.run(['git', *args], cwd=REPO, capture_output=True,
                          text=True)

def git_pull() -> None:
    result = git('pull', '--rebase', '--autostash', '-q')
    if result.returncode:
        print(f'(git pull failed; using local state)\n{result.stderr.strip()}')

def git_push(message: str) -> None:
    path = str(STATE_PATH.relative_to(REPO))
    git('add', path)
    if git('commit', '-q', '-m', message, '--', path).returncode:
        return
    result = git('push', '-q')
    if result.returncode:
        print('(git push failed; the result is committed locally, so push '
              f'before the next email)\n{result.stderr.strip()}')


# --- Problem metadata -------------------------------------------------------

def normalize(title: str) -> str:
    return re.sub(r'[^a-z0-9]', '', title.lower())

def slugify(title: str) -> str:
    slug = re.sub(r'[^a-z0-9 -]', '', title.lower())
    return re.sub(r'[ -]+', '-', slug).strip('-')

def header(path: Path) -> tuple[str, int] | None:
    for line in path.read_text().splitlines()[:5]:
        m = re.match(r'\s*(.*?)\s*\(#(\d+)\)', line)
        if m:
            return m[1], int(m[2])
    return None

def scan_solutions() -> tuple[dict, dict]:
    '''Map problem numbers and normalized titles to solution files.'''
    by_num, by_title = {}, {}
    for path in sorted(SOLUTIONS.glob('*.py')):
        if path.name.startswith('_'):
            continue
        h = header(path)
        if h:
            by_title.setdefault(normalize(h[0]), path)
            by_num.setdefault(h[1], path)
    return by_num, by_title

def git_add_dates() -> dict:
    '''Date each solution file was added to git, by file name.'''
    result = git('log', '--diff-filter=A', '--no-renames', '--date=short',
                 '--format=%x00%ad', '--name-only', '--', 'problems')
    dates, current = {}, None
    for line in result.stdout.splitlines():
        if line.startswith('\0'):
            current = date.fromisoformat(line[1:])
        elif line and current:
            # Newest first, so keep the first (most recent) add
            dates.setdefault(Path(line).name, current)
    return dates

def load_leetcode() -> dict[int, dict]:
    '''LeetCode's problem list, as saved from /api/problems/all/.'''
    if not LEETCODE_PATH.exists():
        return {}
    try:
        items = json.loads(LEETCODE_PATH.read_text())['stat_status_pairs']
    except (ValueError, KeyError):
        print(f'({rel(LEETCODE_PATH)} is not the LeetCode problem list; '
              'no new problems will be picked)', file=sys.stderr)
        return {}
    problems = {}
    for item in items:
        stat = item['stat']
        problems[int(stat['frontend_question_id'])] = {
            'title': stat['question__title'],
            'slug': stat['question__title_slug'],
            'diff': 'EMH'[item['difficulty']['level'] - 1],
            'premium': item['paid_only'],
            'solved': item['status'] == 'ac',
        }
    return problems


class Problem:
    def __init__(self, num, title, diff, category, solution=None, seed=None,
                 history=(), slug=None):
        self.num = num
        self.title = title
        self.diff = diff
        self.category = category
        self.solution = solution
        self.seed = seed
        self.history = list(history)
        self.slug = slug or (None if title.startswith('Problem #')
                             else slugify(title))

    @property
    def minutes(self) -> int:
        return TARGET_MINUTES[self.diff]

    @property
    def link(self) -> str:
        if not self.slug:
            return f'https://leetcode.com/problemset/?search={self.num}'
        return f'https://leetcode.com/problems/{self.slug}/'

    def last_attempt(self) -> date | None:
        return date.fromisoformat(self.history[-1]['date']) if self.history \
            else None

    def last_success(self) -> date | None:
        wins = [date.fromisoformat(h['date']) for h in self.history
                if h['rating'] in SUCCESS]
        return max(wins) if wins else self.seed

    def missed(self) -> bool:
        return bool(self.history) and self.history[-1]['rating'] not in SUCCESS

    def retry_date(self) -> date | None:
        return self.last_attempt() + timedelta(RETRY_DAYS) if self.missed() \
            else None

    def srs_interval(self) -> int:
        '''Replay the history through SM-2 to get the current interval.'''
        interval, ease, learned, prev = 0, START_EASE, False, None
        for h in self.history:
            day, rating = date.fromisoformat(h['date']), h['rating']
            if rating not in SUCCESS:
                interval = RETRY_DAYS
            elif not learned:
                interval = FIRST_INTERVAL[rating]
                learned = True
            else:
                base = max(interval, (day - prev).days)
                interval = round(base * ease * (1.3 if rating == 'easy' else 1))
            interval = min(MAX_INTERVAL, max(1, interval))
            ease = min(MAX_EASE, max(MIN_EASE, ease + EASE_DELTA[rating]))
            prev = day
        return interval

    def srs_due(self) -> date | None:
        if not self.history:
            return None
        return self.last_attempt() + timedelta(self.srs_interval())


def load_problems(state: dict) -> dict[int, Problem]:
    '''The review pool: core NeetCode problems plus recorded new ones.'''
    by_num, by_title = scan_solutions()
    seeds = git_add_dates()

    def make(num, title, diff, category, solution, slug=None):
        seed = seeds.get(solution.name) if solution else None
        history = state['history'].get(str(num), [])
        return Problem(num, title, diff, category, solution, seed, history,
                       slug)

    problems = {}
    for num, (title, diff, category) in CORE.items():
        # Title first: a header with the wrong number shouldn't shadow it
        solution = by_title.get(normalize(title)) or by_num.get(num)
        problems[num] = make(num, title, diff, category, solution)
    for key, meta in state['added'].items():
        num = int(key)
        solution = by_num.get(num)
        problems[num] = make(num, meta['title'], meta['diff'],
                             meta['category'], solution, meta.get('slug'))
    return problems

def queued_problem(entry: dict, problems: dict) -> Problem:
    if entry['num'] in problems:
        return problems[entry['num']]
    return Problem(entry['num'], entry['title'], entry['diff'], OTHER,
                   slug=entry.get('slug'))


# --- Selection --------------------------------------------------------------

def eligible(p: Problem, today: date) -> bool:
    if p.last_attempt() == today:
        return False
    return not p.missed() or p.retry_date() <= today

def rank_rotation(pool: list[Problem], today: date) -> list[Problem]:
    '''Front of the line: oldest last success first, never solved first.'''
    return sorted(pool, key=lambda p: (p.last_success() or date.min, p.num))

def rank_srs(pool: list[Problem], today: date) -> list[Problem]:
    '''Most overdue relative to interval first; untried problems first.'''
    def key(p):
        if not p.history:
            return (0, p.last_success() or date.min, p.num)
        overdue = (today - p.last_attempt()).days / p.srs_interval()
        return (1, -overdue, p.num)
    return sorted(pool, key=key)

RANKERS = {'rotation': rank_rotation, 'srs': rank_srs}

def category_sizes(problems: dict) -> dict:
    sizes = {}
    for p in problems.values():
        sizes[p.category] = sizes.get(p.category, 0) + 1
    return sizes

def recent_attempts(problems: dict, today: date) -> dict:
    start = (today - timedelta(BALANCE_DAYS)).isoformat()
    counts = {}
    for p in problems.values():
        n = sum(1 for h in p.history if h['date'] >= start)
        counts[p.category] = counts.get(p.category, 0) + n
    return counts

def pick_old(problems: dict, system: str, today: date, exclude: set,
             used: set) -> Problem | None:
    '''The next old problem, given the queued numbers and categories.'''
    pool = [p for p in problems.values()
            if eligible(p, today) and p.num not in exclude]
    retries = sorted((p for p in pool if p.missed()),
                     key=lambda p: p.last_attempt())
    ranked = [p for p in RANKERS[system](pool, today) if not p.missed()]
    shortlist = retries + ranked[:SHORTLIST]
    if not shortlist:
        return None

    fresh = [p for p in shortlist if p.category not in used] or shortlist
    urgent = [p for p in fresh if p.missed()]
    if urgent:
        return urgent[0]

    sizes = category_sizes(problems)
    total = sum(sizes.values())
    recent = recent_attempts(problems, today)
    attempts = sum(recent.values())

    def deficit(category):
        return sizes[category] / total * attempts - recent.get(category, 0)

    return max(fresh, key=lambda p: (deficit(p.category), -fresh.index(p)))

def new_candidates(problems: dict, state: dict, config: dict) -> list[dict]:
    '''LeetCode mediums and hards not solved here or on LeetCode.'''
    by_num, _ = scan_solutions()
    queued = {e['num'] for e in state['queue']}
    return [
        {'num': num, **q}
        for num, q in sorted(load_leetcode().items())
        if q['diff'] in 'MH' and not q['solved']
        and (config['include_premium'] or not q['premium'])
        and num not in by_num and num not in problems
        and num not in ALL_PROBLEMS and num not in queued
    ]

def fill_queue(state: dict, problems: dict, config: dict, system: str,
               today: date) -> None:
    '''Top the queue up to per_day. Queued problems are never replaced.'''
    queue = state['queue']
    rng = random.Random(f'{today}:{len(state["history"])}:{len(queue)}')
    while len(queue) < config['per_day']:
        entry = {'since': today.isoformat()}
        candidates = (new_candidates(problems, state, config)
                      if rng.random() < config['new_chance'] else [])
        if candidates:
            q = rng.choice(candidates)
            entry |= {'num': q['num'], 'new': True, 'title': q['title'],
                      'slug': q['slug'], 'diff': q['diff']}
        else:
            current = [queued_problem(e, problems) for e in queue]
            p = pick_old(problems, system, today,
                         {c.num for c in current},
                         {c.category for c in current})
            if not p:
                break
            entry['num'] = p.num
        queue.append(entry)


# --- Presentation -----------------------------------------------------------

def rel(path: Path) -> str:
    try:
        return str(path.relative_to(Path.cwd()))
    except ValueError:
        return str(path)

def make_scratch(p: Problem, today: date) -> Path:
    '''Blank workspace containing only the problem statement.'''
    SCRATCH.mkdir(exist_ok=True)
    stem = p.solution.stem if p.solution else \
        (p.slug or f'problem_{p.num}').replace('-', '_')
    path = SCRATCH / f'{stem}.py'

    # Keep today's in-progress work; replace anything older
    if path.exists() and date.fromtimestamp(path.stat().st_mtime) >= today:
        return path

    docstring = None
    if p.solution:
        m = re.match(r"\s*('''|\"\"\")(.*?)\1", p.solution.read_text(), re.S)
        if m:
            docstring = m[0].strip()
    if not docstring:
        docstring = f"'''\n{p.title} (#{p.num})\n\n{p.link}\n'''"
    path.write_text(docstring + '\n\n\n')
    return path

def describe(p: Problem, entry: dict | None, system: str, today: date) -> str:
    if entry and entry.get('new'):
        note = 'new problem'
    elif p.missed():
        note = f'retry (missed {p.last_attempt()})'
    else:
        last = p.last_success()
        note = (f'last solved {last} ({(today - last).days}d ago)' if last
                else 'never solved')
        if system == 'srs' and p.history:
            late = (today - p.srs_due()).days
            note += f', interval {p.srs_interval()}d'
            if late > 0:
                note += f', {late}d overdue'
    if entry:
        waiting = (today - date.fromisoformat(entry['since'])).days
        if waiting:
            note += f'; in your queue {waiting}d'
    return note

def issue_link(config: dict, num: int, rating: str) -> str:
    query = urllib.parse.urlencode({
        'title': f'done {num} {rating}',
        'body': 'Submit to record this. To log minutes, add them to the '
                f'title, e.g. "done {num} {rating} 18".',
    })
    return f'https://github.com/{config["github_repo"]}/issues/new?{query}'

def solution_link(config: dict, p: Problem) -> str | None:
    if not p.solution:
        return None
    return (f'https://github.com/{config["github_repo"]}/blob/'
            f'{config["branch"]}/problems/{p.solution.name}')


# --- Commands ---------------------------------------------------------------

def cmd_today(args, state, problems, config, today):
    print(f'{today:%a %Y-%m-%d}  system: {args.system}')
    if not state['queue']:
        print('\nQueue is empty; the next email fills it.')
        return
    for entry in state['queue']:
        p = queued_problem(entry, problems)
        scratch = make_scratch(p, today)
        print(f'\n#{p.num} {p.title}  ({p.category} | {p.diff} | '
              f'{p.minutes}m)')
        print(f'    {describe(p, entry, args.system, today)}')
        print(f'    {p.link}')
        print(f'    solve in: {rel(scratch)}')
        if p.solution:
            print(f'    check:    {rel(p.solution)}  (after!)')
    if len(state['queue']) < config['per_day']:
        print('\nThe next problem arrives in the next email.')
    print('\nAfterward: python review.py done NUM again|hard|good|easy '
          '[--min M]')

def record(state, problems, num, rating, minutes, category, today) -> str:
    '''Log an attempt and drop it from the queue. Returns a summary.'''
    iso = today.isoformat()
    if num in ALL_PROBLEMS and num not in CORE:
        raise SystemExit(f'#{num} is an easy NeetCode problem; easies are '
                         'excluded.')
    entry = next((e for e in state['queue'] if e['num'] == num), None)
    if num not in problems:
        lc = load_leetcode().get(num, {})
        meta = entry if entry and entry.get('new') else lc
        state['added'][str(num)] = {
            'title': meta.get('title', f'Problem #{num}'),
            'slug': meta.get('slug'),
            'diff': meta.get('diff', 'M'),
            'category': category or OTHER,
        }
    elif category and str(num) in state['added']:
        state['added'][str(num)]['category'] = category

    attempt = {'date': iso, 'rating': rating}
    if minutes:
        attempt['minutes'] = minutes
    state['history'].setdefault(str(num), []).append(attempt)
    state['queue'] = [e for e in state['queue'] if e['num'] != num]
    save_state(state)

    p = load_problems(state)[num]
    lines = [f'#{num} {p.title}: {rating}']
    if p.missed():
        lines.append(f'Eligible again on {p.retry_date()}.')
    else:
        lines.append('Rotation: back of the line. '
                     f'SRS: due {p.srs_due()} ({p.srs_interval()}d).')
    if minutes and minutes > p.minutes and rating in SUCCESS:
        lines.append(f'Note: {minutes}m is over the {p.minutes}m target; '
                     'that is a "hard".')
    if not p.solution:
        lines.append('No solution file yet. Save yours in problems/ with a '
                     f'"{p.title} (#{num})" header.')
    if not entry:
        lines.append('(It was not in the queue; the queue is unchanged.)')
    return '\n'.join(lines)

def cmd_done(args, state, problems, config, today):
    summary = record(state, problems, args.num, args.rating, args.min,
                     args.category, today)
    print(summary)
    if not args.offline and not IN_CI:
        git_push(f'Record review: #{args.num} {args.rating}')

def cmd_issue(args, state, problems, config, today):
    '''Record a result from an issue title like "done 146 good 18".'''
    m = re.fullmatch(r'\s*done\s+#?(\d+)\s+(again|hard|good|easy)'
                     r'(?:\s+(\d+))?\s*', args.title, re.I)
    if not m:
        raise SystemExit('Expected a title like "done 146 good" or '
                         '"done 146 good 18".')
    print(record(state, problems, int(m[1]), m[2].lower(),
                 int(m[3]) if m[3] else None, None, today))

def email_body(state, problems, config, system, today) -> tuple[str, str]:
    text, rows = [], []
    for entry in state['queue']:
        p = queued_problem(entry, problems)
        label = f'#{p.num} {p.title}'
        meta = (f'{DIFFICULTY[p.diff]} · {p.minutes} min · '
                f'{describe(p, entry, system, today)}')
        solution = solution_link(config, p)
        links = {r: issue_link(config, p.num, r) for r in RATINGS}

        text += [label, f'  {meta}', f'  {p.link}']
        if solution:
            text.append(f'  your solution (after!): {solution}')
        text += [f'  {r}: {links[r]}' for r in RATINGS] + ['']

        record_links = ' · '.join(
            f'<a href="{html.escape(links[r])}">{r}</a>' for r in RATINGS)
        check = (f' · <a href="{html.escape(solution)}">your solution</a> '
                 '(after!)' if solution else '')
        rows.append(
            f'<h3 style="margin:20px 0 4px">'
            f'<a href="{html.escape(p.link)}">{html.escape(label)}</a></h3>'
            f'<div style="color:#555">{html.escape(meta)}{check}</div>'
            f'<div style="margin-top:6px">Record: {record_links}</div>')

    footer = ('Or locally: python problems/review/review.py done NUM RATING. '
              'Problems stay in the queue until you record them.')
    text.append(footer)
    body = (f'<div style="font-family:sans-serif;max-width:600px">'
            f'{"".join(rows)}<p style="color:#777;margin-top:24px">'
            f'{html.escape(footer)}</p></div>')
    return '\n'.join(text), body

def send_email(subject: str, text: str, body: str) -> None:
    payload = {
        'from': os.environ.get('EMAIL_FROM')
                or 'LeetCode Review <onboarding@resend.dev>',
        'to': [os.environ['EMAIL_TO']],
        'subject': subject,
        'text': text,
        'html': body,
    }
    request = urllib.request.Request(
        'https://api.resend.com/emails', data=json.dumps(payload).encode(),
        headers={'Authorization': f'Bearer {os.environ["RESEND_API_KEY"]}',
                 'Content-Type': 'application/json',
                 'User-Agent': 'dsa-library-review'})
    with urllib.request.urlopen(request, timeout=30) as response:
        response.read()

def cmd_email(args, state, problems, config, today):
    '''Fill the queue and email it, once per day at send_hour or later.'''
    now = datetime.now(ZoneInfo(config['timezone']))
    if not (args.force or args.dry_run):
        if state.get('last_email') == today.isoformat():
            print('Already sent today.')
            return
        if now.hour < config['send_hour']:
            print(f'Not {config["send_hour"]}:00 yet in {config["timezone"]}.')
            return

    fill_queue(state, problems, config, args.system, today)
    if not state['queue']:
        print('Nothing to send.')
        return
    titles = [queued_problem(e, problems) for e in state['queue']]
    subject = 'LeetCode today: ' + ', '.join(
        f'#{p.num} {p.title}' for p in titles)
    text, body = email_body(state, problems, config, args.system, today)

    if args.dry_run:
        print(subject + '\n\n' + text)
        return
    send_email(subject, text, body)
    state['last_email'] = today.isoformat()
    save_state(state)
    print(f'Sent: {subject}')

def cmd_stats(args, state, problems, config, today):
    pool = list(problems.values())
    tried = [p for p in pool if p.history]
    print(f'Pool: {len(pool)} problems ({len(CORE)} NeetCode, '
          f'{len(pool) - len(CORE)} new); {len(tried)} practiced here')
    if load_leetcode():
        print(f'{len(new_candidates(problems, state, config))} new problems '
              'available (unsolved mediums and hards)')
    else:
        print('No usable leetcode_problems.json, so no new problems will be '
              'picked.')

    print('\nQueue:')
    for entry in state['queue'] or [{}]:
        if entry:
            p = queued_problem(entry, problems)
            print(f'  #{p.num} {p.title}: '
                  f'{describe(p, entry, args.system, today)}')
        else:
            print('  (empty; the next email fills it)')

    retries = sorted((p for p in pool if p.missed()), key=Problem.retry_date)
    if retries:
        print('\nWaiting for retry:')
        for p in retries:
            print(f'  {p.retry_date()}  #{p.num} {p.title}')

    print(f'\nNext in line ({args.system}, before category balance):')
    queued = {e['num'] for e in state['queue']}
    ranked = [p for p in RANKERS[args.system](
                  [p for p in pool if eligible(p, today)], today)
              if not p.missed() and p.num not in queued]
    for p in ranked[:5]:
        print(f'  #{p.num} {p.title}: {describe(p, None, args.system, today)}')

    if args.system == 'srs':
        due = [p for p in tried if p.srs_due() <= today]
        print(f'\nSRS: {len(due)} due or overdue, '
              f'{len(pool) - len(tried)} never practiced here')

    sizes = category_sizes(problems)
    recent = recent_attempts(problems, today)
    attempts = sum(recent.values())
    print(f'\nCategories (attempts in last {BALANCE_DAYS}d vs fair share; '
          'misses all time):')
    for category in list(NEETCODE_150) + [OTHER]:
        if category not in sizes:
            continue
        group = [p for p in pool if p.category == category]
        fair = sizes[category] / len(pool) * attempts
        misses = sum(h['rating'] not in SUCCESS
                     for p in group for h in p.history)
        print(f'  {category:<24} {sizes[category]:>3} problems  '
              f'{recent.get(category, 0):>3} / {fair:4.1f}  '
              f'misses {misses}')


def main():
    config = load_config()
    today = datetime.now(ZoneInfo(config['timezone'])).date()
    parser = argparse.ArgumentParser(description='NeetCode practice scheduler')
    parser.add_argument('--date', type=date.fromisoformat, default=today)
    parser.add_argument('--system', choices=tuple(RANKERS),
                        default=config['system'])
    parser.add_argument('--offline', action='store_true',
                        help='skip git pull/push')
    sub = parser.add_subparsers(dest='cmd', required=True)

    sub.add_parser('today').set_defaults(func=cmd_today)

    p = sub.add_parser('done')
    p.add_argument('num', type=int)
    p.add_argument('rating', choices=RATINGS)
    p.add_argument('--min', type=int, help='minutes taken')
    p.add_argument('--category', help='category for a new problem')
    p.set_defaults(func=cmd_done)

    p = sub.add_parser('issue', help='record from an issue title (CI)')
    p.add_argument('title')
    p.set_defaults(func=cmd_issue)

    p = sub.add_parser('email', help='fill the queue and send it (CI)')
    p.add_argument('--dry-run', action='store_true',
                   help='print the email; send and save nothing')
    p.add_argument('--force', action='store_true',
                   help='send even if already sent or before send_hour')
    p.set_defaults(func=cmd_email)

    sub.add_parser('stats').set_defaults(func=cmd_stats)

    # Let global options appear after the subcommand too
    argv, front = sys.argv[1:], []
    for flag, takes_value in (('--date', True), ('--system', True),
                              ('--offline', False)):
        if flag in argv:
            i = argv.index(flag)
            n = 2 if takes_value else 1
            front += argv[i:i + n]
            argv = argv[:i] + argv[i + n:]
    args = parser.parse_args(front + argv)

    if args.cmd in ('today', 'done', 'stats') and not (args.offline or IN_CI):
        git_pull()
    state = load_state()
    args.func(args, state, load_problems(state), config, args.date)


if __name__ == '__main__':
    main()
