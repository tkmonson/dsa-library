'''
Disk Space Analysis

There are `n` computers arranged in a row and the available disk space for
these computers is contained in the `disk_space` array. For each contiguous
segment of `k` computers, find the minimum disk space. Return the maximum disk
space of these minima.
'''

import heapq, random

def analyze_disk_space(disk_space: list[int], k: int) -> int:
    heap = []

    for i in range(k):
        heapq.heappush(heap, (disk_space[i], i))
    result = heap[0][0]

    for i in range(k, len(disk_space)):
        heapq.heappush(heap, (disk_space[i], i))

        while heap[0][1] <= i - k:
            heapq.heappop(heap)

        result = max(result, heap[0][0])

    return result

'''
The one quirk in this solution is that we allow the heap to contain stale
elements (those outside of the current segment) because removing them from the
inside of the heap as the window slides is not possible. A stale element is
removed only when necessary, when it appears at the top of the heap while we
are calculating the minimum of a segment.
'''

if __name__ == '__main__':
    disk_space = [random.randint(1, 100) for _ in range(20)]
    k = 3
    print(disk_space)
    print(analyze_disk_space(disk_space, k))

