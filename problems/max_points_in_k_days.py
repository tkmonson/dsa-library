'''
Max Points in K Days (Amazon OA)

Let `t` be an integer array that represents a tournament, where each element in
the array represents a "sprint" in the tournament. A sprint with value `x` is
`x` days long. A participant in the tournament will earn a number of points for
each day that they compete. They will earn 1 point for competing on the first
day of a sprint, 2 points for the second day, and so on. Let `k` be the number
of consecutive days in which the participant will compete (they may start and
end on any day). The tournament is cyclic: the participant may start with less
than `k` days left in the tournament and wrap around to compete in the first
days of the tournament.

Return the maximum number of points the participant can earn
in 'k' consecutive days in the tournament.

E.g. t = [7, 4, 3, 7, 2] would expand to a day array of
     [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 1, 2].
     Given k = 8, the output would be 32 (starting at i = 3 of the day array).

THIS SOLUTION IS UNTESTED, MAY NOT BE PERFECTLY CORRECT.
'''

from collections import deque

# Time: O(m * n), where m = max(t), n = len(t)
# Auxiliary space: O(k)
def max_points_in_k_days(t: list[int], k: int) -> int:
    # Copy first sprints that sum to k, append to t for cyclic requirement
    b = k
    for i in range(len(t)):
        if b <= 0:
            break
        b -= t[i]
        t.append(t[i])

    q = deque([0] * k)
    points = 0
    max_points = 0
    for sprint in t:
        for day in range(1, sprint + 1):
            points -= q.popleft()
            q.append(day)
            points += day
            max_points = max(max_points, points)

    return max_points


if __name__ == '__main__':
    t = [7, 4, 3, 7, 2]
    k = 8
    print(max_points_in_k_days(t, k))

'''
This is a twist on a sliding window problem. You need to slide a k-length
window across the day array but expanding the sprint array into the day array
would be way too memory-intensive, given high sprint values. Thus, you need to
slide the window across the day array without actually instantiating the day
array.

Often times, in sliding window problems, the window is represented with two
pointers, as this is the most memory-efficient representation. This will not
work for this problem because we do not have access to indicies of days within
sprints. Thus, we need to represent the window in a different way, as a queue.

We can slide this window through the day array with a for-loop, by looping
through range(1, sprint + 1) for each sprint.

(You could probably write a solution that is O(1) in memory, but it would be
unintuitive and almost certainly slower because it would require a lot of small
arithmetic operations.)
'''

