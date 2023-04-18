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


if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 9
    print(binary_search(nums, target))

