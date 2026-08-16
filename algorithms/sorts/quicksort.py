import random

# Time: O(n^2) (O(nlogn) average)
# Auxiliary space: O(logn) (stack space)
def quicksort(nums: list[int]) -> list[int]:
    def partition(lo, hi):
        pivot = nums[hi]

        follower = lo - 1
        for leader in range(lo, hi):
            if nums[leader] < pivot:
                follower += 1
                nums[follower], nums[leader] = nums[leader], nums[follower]

        nums[follower + 1], nums[hi] = nums[hi], nums[follower + 1]
        return follower + 1

    def _quicksort(lo, hi):
        if lo < hi:
            pivot_index = partition(lo, hi)
            _quicksort(lo, pivot_index - 1)
            _quicksort(pivot_index + 1, hi)

    _quicksort(0, len(nums) - 1)
    return nums

'''
Simplest version of Quicksort, using Lomuto's partition scheme:

1. Choose the last element as the pivot
2. Follower always points to last element less than pivot,
   Leader looks for next element less than pivot
   When leader finds one, follower increments, leader swaps with follower
   (follower is pointing momentarily to an element leader already checked)
3. Continue until leader traverses whole array except pivot
4. Swap pivot with follower + 1 (the first element greater than pivot)
5. Pivot is now sorted; recur on left and right subarrays
'''

# Time: O(n^2) (O(nlogn) average)
# Auxiliary space: O(n^2) (O(nlogn) average)
def quicksort_lazy(nums: list[int]) -> list[int]:
    def qsort(nums):
        if not nums:
            return nums
        pivot = random.choice(nums)
        left = [x for x in nums if x < pivot]
        equal = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]
        
        return qsort(left) + equal + qsort(right)
        
    return qsort(nums)

'''
This lazy way of writing Quicksort is notable simply because of how compact and
straightforward it is, but it is very space-inefficient.
'''
