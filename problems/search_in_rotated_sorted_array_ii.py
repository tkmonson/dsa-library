'''
Search in Rotated Sorted Array II (#81)

There is an integer array `nums` sorted in non-decreasing order (not
necessarily with distinct values). Before being passed to your function, `nums`
is rotated at an unknown pivot index `k` (`0 <= k < nums.length`) such that the
resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ...,
nums[k-1]]` (0-indexed). For example, `[0,1,2,4,4,4,5,6,6,7]` might be rotated
at pivot index 5 and become `[4,5,6,6,7,0,1,2,4,4]`.

Given the array `nums` after the rotation and an integer `target`, return true
if `target` is in `nums`, or false if it is not in `nums`.
'''

# Time: O(logn)
# Auxiliary space: O(1)
def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return True

        # left portion is sorted
        if nums[left] < nums[mid]:
            # target is in left sorted portion
            if target >= nums[left] and target < nums[mid]:
                right = mid
            else:
                left = mid + 1
        elif nums[left] == nums[mid]:
            left += 1
        # right portion is sorted
        else:
            # target is in right sorted portion
            if target >= nums[mid + 1] and target <= nums[right]:
                left = mid + 1
            else:
                right = mid

    return False

'''
The previous version of this problem had distinct values, which meant that you
could be certain that the left portion was sorted if nums[left] < nums[mid], or
else the right portion was sorted. In this problem, you may not be able to know
which portion is sorted. For example:

     L     M        R     In this case, nums[left] == nums[mid], which doesn't
    [2, 2, 2, 2, 3, 2]    tell you if the left portion is sorted or not, which
                          means you also don't have any information about
    whether the right portion is sorted or not.

The solution is basically the same as the one for the first version of this
problem, except in the case where nums[left] == nums[mid]. If nums[mid] is not
the target, you know nums[left] is also not the target, so you can shift left
to the right by 1 and continue the search by calculating a new mid. Basically,
this is like doing a linear search on steps when you can't do a binary search.
'''

if __name__ == '__main__':
    nums = [2, 2, 2, 2, 3, 1]
    target = 1
    print(search(nums, target))
