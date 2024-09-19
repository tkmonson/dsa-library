'''
Walls and Gates (#286)

You are given an nxm grid initialized with three possible values:

    1. -1 (a wall)
    2. 0 (a gate)
    3. infinity (an empty room)

Fill each empty room cell with the distance to its nearest gate. If no gate can
be reached, the value should remain infinity. Use the maximum integer value of
2147483647 to represent infinity.
'''

from collections import deque

def walls_and_gates(grid: list[list[int]]) -> None:
    INF = 2147483647
    n, m = len(grid), len(grid[0])
    q = deque()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                q.append((i, j))

    dist = 1
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            for ni, nj in [(i, j + 1), (i - 1, j), (i, j - 1), (i + 1, j)]:
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == INF:
                    grid[ni][nj] = dist
                    q.append((ni, nj))
        dist += 1

'''
This is a multi-source BFS solution. All cells that are a distance of 1 from a
gate are explored before all cells that are a distance of 2 from a gate, and so
on. Because cells are explored in order of increasing distance, there is no
need to update any cells that have already been explored.
'''

if __name__ == '__main__':
    INF = 2147483647
    grid = [
        [INF, INF,  -1,   0],
        [INF,  -1, INF, INF],
        [0,    -1, INF, INF],
        [INF, INF, INF, INF]
    ]
    for row in grid:
        print(row)
    print('')
    walls_and_gates(grid)
    for row in grid:
        print(row)

