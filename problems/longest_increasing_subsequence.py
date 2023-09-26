'''
Longest Increasing Subsequence (#300)

Given an integer array, return the length of the longest strictly increasing
subsequence (LIS).
'''

from bisect import bisect_left

# Time: O(nlogn)
# Auxiliary space: O(n)
def length_of_lis(nums: list[int]) -> int:
    sub = [nums[0]]
    for num in nums:
        if num > sub[-1]:
            sub.append(num)
        else:
            sub[bisect_left(sub, num)] = num

    return len(sub)

'''
Greedily construct a strictly increasing subsequence (if you can take an
element, take it). If the next element is not greater than the last element in
the subsequence, it cannot be added to that subsequence. But the LIS may
actually include that element, so you need to store an alternate subsequence by
"backtracking" the current subsequence until the element can be added to it.
Find how far you need to backtrack using binary search.

nums = [2, 6, 8, 3, 4, 5, 9, 1]

[2]
[2, 6]
[2, 6, 8]
[2, 6, 8],     [2, 3]
[2, 6, 8],     [2, 3, 4]
[2, 6, 8],     [2, 3, 4, 5]
[2, 6, 8, 9],  [2, 3, 4, 5, 9]
[2, 6, 8, 9],  [2, 3, 4, 5, 9],  [1]  =>  5

Storing multiple subsequences would require a lot of space. However, because we
only need the last element of the longest subsequence to know whether we can
append a new element and increase the max length so far, we can store alternate
subsequences within the original subsequence by overwriting values.

[2]    [2, 6]    [2, 6, 8]    [2, 3, 8]    [2, 3, 4]    [2, 3, 4, 5]
[2, 3, 4, 5, 9]    [1, 3, 4, 5, 9]  =>  5

You can visualize this with cards. If the next card is greater, deal it to the
right of the rightmost card. Otherwise, stack it on top of the smallest card
that is still greater than the card being dealt. Only the topmost cards count
for comparisons, but this is essentially a representation of overlapping linked
lists.
               _________
              |         |
    2 <- 6 <- 8    5 <- 9
     \__           |
        \          |
    1    3 <- 4 <--
'''

# Time: O(n^2)
# Auxiliary space: O(n)
def length_of_lis_dp(nums: list[int]) -> int:
    n = len(nums)
    dp = [1] * n
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], 1 + dp[j])
    return max(dp)

'''
You can either take or not take each element in nums. There must be some first
element in the longest increasing subsequence of nums. If this is the ith
element in nums, then the LIS of nums is equal to the LIS of nums[i:], assuming
that the ith element is taken.

Let lis[i] be the LIS of nums[i:], where nums[i] is the first element included
in the subsequence. There are n subsequences in lis, the longest of which is
the LIS of nums.

Consider lis[n - 1]; it is [nums[n - 1]].
Consider lis[n - 2]; it could be [nums[n - 2]] or
                     it could be [nums[n - 2]] + lis[n - 1]
                         (as long as nums[n - 2] < nums[n - 1]).
Consider lis[n - 3]; it could be [nums[n - 3]] or
                     it could be [nums[n - 3]] + lis[n - 2]
                         (as long as nums[n - 3] < nums[n - 2]) or
                     it could be [nums[n - 3]] + lis[n - 1]
                         (as long as nums[n - 3] < nums[n - 1]).

Let dp[i] be the length of lis[i]. To generalize:
    dp[i] = 1 + max([dp[j] * (nums[i] < nums[j]) for j in range(i + 1, n)]).
'''

if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 4, 101, 18]
    print(length_of_lis_bs(nums))

