'''
Binary Search (#704)

Given an integer array `nums` that is sorted in ascending order and an integer
`target`, write a function that searches for `target` in `nums` in O(logn)
time. If target exists, return its index. Otherwise, return -1.
'''

def binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1

def binary_search_leftmost(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

'''
Return the index of the leftmost target. If target does not exist in nums, the
returned value is the number of elements in nums that are less than the target
(the rank of target in nums).

bisect.bisect_left(nums, target)
'''

def binary_search_rightmost(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    return right - 1

'''
Return the index of the rightmost target. If target does not exist in nums,
(n - right) is the number of elements in nums that are greater than the target.

bisect.bisect_right(nums, target) - 1
'''

if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(binary_search(nums, target))

