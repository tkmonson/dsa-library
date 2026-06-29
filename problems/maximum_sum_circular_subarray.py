'''
Maximum Sum Circular Subarray (#918)

Given a circular integer array nums of length n, return the maximum possible
sum of a non-empty subarray of nums.
'''

# Time: O(n)
# Auxiliary space: O(1)
def max_subarray_sum_circular(nums: list[int]) -> int:
    max_sum = min_sum = curr_max = curr_min = total = nums[0]
    
    for i in range(1, len(nums)):
        curr_max = max(curr_max + nums[i], nums[i])
        max_sum = max(max_sum, curr_max)
        
        curr_min = min(curr_min + nums[i], nums[i])
        min_sum = min(min_sum, curr_min)
        
        total += nums[i]
    
    circular_sum = total - min_sum
    
    # All elements are negative, return largest element
    if circular_sum == 0:
        return max_sum
    
    return max(max_sum, circular_sum)

'''
For a regular array, use Kadane's algorithm to find the maximum subarray sum:
    * max_sum(nums[:i+1]) = max(max_sum(nums[:i]) + nums[i], nums[i])
      (If sum(a[i:j]) < 0, consider a[j:j+1] instead.)

For a circular array, the maximum subarray can either be "normal"
(non-wrapping) or "special" (wrapping). If it is special, that means there is
some non-wrapping subarray that is not part of the special subarray. Maximizing
the sum of the special subarray can be thought of as minimizing the sum of this
non-wrapping subarray.

Since we don't know if the maximum subarray is normal or special, calculate the
maximum sum of a normal subarray and the maximum sum of a special subarray and
return the greater of the two.

1. For normal, use Kadane's algorithm.
2. For special, modify Kadane's algorithm to find the minimum subarray sum and
   subtract it from the total sum.
'''

if __name__ == '__main__':
    nums = [1,-2,3,-2]
    print(max_subarray_sum_circular(nums))

'''
Another way to approach this problem is to recognize that if the maximum
subarray wraps around, it is composed of a prefix subarray and a suffix
subarray. You need to find the combination of non-overlapping prefix and suffix
subarrays that yields the maximum sum.

Let right_max[i] be the maximum sum of a subarray starting at index i or
greater: right_max[i] = max(suffix_sum[i], suffix_sum[i+1], ...).

Once you have right_max, you can accumulate the prefix sum and, at each index
i, get right_max[i+1], the maximum sum of a suffix subarray that does not overlap
with the current prefix subarray.
'''
