'''
Unique Paths II (#63)

You are given an `m x n` integer array `grid`. There is a robot initially
located at the top-left corner. The robot tries to move to the bottom-right
corner. The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in `grid`. A path that
the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the
bottom-right corner.
'''

def unique_paths2(grid):
    if (grid is None) or (len(grid) == 0) or (len(grid[0]) == 0):
        return 0

    height = len(grid)
    width = len(grid[0])
    paths = [[0 for c in range(width)] for r in range(height)]

    for c in range(width):
        if grid[0][c] != 1:
            paths[0][c] = 1
        else:
            break

    for r in range(height):
        if grid[r][0] != 1:
            paths[r][0] = 1
        else:
            break

    for r in range(1, height):
        for c in range(1, width):
            if grid[r][c] != 1:
                paths[r][c] = paths[r-1][c] + paths[r][c-1]

    return paths[-1][-1]

'''
The number of possible paths to the bottom-right corner can be found by finding
the number of possible paths to other cells closer to the start.

There is only one path to any cell in the first row or column. The number of
paths to any other cell C is the sum of paths to cells from which the robot
can enter C (that is, the cells above and to the left of C).

A cell with an obstacle always has zero paths to it.

1    1    1    1
1    2    3    4
1    3    6   10
1    4   10   20
'''

if __name__ == '__main__':
    grid = [
            [0, 0, 1, 0,],
            [1, 0, 1, 0,],
            [0, 0, 0, 0,],
        ]

    print(unique_paths2(grid))
