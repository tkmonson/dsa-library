'''
House Robber (#198)

There is a row of houses along a street, each with a certain amount of money
stashed. Adjacent houses have a security system connected that will contact the
police if both houses are robbed. Given an array representing the amount of
money in each house, return the maximum amount of money you can rob without
alerting the police.
'''

# Time: O(n)
# Auxiliary space: O(1)
def rob(nums: list[int]):
    prev1, prev2 = 0, 0
    for num in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + num)
    return prev1


# Time: O(n)
# Auxiliary space: O(1)
def rob_tabu(nums: list[int]):
    dp = [-1] * (len(nums) + 1)
    dp[0] = 0
    dp[1] = nums[0]
    for i in range(1, len(nums)):
        dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])
    return dp[len(nums)]


# Time: O(n)
# Auxiliary space: O(n)
def rob_memo(nums: list[int]):
    dp = [-1] * len(nums)

    def _rob(nums, i):
        if i < 0:
            return 0
        if dp[i] >= 0:
            return dp[i]
        dp[i] = max(_rob(nums, i - 1), _rob(nums, i - 2) + nums[i])
        return dp[i]

    return _rob(nums, len(nums) - 1)


if __name__ == '__main__':
    nums = [2, 7, 9, 3, 1]
    print(rob(nums))

'''
First naive thought: you either want [Y N Y N Y N] or [N Y N Y N Y].
Second revised thought: you actually may want to skip two houses in a row, like
[N Y N N Y N], as a way of switching to the other alternating sequence. But you
will never want to skip three in a row.

At each house i, the robber can rob or not rob. If they rob, that means they
cannot rob house i-1, but they can rob the maximum amount of money from houses
0 through i-2. If they don't rob, they can rob the maximum amount of money from
houses 0 through i-1. Thus, f(i) = max(f(i - 1), f(i - 2) + nums[i]).

Because computing f(i) can be expressed in terms of f(i - 1) and f(i - 2), this
problem has optimal substructure (i.e. its optimal solution can be constructed
from optimal solutions to its subproblems).

Because computing f(i) involves computing both f(i - 1) and f(i - 2) before
comparing their results and because computing f(i - 1) requires computing
f(i - 2), this problem also has overlapping subproblems (i.e. it can be broken
down into subproblems whose results are recomputed/reused multiple times).

f(i) = f(i - i)  f(i - 2)
         |         |
         |         f(i - 3)  f(i - 4)
         |           |
         |           f(i - 4)  f(i - 5)
         |
         f(i - 2)  f(i - 3)
           |         |
           |         f(i - 4)  f(i - 5)
           |
           f(i - 3)  f(i - 4)

A problem with optimal substructure and overlapping subproblems is a good
candidate for dynamic programming.

Let dp[i] be the maximum amount of money that can be robbed from houses
nums[:i].

dp[0]: [] => 0
dp[1]: [x] => max(x) = x
dp[2]: [x, y] => max(x, y)
dp[3]: [x, y, z] => max(y, x + z) = max(dp[2], dp[1] + nums[2])
dp[4]: [x, y, z, a] => max(x + z, max(x, y) + a) = max(dp[3], dp[2] + nums[3])
dp[5]: [x, y, z, a, b] => max(max(x, y) + a, max(y, x + z) + b)
...                     = max(dp[4], dp[3] + nums[4])
dp[i + 1]: [...] => max(dp[i], dp[i - 1] + nums[i])
'''

