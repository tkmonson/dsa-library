# How many unique paths are there from the top-left to the bottom-right of a grid?

# m = columns, n = rows

def unique_paths(m, n):
    if m == 0 or n == 0:
        return 0

    paths = [[0 for c in range(m)] for r in range(n)]

    for c in range(m):
        paths[0][c] = 1

    for r in range(n):
        paths[r][0] = 1

    for r in range(1, n):
        for c in range(1, m):
            paths[r][c] = paths[r-1][c] + paths[r][c-1]

    return paths[-1][-1]

print(unique_paths(4,3))
