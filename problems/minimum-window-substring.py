'''
Minimum Window Substring (#76)

Given two non-empty strings `s` and `t`, return a minimum window substring of
`s` such that every character in t, including duplicates, is included in the
window. If there is no such substring, return the empty string.
'''

from collections import Counter, defaultdict

def min_window(s: str, t: str) -> str:
    if len(t) > len(s):
        return ''

    need = defaultdict(int)
    for ch in t:
        need[ch] += 1

    distance_from_match = len(t)
    left = 0
    window = (0, float('inf'))

    for right, ch in enumerate(s):
        if need[ch] > 0:
            distance_from_match -= 1
        need[ch] -= 1

        if distance_from_match == 0:
            while True:
                ch = s[left]
                if need[ch] == 0:
                    break
                need[ch] += 1
                left += 1

            if right - left < window[1] - window[0]:
                window = (left, right)

            need[ch] += 1
            distance_from_match += 1
            left += 1

    return '' if window[1] == float('inf') else s[window[0] : window[1] + 1]

'''
As you slide the window, you have to keep track of which characters and how
many of each you still need to make a "match" (a substring that contains all
characters in t). A map is a natural choice for this. You also need to know
how many of these characters in total you still need to make a match (which can
be thought of as your "distance" from a match), and it would be most efficient
to know this without having to scan the map each time, so it should be stored
separately.

This solution slides the window along like an inchworm: the right delimiter
moves to the right until a match is found, and the left delimiter moves to the
right until the window is no longer a match. Right before the window goes from
match to not-match, its position is saved if it is the smallest match window
encountered so far.

t = ABC, s = ADOBECODEBANC
             ------
              -----
              ----------
                   -----
                   -------
                      ----  => BANC
'''

def min_window2(s: str, t: str) -> str:
    if len(t) > len(s):
        return ''

    c = Counter(t)
    distance = len(t)
    left, right = 0, 0
    window = (0, float('inf'))

    while right < len(s):
        while right < len(s) and distance:
            if s[right] in c:
                c[s[right]] -= 1
                distance -= (c[s[right]] >= 0)
            right += 1

        while not distance:
            if s[left] in c:
                c[s[left]] += 1
                distance += (c[s[left]] > 0)
            left += 1

        if left > 0:
            left -= 1
            if (size := right - left) < window[1] - window[0]:
                window = (left, right)
            left += 1

    return '' if window[1] == float('inf') else s[window[0] : window[1]]

'''
Similar to the above solution but with a less elegant loop structure. This
solution also explicitly checks whether a character in s is contained in the
character:count map of t, to avoid putting irrelevant characters into the map.
However, for any character in a given window:
    * non-negative count in map => character is in t
    * negative count in map => character is (not in t) OR
                                            (in t but not needed for a match)
When shrinking a match window from the left, you know that the window will no
longer match when you remove a character with a zero count (and thus increase
its count to 1). This is enough information to write a solution without the
checks described above.
'''

def min_window3(s: str, t: str) -> str:
    if len(t) > len(s):
        return ''

    def f(p: int, add: bool) -> int:
        nonlocal c, distance
        if s[p] in c:
            if add:
                c[s[p]] -= 1
                distance -= (c[s[p]] >= 0)
            else:
                c[s[p]] += 1
                distance += (c[s[p]] > 0)

    c = Counter(t)
    for i in range(len(t)):
        if s[i] in c:
            c[s[i]] -= 1

    distance = 0
    for key in c:
        if c[key] > 0:
            distance += c[key]
    
    min_distance = distance
    left, right = 0, len(t) - 1
    while True:
        if not distance:
            return s[left: right + 1]
        if left == 0:
            while right < len(s) - 1:
                right += 1
                f(right, True)
                f(left, False)
                left += 1
                if not distance:
                    return s[left: right + 1]
                min_distance = min(min_distance, distance)
            for _ in range(min_distance):
                left -= 1
                if left < 0:
                    return ''
                f(left, True)
        else:
            while left > 0:
                left -= 1
                f(left, True)
                f(right, False)
                right -= 1
                if not distance:
                    return s[left: right + 1]
                min_distance = min(min_distance, distance)
            for _ in range(min_distance):
                right += 1
                if right == len(s):
                    return ''
                f(right, True)

'''
My initial solution, slow but passes all test cases. First, it checks all
windows of size len(t), from left to right, and stores the smallest distance
from a match. Then, it increases the size of the window by that distance,
checks all windows of that size, from right to left, and stores the smallest
distance from a match. It continues checking windows back and forth until it
finds a match.

t = ABC, s = ADOBEDCED  ADOBEDCED  ADOBEDCED  ADOBEDCED
             ---            -----  ------       -------
              ---          -----    ------     -------
               ---        -----      ------   -------  => ADOBEDC
                ---      -----        ------
                 ---    -----
                  ---
                   ---
'''

if __name__ == '__main__':
    s = 'ADOBECODEBANC'
    t = 'ABC'
    print(min_window(s, t))

