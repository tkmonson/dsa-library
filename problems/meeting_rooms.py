'''
Meeting Rooms (#252)

Given an array of meeting time intervals consisting of start and end times
`[[s_1, e_1], [s_2, e_2], ...]` where `s_i < e_i`, determine if a person could
attend all meetings without conflicts.
'''

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


# Time: O(nlogn)
# Auxiliary space: O(1)
def can_attend_meetings(intervals: list[Interval]) -> bool:
    intervals.sort(key=lambda i: i.start)
    for i in range(1, len(intervals)):
        if intervals[i].start < intervals[i - 1].end:
            return False
    return True


if __name__ == '__main__':
    intervals = [Interval(5, 10), Interval(0, 4)]
    print(can_attend_meetings(intervals))

