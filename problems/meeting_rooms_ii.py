'''
Meeting Rooms II (#253)

Given an array of meeting time intervals consisting of start and end times
`[[s_1, e_1], [s_2, e_2], ...]` where `s_i < e_i`, find the minimum number of
conference rooms required to host all meetings.
'''

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


# Time: O(nlogn)
# Auxiliary space: O(n)
def min_rooms(intervals: list[Interval]) -> int:
    brackets = []
    for iv in intervals:
        brackets.append((iv.start, 1))
        brackets.append((iv.end, -1))
    brackets.sort()

    count = 0
    rooms = 0
    for b in brackets:
        count += b[1]
        rooms = max(rooms, count)

    return rooms


# Time: O(nlogn)
# Auxiliary space: O(n)
def min_rooms2(intervals: list[Interval]) -> int:
    starts = []
    ends = []
    for iv in intervals:
        starts.append(iv.start)
        ends.append(iv.end)
    starts.sort()
    ends.sort()

    count = 0
    rooms = 0
    i, j = 0, 0
    while i < len(starts):
        if starts[i] < ends[j]:
            count += 1
            i += 1
        else:
            count -= 1
            j += 1
        rooms = max(rooms, count)

    return rooms


if __name__ == '__main__':
    intervals = [Interval(0, 40), Interval(5, 10), Interval(15, 20)]
    print(min_rooms(intervals))

'''
The above solutions are slightly different ways of implementing a sweep line
algorithm.
'''

