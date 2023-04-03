'''
Merge Intervals (#56)

Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge
all overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.
'''

import heapq

# Same sweep line algorithm used in insert-interval.py
def merge(intervals: list[list[int]]) -> list[list[int]]:
    pq = []
    for start, end in intervals:
        heapq.heappush(pq, (start, -1))
        heapq.heappush(pq, (end, 1))

    intervals = []
    start, balance = None, 0
    while pq:
        i, val = heapq.heappop(pq)
        if start is None:
            start = i
        balance += val
        if balance == 0:
            intervals.append([start, i])
            start = None

    return intervals


# Faster, simpler algorithm
def merge2(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort()

    result = []
    prev = intervals[0]
    for curr in intervals:
        if curr[0] <= prev[1]:
            prev[1] = max(prev[1], curr[1])
        else:
            result.append(prev)
            prev = curr
    result.append(prev)

    return result


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(merge(intervals))

'''
Given a = [start_a, end_a] and b = [start_b, end_b] where start_a <= start_b:

When do a and b overlap?    When b[0] <= a[1].
If they overlap, what is the result of merging them?    [a[0], max(a[1], b[1])]
'''

