'''
Task Scheduler (#621)

A CPU needs to complete a set of tasks, which is represented by an array of
uppercase letters, where each letter represents a different kind of task. The
tasks can be done in any order, and each task takes one unit of time to
complete. For each unit of time, the CPU can either complete a task or be idle.
Given an array of tasks and a non-negative integer `n` that represents a
cooldown period between two tasks of the same kind (which are represented by
the same letter), such that there must be at least `n` units of time between
such tasks, return the minimum number of units of time that the CPU requires to
complete all of the tasks.


E.g.  tasks = ['A', 'A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F', 'G'],
          n = 2  => 16

(One possible schedule is [A, B, C, A, D, E, A, F, G, A, i, i, A, i, i, A]
where i represents an idle operation.)
'''

from collections import Counter

def least_interval(tasks: list[str], n: int) -> int:
    counts = list(Counter(tasks).values())
    max_count = max(counts)

    slot_size = n + 1
    num_slots = max_count - 1
    num_ties = counts.count(max_count)
    return max(slot_size * num_slots + num_ties, len(tasks))

'''
Consider tasks = [A, A, A, A, A], n = 2. The tasks need to be scheduled like:

    [A, i, i, A, i, i, A, i, i, A, i, i, A]

Now consider that there are also 4 'B' tasks:

    [A, B, i, A, B, i, A, B, i, A, B, i, A]

If 'A' is the most frequent task, all other less frequent tasks can be
scheduled in between the 'A' tasks:

    [A, B, C, D, E, A, B, C, D, E, A, B, C, D, E, A, B, C, D, E, A]

Now consider tasks = [A, A, A, A, A, B, B, B, B, B], n = 2:

    [A, B, i, A, B, i, A, B, i, A, B, i, A, B]
    |________|________|________|________|

In cases where idle operations are necessary, we can conceive of there being
max_count - 1 "slots," each of size n + 1, followed by one task from each of
the tasks that tie for most frequent. Thus, the number of time units required
for such cases can be expressed as:

    (n + 1) * (max_count - 1) + num_ties

In the best case, where no idle operations are necessary, the number of time
units required is simply equal to the number of tasks.
'''

if __name__ == '__main__':
    tasks = ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'D', 'D', 'D']
    n = 2
    print(least_interval(tasks, n))

