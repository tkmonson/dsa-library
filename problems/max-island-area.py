'''
Max Area of Island (#695)
PASSES BUT NOT OPTIMIZED FOR TIME, SPACE, OR READABILITY

Given an rxc binary matrix, return the maximum area of an island in the matrix,
where an island is a group of 1s connected 4-directionally and the area of an
island is the number of cells with a value of 1 in the island. If there is no
island in the grid, return 0.
'''

def max_island_area(grid: list[list[int]]) -> int:
    r, c = len(grid), len(grid[0])
    def dfs(i, j):
        if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] != 1:
            return 0
        grid[i][j] = 2
        return 1 + dfs(i, j+1) + dfs(i+1, j) + dfs(i, j-1) + dfs(i-1, j)

    max_area = 0
    for i in range(r):
        for j in range(c):
            max_area = max(max_area, dfs(i, j))

    return max_area

if __name__ == '__main__':
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    ]
    print(max_island_area(grid))

'''
Islands can be explored using either DFS or BFS.

What is found during a DFS is the sum of what is found where you start and what
is found to the left, the right, above, and below.

To avoid exploring the same island twice, it should be marked once explored.
'''

