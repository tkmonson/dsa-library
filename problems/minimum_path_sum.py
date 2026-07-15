'''
Minimum Path Sum (#64)

Given a `m x n` grid filled with non-negative numbers, find a path from top
left to bottom right, which minimizes the sum of all numbers along its path.
You can only move either down or right at any point in time.

Return the minimum path sum.

1 <= m, n <= 200
'''

from contextlib import suppress

# Time: O(m*n)
# Auxiliary space: O(n)
def min_path_sum(grid: list[list[int]]) -> int:
    R, C = len(grid), len(grid[0])
    dp = [grid[0][0]]
    for _ in range(C - 1):
        dp.append(float('inf'))

    for r in range(R):
        for c in range(1, C):
            dp[c] = grid[r][c] + min(dp[c - 1], dp[c])
        with suppress(IndexError):
            dp[0] += grid[r + 1][0]

    return dp[-1]

'''
mps(r, c) = g[r][c] + min(mps(r - 1, c), mps(r, c - 1))

This means this problem is well-suited for a 1D-tabulation solution.

The grid is guaranteed to be at least 1 x 1. Thus, the best initial state for
the table is [grid[0][0], inf, inf, inf, ...] because it doesn't require
special test cases before the general case.

1 3 1   |   1 * *    1 4 *    1 4 5
1 5 1   |   2 4 5    2 7 5    2 7 6
4 2 1   |   6 7 6    6 8 6    6 8 7  =>  7
'''

if __name__ == '__main__':
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(min_path_sum(grid))
