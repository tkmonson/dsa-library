'''
Number of Islands (#200)

Given an mxn binary grid where 0s represent water and 1s represent land, return
the number of islands. An island is surrounded by water and is formed by
connecting adjacent lands horizontally and vertically. All four edges of the
grid are surrounded by water.
'''

def num_islands(grid: list[list[str]]) -> int:
    def dfs(r, c):
        grid[r][c] = '2'
        if c < C - 1 and grid[r][c + 1] == '1':
            dfs(r, c + 1)
        if r > 0 and grid[r - 1][c] == '1':
            dfs(r - 1, c)
        if c > 0 and grid[r][c - 1] == '1':
            dfs(r, c - 1)
        if r < R - 1 and grid[r + 1][c] == '1':
            dfs(r + 1, c)

    count = 0
    R, C = len(grid), len(grid[0])
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1

    return count


if __name__ == '__main__':
    grid = [['1','1','0','0','0'],
            ['1','1','0','0','0'],
            ['0','0','1','0','0'],
            ['0','0','0','1','1']]
    print(num_islands(grid))

