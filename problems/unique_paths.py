'''
Unique Paths (#62)

There is a robot on an mxn grid. The robot starts in the top-left corner and
tries to move to the bottom-right corner, but it can only move down and to the
right. Return the number of unique paths that the robot can take to the
bottom-right corner.
'''

from math import factorial

# Time: O(m * n)
# Auxiliary space: O(m * n) + O(m + n) (memo + stack)
def unique_paths(m, n):
    dp = {}
    def dfs(r, c):
        if r == m - 1 or c == n - 1:
            return 1
        if (r, c) not in dp:
            dp[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
        return dp[(r, c)]
    return dfs(0, 0)

'''
Top-down, recursive solution with memoization.
'''

# Time: O(m * n)
# Auxiliary space: O(m * n)
def unique_paths2(m, n):
    dp = [[1 for _ in range(n)] for _ in range(m)]
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r-1][c] + dp[r][c-1]
    return dp[-1][-1]

'''
A naive approach would be to use recursion to explore all possible paths to the
bottom-right corner. The problem with this approach is that the paths overlap,
so exploring each one individually leads to redundant computation.

Because you can only enter a cell from the top or left, we know that any path
from the start to the end that passes through some cell must also pass through
either that cell's top or left neighbor. Thus, the number of paths from the
start to some cell is equal to the number of paths from the start to that
cell's top neighbor plus the number of paths from the start to that cell's left
neighbor.
'''

# Time: O(m * n)
# Auxiliary space: O(n)
def unique_paths3(m, n):
    dp = [1] * n
    for _ in range(1, m):
        for c in range(1, n):
            dp[c] += dp[c - 1]
    return dp[-1]

'''
A space-optimized version of the same algorithm. The new dp[c] is equal to the
sum of the old dp[c] (top neighbor) and dp[c - 1] (left neighbor).
'''

# Time: O(m + n)
# Auxiliary space: O(1)
def unique_paths4(m, n):
    k = min(m - 1, n - 1)
    n = m + n - 2
    return factorial(n) // (factorial(k) * factorial(n - k))

'''
A solution to this problem can also be expressed as a binomial coefficient
(nCk, "n choose k"). Given any m and n, it will take m + n - 2 moves to get
from the start to the end. m - 1 of these moves must be down, and n - 1 of
these moves must be right. Thus, we can rephrase this problem as "given
m + n - 2 moves, in how many different ways can you choose m - 1 of these moves
to be down?". nCk = n! / (k!(n - k)!).
'''

# Time: O(min(m, n))
# Auxiliary space: O(1)
def unique_paths5(m, n):
    k = min(m - 1, n - 1)
    n = m + n - 2
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result

'''
A more efficient version of the binomial coefficient solution that uses the
multiplicative formula nCk = n * (n - 1) * ... * (n - k + 1) / k!. This works
better for very large n and k because it avoids computing n! and (n - k)!.
Dividing at each step keeps the number small.
'''

if __name__ == '__main__':
    m = 3
    n = 7
    print(unique_paths(m, n))
