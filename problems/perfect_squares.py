'''
Perfect Squares (#279)

A perfect square is an integer that is the square of an integer. Given an
integer `n`, return the least number of perfect square numbers that sum to `n`.
'''

from math import inf, isqrt

# Time: O(n * sqrt(n))
# Auxiliary space: O(n)
def num_squares_tab(n: int) -> int:
    dp = [inf] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for sq in range(1, isqrt(i) + 1):
            dp[i] = min(dp[i], 1 + dp[i - sq * sq])

    return dp[n]

'''
You can know there is no greedy solution to this problem by looking at n = 12.
If we were greedy, we would want to reduce 12 as much as possible with each
subtraction of a square. This leads to 3^2 + 1^2 + 1^2 + 1^2, which is 4 terms.
But 12 can also be expressed as 2^2 + 2^2 + 2^2, which is 3 terms. So you need
to explore different paths for each square on each term => dynamic programming.

This is an unbounded knapsack problem, and it is very similar to Coin Change
(#322). Imagine each perfect square less than or equal to n is a coin. On each
turn, you can choose any coin. f(t) = 1 + f(t - coin). You want to take the
coin that minimizes f(t - coin). Build a solution from answers to subproblems.
'''

# Time: O(n * sqrt(n))
# Auxiliary space: O(n)
def num_squares_memo(n: int) -> int:
    dp = {}
    def dfs(i):
        if i == 0:
            return 0
        if i in dp:
            return dp[i]

        res = inf
        for j in range(1, isqrt(i) + 1):
            res = min(res, 1 + dfs(i - j * j))

        dp[i] = res
        return dp[i]

    return dfs(n)


# Time: O(sqrt(n))
# Auxiliary space: O(1)
def num_squares_lagrange(n: int) -> int:
    def is_square(n):
        sq = isqrt(n)
        if sq * sq == n:
            return True
        
    if is_square(n):
        return 1
    
    for i in range(1, isqrt(n) + 1):
        if is_square(n - i * i):
            return 2

    while n % 4 == 0:
        n //= 4
    return 4 if n % 8 == 7 else 3

'''
This very fast solution is based on Langrange's four-square theorem, which
states that every non-negative integer can be represented as the sum of four
perfect squares. An extension of this theorem states that a non-negative
integer can be represented as the sum of three perfect squares if and only if
it is NOT of the form 4^k * (8m + 7), for integers k and m. So the result of
this function can only ever be 1, 2, 3, or 4.
'''

if __name__ == '__main__':
    print(num_squares_tab(48))
