'''
Search in Rotated Sorted Array (#33)

An initially sorted array of distinct integers is possibly rotated at an
unknown pivot index. Given the array `nums` after the possible rotation and an
integer `target`, return the index of `target` if it is in `nums` or -1 if it
is not in `nums`. You must write an algorithm that runs in O(logn) time.
'''

# Time: O(logn)
# Auxiliary space: O(1)
def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid

        # left portion is sorted
        if nums[left] <= nums[mid]:  # = only if left == mid
            # target is in left sorted portion
            if target >= nums[left] and target < nums[mid]:
                right = mid
            else:
                left = mid + 1
        # right portion is sorted
        else:
            # target is in right sorted portion
            if target >= nums[mid + 1] and target <= nums[right]:
                left = mid + 1
            else:
                right = mid

    return -1


if __name__ == '__main__':
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 0
    print(search(nums, target))

'''
Since the algorithm must be a search that runs in O(logn), it is likely a
binary search. How would you choose the side on which you would continue your
search? Consider a left side nums[left: pivot + 1] and a right side
nums[pivot + 1: right + 1]. Since there is at most one contiguous pair of
elements in the array that is not ascending, at least one of these sides must
be strictly ascending (that is, the leftmost element of this side is less than
the rightmost element (or equal to in the case where the side contains one
element)). If the target could exist on that strictly ascending side, we
continue the search there. Otherwise, we continue the search on the other side.
'''
