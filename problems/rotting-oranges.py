'''
Rotting Oranges (#994)

You are given a 2D array where each cell can have one of three values: 0 (empty
cell), 1 (fresh orange), or 2 (rotten orange). Every minute, any fresh orange
that is 4-directionally adjacent to a rotten orange becomes rotten. Return the
minimum number of minutes that must elapse until no cell has a fresh orange. If
this is impossible, return -1.
'''

from collections import deque

def oranges_rotting(grid: list[list[int]]) -> int:
    R, C = len(grid), len(grid[0])
    num_fresh_oranges = 0
    queue = deque()
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1:
                num_fresh_oranges += 1
            elif grid[r][c] == 2:
                queue.append((r, c))

    count = 0
    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for r, c in [(r, c + 1), (r - 1, c), (r, c - 1), (r + 1, c)]:
                if 0 <= r < R and 0 <= c < C and grid[r][c] == 1:
                    num_fresh_oranges -= 1
                    grid[r][c] = 2
                    queue.append((r, c))
        count += 1

    if count > 0:
        count -= 1

    return count if num_fresh_oranges == 0 else -1


if __name__ == '__main__':
    grid = [[2, 1, 1],
            [1, 1, 0],
            [0, 1, 1]]
    print(oranges_rotting(grid))

