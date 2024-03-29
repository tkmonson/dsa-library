'''
Maximum Product Subarray (#152)

Given an array of integers, find a subarray that has the largest product and
return that product.

E.g.
    [-6, 4, -5, 8, -10, 0, 8]  =>  1600 (subarray is [4, -5, 8, -10])
    [40, 0, -20, -10]  =>  200 (subarray is [-20, -10])
'''

# Time: O(n)
# Auxiliary space: O(1)
def max_subarray_product(nums: list[int]) -> int:
    max_ending, min_ending, curr_max = (nums[0],) * 3
    for i in range(1, len(nums)):
        a, b = nums[i] * max_ending, nums[i] * min_ending
        max_ending = max(nums[i], a, b)
        min_ending = min(nums[i], a, b)
        curr_max = max(curr_max, max_ending)
    return curr_max

'''
The naive O(n^2) solution is to calculate the product of every subarray. The
better solution is to realize that the product of a subarray is equal to its
last element times the product of its previous elements. And the maximum
product of a subarray ending at index i is equal to A[i] times either the
minimum or maximum product of a subarray ending at i - 1, depending on whether
A[i] is negative or positive (or it is just A[i], when min_or_max(i - 1) * A[i]
< A[i]). At each index i, we collect the minimum and maximum product of
subarrays ending at i, and we use them to inform answers at higher indices.
Finally, we return the maximum subarray product for the whole array.
'''

if __name__ == "__main__":
    arr = [-6, 4, -5, 8, -10, 0, 8]
    print(max_subarray_product(arr))

