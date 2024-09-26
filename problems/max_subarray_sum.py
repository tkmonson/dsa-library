'''
Maximum Subarray (#53)

Given an integer array nums, find the subarray (contiguous, non-empty sequence)
with the largest sum and return its sum.
'''

# Time: O(n)
# Auxiliary Space: O(1)
def max_subarray_sum(nums: list[int]) -> int:
    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


# Time: O(n*log(n))
# Auxiliary Space: O(log(n)) (call stack)
def max_subarray_sum_daq(nums: list[int]) -> int:
    def daq(left, right):
        if left == right:
            return nums[left]
        mid = (left + right) // 2
        left_max = daq(left, mid)
        right_max = daq(mid + 1, right)
        cross_max = cross(left, right, mid)

        return max(left_max, right_max, cross_max)

    def cross(left, right, mid):
        left_sum = 0
        left_max = float('-inf')
        for i in range(mid, left - 1, -1):
            left_sum += nums[i]
            left_max = max(left_max, left_sum)

        right_sum = 0
        right_max = float('-inf')
        for i in range(mid + 1, right + 1):
            right_sum += nums[i]
            right_max = max(right_max, right_sum)

        return left_max + right_max

    return daq(0, len(nums) - 1)

'''
This problem has optimal substructure (the maximum subarray of nums can be
calculated from e.g. the maximum subarray of nums[:-1] or from e.g. the maximum
subarrays of nums[:i] and nums[i:] (or some subarray that crosses both)) and
overlapping subproblems (the subarrays are nested).

This problem is solved by Kadane's algorithm, which is similar to a sliding
window solution. Starting from the left, you add elements to a sum; the left
pointer is at 0, and the right pointer increments as elements are added. If the
sum becomes negative after adding nums[i] to it, you know that nums[i + 1] is
greater than the sum of the subarray nums[:i + 2], so it makes sense to get rid
of the elements that came before nums[i + 1] by setting the sum to nums[i + 1]
(in other words, moving the left and right pointer to i + 1). Keep track of the
largest sum that is generated and return it once the whole array has been
traversed.

Because this algorithm calculates the maximum subarray ending at each position
from a related overlapping subproblem (the maximum subarray ending at the
previous position), it is an example of dynamic programming.

   [-2,  1, -3, 4, -1, 2, 1, -5, 4]
-2 |__|
      1 |_|
     -2 |_____|
             4 |_|
             3 |_____|
             5 |________|
             6 |___________|
             1 |_______________|
             5 |__________________|  => the largest sum is 6.

This problem can also be solved by a divide-and-conquer algorithm:
    1. Divide the given array in two halves
    2. Return the maximum of:
        a. the maximum subarray sum of the left half
        b. the maximum subarray sum of the right half
        c. the maximum subarray sum of a subarray that crosses the midpoint
            i. Find the maximum sum of a subarray that ends at the midpoint
            ii. Find the maximum sum of a subarray that starts at mid + 1
            iii. Return their sum
'''

