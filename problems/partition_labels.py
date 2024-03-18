'''
Partition Labels (#763)

Given a string, partition it into as many parts as possible so that each letter
appears in at most one part. Return a list representing the size of these
parts.
'''

from collections import defaultdict

# Time: O(n) (fastest)
# Auxiliary space: O(n)
def partition_labels(s: str) -> list[int]:
    last_index = {c: i for i, c in enumerate(s)}
    start, end = 0, 0
    result = []
    for i, c in enumerate(s):
        end = max(end, last_index[c])
        if i == end:
            result.append(end - start + 1)
            start = i + 1

    return result

'''
For each character c in s, it would help to know the index of the last instance
of c because a partition will end on the last instance of some character
contained within it. Map characters to indicies of their last instance. As you
traverse s, start a partition, keep track of its predicted right boundary, and
shift that boundary to the right if you come across a character whose last
instance is to the right of that boundary. Close the partition when you get to
the right boundary.
'''

# Time: O(n)
# Auxiliary space: O(n)
def partition_labels2(s: str) -> list[int]:
    p = []  # left index of partition
    z = []  # size of partition
    d = {}  # letter -> index of partition that letter belongs to
    for i, c in enumerate(s):
        if c in d:
            for _ in range(len(p) - d[c] - 1):
                p.pop()
                z.pop()
            for j in range(p[-1], i + 1):
                d[s[j]] = len(p) - 1
            z[-1] = i - p[-1] + 1
        else:
            d[c] = len(p)
            p.append(i)
            z.append(1)

    return z

'''
Assume the partitions are as small as possible (size of 1) until proven
otherwise. If you come across a character c that was included in a previous
partition P, remove the partitions that came after P and expand P up to c.
'''

# Time: O(n)
# Auxiliary space: O(n)
def partition_labels3(s: str) -> list[int]:
    intervals = []
    d = {}
    for i, c in enumerate(s):
        if c in d:
            intervals[d[c]][1] = i
        else:
            intervals.append([i, i])
            d[c] = len(intervals) - 1

    result = []
    prev = intervals[0]
    for curr in intervals:
        if curr[0] <= prev[1]:
            prev[1] = max(prev[1], curr[1])
        else:
            result.append(prev[1] - prev[0] + 1)
            prev = curr
    result.append(prev[1] - prev[0] + 1)

    return result

'''
This solution uses the strategy from the "Merge Intervals" problem. Get a list
of intervals from the first instance to the last instance of a character. Merge
the intervals such that they do not overlap.
'''

if __name__ == '__main__':
    s = 'ababcbacadefegdehijhklij'
    print(partition_labels2(s))
    
