'''
Insert Interval (#57)

You are given an array of non-overlapping intervals `intervals` where
`intervals[i] = [start_i, end_i]` represents the start and the end of the ith
interval, and `intervals` is sorted in ascending order by `start_i`. You are
also given an interval `new_interval = [start, end]` that represents the start
and end of another interval.

Insert `new_interval` into `intervals` such that `intervals` is still sorted in
ascending order by `start_i` and `intervals` still does not have any
overlapping intervals (merge overlapping intervals if necessary).

Return `intervals` after the insertion.
'''

import heapq

def insert(intervals: list[list[int]],
           new_interval: list[int]) -> list[list[int]]:
    i = 0
    while i < len(intervals) and new_interval[0] >= intervals[i][0]:
        i += 1
    if i != 0 and new_interval[0] <= intervals[i - 1][1]:
        intervals[i - 1][1] = max(intervals[i - 1][1], new_interval[1])
        i -= 1
    else:
        intervals.insert(i, new_interval)

    j = i + 1
    while j < len(intervals) and intervals[i][1] >= intervals[j][0]:
        j += 1
    intervals[i][1] = max(intervals[i][1], intervals[j - 1][1])
    del intervals[i + 1 : j]

    return intervals

'''
Find the insertion index for the new interval by iterating until you find an
interval whose start is greater than the new interval's start (if you don't
find one, you will be inserting at the end of the list). At this point, you
know that a maximum of one interval to the left of the new interval may be
merged. If that left interval is to be merged with the new interval, do so by
setting its end to the greater of the two intervals' ends (this avoids a costly
insert operation). Otherwise, insert the new interval. In either case, the
index pointer should point to the merged/new interval (M). Iterate to the right
of M until you find an interval (R) whose start is greater than M's end. Merge
all intervals that come after M and before R into M.

This solution is very "literal"; that is, it focuses on actually inserting the
new interval into the given interval list. This results in having to handle
edge cases (can't merge left at index 0, can't merge right at index n - 1,
make sure you merge correctly based on how the intervals intersect).
'''

def insert2(intervals: list[list[int]],
            new_interval: list[int]) -> list[list[int]]:
        pq = []
        for start, end in intervals + [new_interval]:
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

'''
This solution uses a sweep line algorithm and a priority queue (heap). Sweep
line algorithms are used to solve planar problems. A line sweeps across a
plane, and events of interest occur, such as the line passing over a point.
Events are processed as they occur, leaving a solved problem behind.

Given:
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    new_interval = [4,8]

We can visualize this as the following:

|            [             ]
|
|   [    ][       ][    ][       ]   [             ]
| 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16

We can then convert the collection of these intervals into a collection of
opening or closing 'brackets,' each represented by a position on a line and a
value that signifies opening or closing type. Add these brackets to a priority
queue such that lower positions have higher priority. Brackets will be dequeued
in the same order that a line would sweep across them from left to right.

When the first opening bracket is encountered, its position is the start of an
interval to be appended to the final list. If the next bracket is closing, the
interval is closed and can be appended; if it is opening, then two closing
brackets must be encountered before the interval is closed (plus an additional
closing bracket for every opening bracket encountered along the way). If -1
signifies an opening bracket and 1 signifies a closing bracket, an interval is
closed when the sum of these values is 0 for all brackets contained within the
interval.
'''

def insert3(intervals: list[list[int]],
            new_interval: list[int]) -> list[list[int]]:
    start, end = new_interval[0], new_interval[1]
    left = [i for i in intervals if i[1] < start]
    right = [i for i in intervals if i[0] > end]
    if left + right != intervals:
        start = min(start, intervals[len(left)][0])
        end = max(end, intervals[~len(right)][1])  # ~x = -x - 1
    return left + [[start, end]] + right

'''
This solution focuses on collecting the intervals that do not overlap with the
new interval, both those to the left of it and those to the right. If the union
of these collections is not equal to the original interval list, then there is
at least one interval that overlaps with the new interval. Merge these
intervals and concatenate the result with the left and right collections to
produce the final list.
'''

def insert4(intervals: list[list[int]],
            new_interval: list[int]) -> list[list[int]]:
    start, end = new_interval[0], new_interval[1]
    parts = merge, left, right = [], [], []
    for i in intervals:
        parts[(i[1] < start) - (i[0] > end)].append(i)
    if merge:
        start = min(start, merge[0][0])
        end = max(end, merge[-1][1])
    return left + [[start, end]] + right

'''
This solution is similar to the one above, but it also explicitly collects the
intervals to be merged with the new interval. For the expression
(i[1] < start) - (i[0] > end):
    1. Interval to the left => True - False = 1
    2. Interval to the right => False - True = -1
    3. Interval overlaps => False - False = 0
'''

def insert5(intervals: list[list[int]],
            new_interval: list[int]) -> list[list[int]]:
    start, end = new_interval[0], new_interval[1]
    left, right = [], []
    for i in intervals:
        if i[1] < start:
            left += i,
        elif i[0] > end:
            right += i,
        else:
            start = min(start, i[0])
            end = max(end, i[1])
    return left + [[start, end]] + right

'''
This solution is very similar to the one above but easier to understand.
'''

if __name__ == '__main__':
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    new_interval = [4,8]
    print(f'intervals: {intervals}, new_interval: {new_interval}')
    print(insert5(intervals, new_interval))

'''
In general, it is much easier to solve this problem by creating a new list
rather than trying to insert the new interval in-place.
'''

