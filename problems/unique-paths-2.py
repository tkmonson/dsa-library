# How many unique paths are there from the top-left to the bottom-right of a grid that contains obstacles?

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

grid = [
        [0, 0, 1, 0,],
        [1, 0, 1, 0,],
        [0, 0, 0, 0,],
       ]

print(unique_paths2(grid))
