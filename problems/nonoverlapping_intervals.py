'''
Non-Overlapping Intervals (#435)

Given an array of intervals, return the minimum number of intervals you need to
remove to make the rest of the intervals non-overlapping.
'''

# Time: O(nlogn)
# Auxiliary space: O(1)
def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    intervals.sort()

    result = 0
    prev_end = intervals[0][1]
    for start, end in intervals[1:]:
        if start >= prev_end:
            prev_end = end
        else:
            result += 1
            prev_end = min(prev_end, end)

    return result

'''
Traverse through the intervals in ascending order of starting point.

[  ] [  ]  You know that these intervals do not overlap because the start of
           the second is greater than or equal to the end of the first. Which
end should we use to compare to the start of a third interval? The second end
because we now know that no interval will overlap the first interval.

[    ]     You know that these intervals overlap because the start of the
  [  x  ]  second is less than the end of the first.

[   x   ]  Same in this case. Which end should we use to compare to the start
   [ ]     of a third interval? In both cases, the lesser end (i.e. we delete
           the interval with the greater end, because it is more likely to
overlap with future intervals).
'''

if __name__ == '__main__':
    intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
    print(erase_overlap_intervals(intervals))

