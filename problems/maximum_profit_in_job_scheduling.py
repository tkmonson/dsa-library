'''
Maximum Profit in Job Scheduling (#1235)

There are `n` jobs, where each job is scheduled to be done from `start_time[i]`
to `end_time[i]` for a profit of `profit[i]`. Given `start_time`, `end_time`,
and `profit` arrays, return the maximum profit that can be made such that no
two jobs overlap. A job that ends at time `t` and a job that starts at time `t`
do not overlap.
'''

import bisect
from functools import cache
import heapq

def job_scheduling_top_down(start_time: list[int], end_time: list[int],
                            profit: list[int]) -> int:
    jobs = sorted(zip(start_time, end_time, profit))
    n = len(jobs)
    start_time.sort()

    @cache
    def dp(i: int) -> int:
        if i >= n: return 0

        j = bisect.bisect_left(start_time, jobs[i][1])
        return max(dp(i + 1), dp(j) + jobs[i][2])

    return dp(0)


def job_scheduling_bottom_up(start_time: list[int], end_time: list[int],
                             profit: list[int]) -> int:
    jobs = sorted(zip(start_time, end_time, profit))
    n = len(jobs)
    start_time.sort()

    dp = [0 for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        j = bisect.bisect_left(start_time, jobs[i][1])
        dp[i] = max(dp[i + 1], dp[j] + jobs[i][2])

    return dp[0]

'''
The overall problem can be restated as "find the maximum profit that can be
earned from jobs 0 through n - 1 such that no two jobs overlap." Similar to the
knapsack problem, we can either take or not take each job, and we can express
the overall problem in terms of subproblems. Its solution is equal to the
greater of the following:

    1. the profit of job 0 + the maximum profit of jobs j through n - 1, where
       j is the index of the job that starts soonest after job 0 ends
    2. the maximum profit of jobs 1 through n - 1

This problem has optimal substructure and overlapping subproblems, so dynamic
programming is appropriate. We can start choosing items from the left or right,
but the example above starts from the left, so let's continue with that
convention. Let dp[i] represent the maximum profit that can be earned from jobs
i through n - 1 (dp[0] represents the overall problem). To generalize:

    dp[i] = max(profit[i] + dp[j], dp[i + 1])

To find j, you could linearly search the unsorted start_time array each time
you take a job (n times) or you could sort start_time and perform a binary
search each time you take a job. That's O(n^2) vs. O(nlogn), so the latter is
the better option.

This is the top-down approach, where we start with the largest problem dp[0].
In the bottom-up approach, we start with the smallest problem dp[n - 1] and
fill in the dp array right to left until dp[0] is solved. In this case, we
choose items from right to left, but it would be done left to right if dp[i]
were defined as "the maximum profit that can be earned from jobs 0 through i."
'''

def job_scheduling_sweep_line(start_time: list[int], end_time: list[int],
                              profit: list[int]) -> int:
    n = len(start_time)
    events = []
    for i in range(n):
        events.append((start_time[i], True, i))
        events.append((end_time[i], False, i))

    events.sort()  # if end and start brackets occur at the same time,
                   # the end brackets should come first

    potential_max = [0] * n
    actual_max = 0

    for _, is_start, i in events:
        if is_start:
            potential_max[i] = actual_max + profit[i]
        else:
            actual_max = max(actual_max, potential_max[i])

    return actual_max

'''
Break job intervals into individual start and end "brackets" and sweep a line
across them left to right. When we encounter the start bracket of job i,
actual_max represents the max profit of jobs that end before job i starts. It
may or may not be optimal to "take" job i, but let's assume that it is and
store the result (actual_max + profit[i]) in potential_max[i]. We won't know if
taking job i is optimal until we encounter the end bracket of job i. Meanwhile,
we may encounter other jobs and add their profit to actual_max. When we
encounter the end bracket of job i, we will "take" job i if potential_max[i] is
still greater than actual_max.
'''

def job_scheduling_heap(start_time: list[int], end_time: list[int],
                        profit: list[int]) -> int:
    jobs = list(zip(start_time, end_time, profit))
    jobs.sort()
    
    heap = []        
    curr_profit = 0
    result = 0
    
    for start, end, p in jobs:
        while heap and heap[0][0] <= start:
            _, prev_profit = heapq.heappop(heap)
            curr_profit = max(curr_profit, prev_profit)
        
        heapq.heappush(heap, (end, curr_profit + p))
        result = max(result, curr_profit + p)

    return result

'''
If the current job overlaps the job at the top of the heap, push the current
job on the heap. Else, pop the heap and find the max profit of all jobs up to
and including that popped job; continue to pop until the current job and the
job at the top of the heap overlap, at which point, push the current job on the
heap.
'''

if __name__ == '__main__':
    start_time = [1, 2, 3, 4, 6]
    end_time = [3, 5, 10, 6, 9]
    profit = [20, 20, 100, 70, 60]
    print(job_scheduling_top_down(start_time, end_time, profit))

