'''
Subarray Sum Equals K (#560)

Given an array of integers and an integer `k`, return the total number of
subarrays whose sum equals `k`.
'''

from collections import defaultdict

def subarray_sum(nums: list[int], k: int) -> int:
    prefix_sum = defaultdict(lambda: 0)
    result = 0

    total = 0
    for i in range(len(nums)):
        total += nums[i]
        if total - k in prefix_sum:
            result += prefix_sum[total - k]
        prefix_sum[total] += 1
    result += prefix_sum[k]

    return result

'''
Finding sums for each subarray => compute prefix sum.

Given some subarray A[:i] that sums to x, we want to consider all subarrays
A[:j] that sum to y such that j < i and x - y = k.

We can store prefix sum data in a map from sum to number of subarrays of that
sum. Thus, when trying to find how many subarrays A[:j] can be "subtracted"
from A[:i] to form a subarray A[j:i] that sums to k, we can query the map with
the key x - k.

However, in order to ensure that map[x - k] returns only the number of
subarrays A[:j] that sum to x - k where j < i, and not the total number of
subarrays in A that sum to x - k, you should count subarrays as the map is
being built. This way, the map only contains information about subarrays that
are smaller than A[:i].

E.g. Let k = 4 and sum(a[:5]) = 6. While there may be some subarray a[:7] that
sums to 2, you don't want to consider it when looking for subarrays that can be
"subtracted" from a[:5] to form a subarray that sums to k.
'''

if __name__ == '__main__':
    nums = [1, 2, 3]
    k = 3
    print(subarray_sum(nums, k))

