'''
Minimum Interval to Include Each Query (#1851)

You are given a 2D integer array `intervals` where
`intervals[i] = [left_i, right_i]` describes an interval starting at `left_i`
and ending at `right_i` (inclusive). The size of an interval is defined as
`right_i - left_i + 1`. You are also given an integer array `queries`. The
answer to the jth query is the size of the smallest interval `i` such that
`left_i <= queries[j] <= right_i`. If no such interval exists, the answer is
-1. Return an array containing the answers to the queries.

E.g. intervals = [[1, 4], [2, 4], [3, 6], [4, 4]],  queries = [2, 3, 4, 5]
         =>  [3, 3, 1, 4]
'''

import heapq

# Time: O(mlogm + nlogn)
# Auxiliary space: O(m + n)
def min_interval(intervals: list[list[int]], queries: list[int]) -> list[int]:
    heap = []
    results = {}
    intervals.sort()

    i, j = 0, 0
    for q in sorted(set(queries)):  # remove duplicate queries
        while i < len(intervals) and intervals[i][0] <= q:
            left, right = intervals[i]
            heapq.heappush(heap, (right - left + 1, right))
            i += 1
        while heap and heap[0][1] < q:
            heapq.heappop(heap)
        results[q] = heap[0][0] if heap else -1

    return [results[q] for q in queries]

'''
Two insights:

1. Find minimum interval => min-heap
2. You should sort both intervals and queries in the same order (ascending or
   descending). By doing this, you can scan through them together.

Add all intervals with left boundary less than or equal to the current query to
a heap. Pop intervals from the heap until you find one with right boundary
greater than or equal to the current query. This is the minimum interval that
includes the query.

Duplicate queries result in the same answer. Remove them to avoid redundant
computation.
'''

if __name__ == '__main__':
    intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
    queries = [2, 3, 4, 5]
    print(min_interval(intervals, queries))

