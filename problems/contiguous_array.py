'''
Contiguous Array (#525)

Given a binary array, return the maximum length of a contiguous subarray with
an equal number of 0s and 1s.
'''

from collections import Counter

def find_max_length(nums: list[int]) -> int:
    total = 0
    prefix_sum = {0: -1}
    max_length = 0

    for i, v in enumerate(nums):
        total += 1 if v else -1
        if total in prefix_sum:
            max_length = max(max_length, i - prefix_sum[total]
        else:
            prefix_sum[total] = i

    return max_length

'''
Let each subarray have a total = count(1) - count(0). We are looking for the
longest subarray with a total of 0.

Computing the prefix sum of the given array (where each 0 subtracts 1) will
give you the total for each subarray starting at i = 0. By subtraction, these
subarray totals can be used to compute the total of any subarray.

     [* * * * * * *]
(A)  |_____|        <-- if this subarray has total = z
(B)  |___________|  <-- and this subarray has total = z
(C)        |_____|  <-- then this subarray has total = 0

To maximize the length of C, minimize the length of A and maximize the length
of B. That is, while scanning the array to create its prefix sum, store the
index of the first subarray (A) with total of z. If some larger subarray (B)
with a total of z is found later in the scan, then the length of their
difference (C) can be computed.
'''
