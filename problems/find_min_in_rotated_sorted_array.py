'''
Find Minimum in Rotated Sorted Array (#153)

Given an array of length `n` that has been sorted in ascending order and then
has been rotated between 1 and `n` times, return the minimum element of this
array in O(logn) time. The array contains unique elements.
'''

# Time: O(n)
# Auxiliary space: O(1)
def find_min(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1
    while nums[left] > nums[left - 1]:
        mid = (left + right) // 2
        if nums[left] <= nums[mid]:  # = for the case where left == mid
            left = mid + 1
        else:
            right = mid
    return nums[left]

'''
We are searching for the only element in the array that is less than its
predecessor. This pair of elements (predecessor, target) is the only place in
the array that is not monotonically increasing. If (left < mid) and
(nums[left] < nums[mid]), then nums[left : mid + 1] is monotonically
increasing, and the target must be in the right subarray. If (left < mid) and
(nums[left] > nums[mid]), then a drop in value occured somewhere in the left
subarray and the target must be in there.
'''

if __name__ == '__main__':
    nums = [3, 4, 5, 6, 7, 8, 9, 1, 2]
    nums = [4,5,6,7,0,1,2]
    print(find_min(nums))

