'''
Sliding Window Maximum (#239)

Given an array of integers `nums` and an integer `k` that denotes the size of a
sliding window that moves from left to right, one element at a time, across
`nums`, return an array of integers `result` where `result[i]` is the maximum
element contained in the sliding window that starts at index `i` of `nums`.

E.g. nums = [1, 3, -1, -3, 5, 3, 6, 7],  k = 3  =>  [3, 3, 5, 5, 6, 7]
'''

from collections import defaultdict, deque
import heapq

# Time: O(n)
# Auxiliary space: O(n)
def max_sliding_window(nums: list[int], k: int) -> list[int]:
    result = []
    queue = deque()
    left = right = 0

    while right < len(nums):
        while queue and nums[queue[-1]] < nums[right]:
            queue.pop()
        queue.append(right)

        if queue[0] < left:
            queue.popleft()

        if right >= k - 1:
            result.append(nums[queue[0]])
            left += 1
        right += 1

    return result

'''
This solution uses a monotonically decreasing deque. While traversing the
array, push elements into the deque. If the next element is greater than the
last item in the deque, dequeue items until this is no longer the case. Because
of the invariant, the leftmost element in the deque is always the greatest
element.
'''

# Time: O(n)
# Auxiliary space: O(n)
def max_sliding_window2(nums: list[int], k: int) -> list[int]:
    result = []
    queue = deque()

    for right in range(k - 1):
        while queue and nums[queue[-1]] < nums[right]:
            queue.pop()
        queue.append(right)

    for right in range(k - 1, len(nums)):
        while queue and nums[queue[-1]] < nums[right]:
            queue.pop()
        queue.append(right)

        if queue[0] < right - k + 1:
            queue.popleft()

        result.append(nums[queue[0]])

    return result

'''
A slightly faster version of the first solution (removes a conditional branch,
uses two for loops instead of one while loop).
'''

# Slower
def max_sliding_window3(nums: list[int], k: int) -> list[int]:
    result = []
    heap = []
    count = defaultdict(lambda: 0)
    for i in range(k):
        count[nums[i]] += 1
        heapq.heappush(heap, -nums[i])
    left, right = 0, k
    while True:
        while not count[-heap[0]]:
            heapq.heappop(heap)
        result.append(-heap[0])

        if right == len(nums):
            break

        count[nums[left]] -= 1
        left += 1
        count[nums[right]] += 1
        heapq.heappush(heap, -nums[right])
        right += 1

    return result

'''
The dictionary finds what is in the window in O(1) time. The heap finds its
max element in O(1) time. The heap may contain elements that are no longer in
the window, but it will pop them off until it finds the largest element in the
window.
'''

if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(max_sliding_window(nums, k))

