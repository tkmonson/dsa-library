'''
Target Sum (#494)

You are given an integer array `nums` and an integer `target`. You want to
build an expression out of `nums` by adding `+` or `-` before each integer in
`nums` and concatenating all the integers. Return the number of different
expressions you can build that evaluate to `target`.

1 <= len(nums) <= 20
0 <= nums[i] <= 1000
0 <= sum(nums) <= 1000
-1000 <= target <= 1000
'''

from functools import cache

def find_target_sum_ways_memo(nums: list[int], target: int) -> int:
    @cache
    def dfs(i, t):
        if i == len(nums):
            return int(t == target)
        return dfs(i + 1, t + nums[i]) + dfs(i + 1, t - nums[i])

    return dfs(0, 0)


def find_target_sum_ways_memo2(nums: list[int], target: int) -> int:
    memo = {}
    def dfs(i, t):
        if i == len(nums):
            return int(t == target)
        if (i, t) not in memo:
            memo[(i, t)] = dfs(i + 1, t + nums[i]) + dfs(i + 1, t - nums[i])
        return memo[(i, t)]

    return dfs(0, 0)


def find_target_sum_ways_tab_2d(nums: list[int], target: int) -> int:
    S = sum(nums)
    if S < abs(target) or (S + target) % 2:
        return 0

    P = (S + target) // 2
    dp = [[0] * (P + 1) for _ in range(len(nums) + 1)]
    dp[0][0] = 1

    for i in range(1, len(nums) + 1):
        for j in range(P + 1):
            dp[i][j] = dp[i - 1][j]
            if nums[i - 1] <= j:
                dp[i][j] += dp[i - 1][j - nums[i - 1]]

    return dp[-1][P]

'''
For each integer, you have to choose whether to make the integer positive or
negative. Let's redefine this choice to make it look like the knapsack problem:
for each integer, choose whether or not to take the integer as part of the set
of the terms that are to be added in an expression that evaluates to target.

Let P be a set of all the terms that are to be added in an expression that
evaluates to target and let N be a set of the remaining terms (that are to be
subtracted).

sum(P) - sum(N) = target
sum(P) = target + sum(N)
sum(P) + sum(P) = target + sum(N) + sum(P)
2 * sum(P) = target + sum(nums)
    => sum(P) = (target + sum(nums)) / 2

sum(P) is an integer => a valid expression that sums to target exists iff
target + sum(nums) is divisible by 2.

Now we can construct the 2D cache. Let it have len(nums) + 1 rows (to represent
subarrays nums[:0], nums[:1], ... nums[:len(nums)]) and sum(P) + 1 columns (to
represent possible positive term sums 0, 1, ..., sum(P)).

dp[i][j] = the number of ways you can select numbers from nums[:i] such that
           their sum is j

For dp[i][j], you are deciding whether or not to take nums[i - 1].

dp[i][j] = dp[i - 1][j]  (# ways to select from nums[:i - 1] to make j)
         + dp[i - 1][j - nums[i - 1]] (# ways to take nums[i - 1] and also
                                       select from nums[:i - 1] to make j)
'''

def find_target_sum_ways_tab_1d(nums: list[int], target: int) -> int:
    S = sum(nums)
    if S < abs(target) or (S + target) % 2:
        return 0

    P = (S + target) // 2
    dp = [0] * (P + 1)
    dp[0] = 1

    for num in nums:
        next = [0] * (P + 1)
        for j in range(P + 1):
            next[j] = dp[j]
            if num <= j:
                next[j] += dp[j - num]
        dp = next

    return dp[P]

'''
Note that you do need to maintain two rows. A one-row solution is not possible
because by the time you would be evaluating dp[j], dp[j - num] would be
overwritten (in the terms of the solution above, it would be dp[i][j - nums[i]]
instead of dp[i - 1][j - nums[i - 1]]).
'''

if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1]
    target = 3
    print(find_target_sum_ways_tab_1d(nums, target))

'''
In the 2D tabulation solution, instead of redefining the problem, you could
have dp[i][j] = the number of ways to assign symbols to numbers in nums[:i]
such that the expression evaluates to j. j would fall in range(-S, S + 1), but
it could be normalized to range(2 * S + 1), in which case the return value
would be dp[-1][S + target]. This is a cruder solution that will produce a
table that is larger than necessary.

dp[i][j] = dp[i - 1][j - nums[i - 1]] + dp[i - 1][j + nums[i - 1]]
'''

