'''
Longest Increasing Path (#329)

Given an mxn matrix of integers, return the length of the longest increasing
path in the matrix. You can only move 4-directionally, not diagonally or
outside of the boundary.
'''

from functools import cache

def longest_increasing_path(matrix: list[list[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    d = ((1, 0), (-1, 0), (0, 1), (0, -1))
    result = 0

    @cache
    def dfs(i, j):
        ans = 0
        for di, dj in d:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                ans = max(ans, dfs(ni, nj))
        return ans + 1

    for i in range(m):
        for j in range(n):
            if (path_length := dfs(i, j)) > result:
                result = path_length

    return result

'''
Small mistake to avoid: I tried to pass the current length of a growing path as
a third argument of the DFS call. That made the caching much less efficient
(you want to cache values based on (i, j), not (i, j, curr)). So you need to
instead increment the path length as you are backing out of the recursion.

The way the DFS is written above is more concise, but this implementation is
slightly faster (12 comparisons per call versus 24):

@cache
def dfs(i, j):
    ans = 0
    if i > 0 and matrix[i - 1][j] > matrix[i][j]:
        ans = max(ans, dfs(i - 1, j))
    if j > 0 and matrix[i][j - 1] > matrix[i][j]:
        ans = max(ans, dfs(i, j - 1))
    if i < m - 1 and matrix[i + 1][j] > matrix[i][j]:
        ans = max(ans, dfs(i + 1, j))
    if j < n - 1 and matrix[i][j + 1] > matrix[i][j]:
        ans = max(ans, dfs(i, j + 1))
    return 1 + ans
'''

if __name__ == '__main__':
    matrix = [[9, 9, 9],
              [6, 6, 8],
              [2, 1, 1]]
    print(longest_increasing_path(matrix))

