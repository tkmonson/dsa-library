'''
01 Matrix (#542)

Given an rxc binary matrix, return the distance to the nearest 0 for each cell.
The distance between two adjacent cells is 1.
'''

from collections import deque

def update_matrix_naive(mat: list[list[int]]) -> list[list[int]]:
    def bfs(i, j):
        queue = deque([(i, j, 0)])
        visited = set()
        while queue:
            i, j, d = queue.popleft()
            visited.add((i, j))
            if mat[i][j] == 0:
                return d
            for i, j in [(i, j + 1), (i - 1, j), (i, j - 1), (i + 1, j)]:
                if (i >= 0 and i < r and j >= 0 and j < c and
                    (i, j) not in visited):
                    queue.append((i, j, d + 1))

    r, c = len(mat), len(mat[0])
    ans = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            ans[i][j] = bfs(i, j)
    return ans

'''
This naive solution traverses the matrix and performs a BFS at every cell,
resetting the visited set each time.
'''

def update_matrix(mat: list[list[int]]) -> list[list[int]]:
    r, c = len(mat), len(mat[0])
    ans = [[-1 for _ in range(c)] for _ in range(r)]
    queue = deque()

    for i in range(r):
        for j in range(c):
            if mat[i][j] == 0:
                queue.append((i, j, 0))
                ans[i][j] = 0

    while queue:
        i, j, d = queue.popleft()
        for i, j in [(i, j + 1), (i - 1, j), (i, j - 1), (i + 1, j)]:
            if i >= 0 and i < r and j >= 0 and j < c and ans[i][j] == -1:
                queue.append((i, j, d + 1))
                ans[i][j] = d + 1

    return ans

'''
This solution performs a BFS at all zero cells, expanding outward at the same
rate. So all cells at a distance of 1 from a 0 are explored before cells at a
distance of 2 from a 0 are explored. Values in the distance matrix are updated
when the cell is added to the queue, which ensures that cells are not added to
the queue twice and distances are not overwritten.
'''

def update_matrix2(mat: list[list[int]]) -> list[list[int]]:
    r, c = len(mat), len(mat[0])

    for i in range(r):
        for j in range(c):
            if mat[i][j] != 0:
                top = mat[i - 1][j] if i > 0 else float('inf')
                left = mat[i][j - 1] if j > 0 else float('inf')
                mat[i][j] = min(top, left) + 1

    for i in reversed(range(r)):
        for j in reversed(range(c)):
            if mat[i][j] != 0:
                bot = mat[i + 1][j] if i < r - 1 else float('inf')
                right = mat[i][j + 1] if j < c - 1 else float('inf')
                mat[i][j] = min(mat[i][j], min(bot, right) + 1)

    return mat

'''
This solution is in-place. Imagine that you are looking for the distance to the
nearest 0 for each cell if you can only move up and left. The distance for each
1 cell would be equal to min(dist(top), dist(left)) + 1. Then imagine that you
can only move down or right. The distance for each 1 cell would be equal to
min(dist(bot), dist(right)) + 1. The greater of these expressions is the true
distance to the nearest 0. This solution is possible because 0s in the given
matrix and 0s in the result matrix are in the same place, so that information
is never destroyed even if you are overwriting all 1 values in the given
matrix.
'''

if __name__ == '__main__':
    mat = [[0, 0, 0],
           [0, 1, 0],
           [1, 1, 1]]
    print(update_matrix(mat))

