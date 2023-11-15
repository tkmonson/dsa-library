'''
Kth Largest Element in an Array (#215)

Given an integer array and an integer k, return the kth largest element in the
array (kth largest element in sorted order).
'''

import heapq

# Time: O(n + klogn)
# Auxiliary space: O(1)
def find_kth_largest(nums: list[int], k: int) -> int:
    for i in range(len(nums)):
        nums[i] = -nums[i]
    heapq.heapify(nums)
    for _ in range(k - 1):
        heapq.heappop(nums)
    return -nums[0]


# Time: O(nlogk)
# Auxiliary space: O(k)
def find_kth_largest2(nums: list[int], k: int) -> int:
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        else:
            heapq.heappushpop(heap, num)
    return heap[0]


if __name__ == '__main__':
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(find_kth_largest(nums, k))

