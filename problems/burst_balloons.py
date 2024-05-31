'''
Burst Balloons (#312)

You are given `n` balloons, indexed from `0` to `n - 1`. Each balloon is
painted with a number on it, represented by an array `nums`. You are asked to
burst all the balloons.

If you burst the `ith` balloon, you will get
`nums[i - 1] * nums[i] * nums[i + 1]` coins. If `i - 1` or `i + 1` goes out of
bounds, treat it as if there is a balloon with a `1` painted on it.

Return the maximum coins you can collect by bursting the balloons optimally.
'''

from functools import cache

# Time: O(n^3)
# Auxiliary space: O(n^2)
def max_coins(nums: list[int]) -> int:
    nums = [1] + nums + [1]

    @cache
    def dfs(L, R):
        if L > R:
            return 0

        max_c = 0
        for i in range(L, R + 1):
            coins = nums[L - 1] * nums[i] * nums[R + 1]
            coins += dfs(L, i - 1) + dfs(i + 1, R)
            max_c = max(max_c, coins)

        return max_c

    return dfs(1, len(nums) - 2)

'''
Naive solution: backtracking. Choose a balloon to pop first, pop it, and move
on to choose another balloon to pop. Unpop balloons on the way back, choose a
different balloon to pop first. n balloons at layer 1, n - 1 balloons at layer
2, ..., 1 balloon at layer n => O(n!).

[3, 2, 5, 8]  =>  [3, 2, x, 8]  =>  [3, 2]  [8]

You might think that after choosing a balloon to pop (5), you would be able to
recur on the adjacent subproblems ([3, 2], [8]), but these problems are
interdependent. For example, after popping 5, popping 2 would give you
3 * 2 * 8 coins, but 8 is not contained in [3, 2], so you wouldn't know to
include it in the product.

Key insight: choose a balloon to pop last. Consider S := A[L : R + 1], a
subarray of an array A, delimited by inclusive left and right pointers, L and
R. Let A[i] be the balloon in S to be popped last (L <= i <= R).

              L       i   R
[ x | x | x { x | x | x | x } x | x ]
            {   Y   }   { Z }

If A[i] is popped last, that means that every balloon in Y := A[L:i] and
Z := A[i + 1 : R + 1] will be popped before A[i]. That means that the
subproblems Y and Z are independent of each other because there will always be
an element between them. Thus, we can recur on those subproblems. For example,
given [3, 2, 5, 8], if we pop 5 last, then popping 2 will never produce a
product including 8 and popping 8 will never produce a product 2. The
subproblems are independent.

Thus, the maximum number of coins you can get from S is equal to:
    A[L - 1] * A[i] * A[R + 1]
  + the maximum number of coins you can get from Y
  + the maximum number of coins you can get from Z.

For every balloon in A, we will consider the case where it is popped last. This
is O(n). For each of these cases, we will consider every subarray in Y and
every subarray in Z. This is O(n^2). Thus, the time complexity is O(n^3).
'''

# Time: O(n^3)
# Auxiliary space: O(n^2)
def max_coins_tabu_inc(nums: list[int]) -> int:
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    for i in range(n - 2, 0, -1):
        for j in range(i, n - 1):
            for k in range(i, j + 1):
                coins = nums[i - 1] * nums[k] * nums[j + 1]
                coins += dp[i][k - 1] + dp[k + 1][j]
                dp[i][j] = max(dp[i][j], coins)

    return dp[1][n - 2]

'''
We need to consider all subarrays and, for each subarray, we need to consider
each element in the subarray as the last balloon to be popped. Let
S := A[L : R + 1], let A[i] be the last balloon in S to be popped, and let
Y := A[L:i] and Z := A[i + 1 : R + 1]. When computing the maximum number of
coins we can get from S when A[i] is popped last, we would like to have the
results for max_coins(Y) and max_coins(Z) cached, where max_coins(p) is the
maximum number of coins we can get from p, regardless of which balloon in p is
popped last. We can do this by computing results for subarrays in the following
manner (* denotes the element that is to be popped last).

  [ x | x | x ]

          | * |
      | * |
      | *     |
      |     * |
  | * |
  | *     |
  |     * |
  | *         |
  |     *     |
  |         * |

This solution uses inclusive delimiters, similar to the memoization solution
above.
'''

# Time: O(n^3)
# Auxiliary space: O(n^2)
def max_coins_tabu_exc(nums: list[int]) -> int:
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    for i in range(n - 3, -1, -1):
        for j in range(i + 2, n):
            for k in range(i + 1, j):
                dp[i][j] = max(
                    dp[i][j],
                    dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j]
                )

    return dp[0][n - 1]

'''
Similar to the above solution but using exclusive delimiters and consolidating
calculations into a single statement. This solution runs faster because no index
arithmetic needs to be performed within the third loop.
'''

if __name__ == '__main__':
    nums = [3, 2, 5, 8]
    print(max_coins_tabu_exc(nums))

