'''
Rotate Image (#48)

Given an nxn 2D array `matrix` representing an image, rotate the image
clockwise by 90 degrees and do so in-place.
'''

# Time: O(n^2)
# Auxiliary space: O(1)
def rotate(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - 1 - i):
            ti, tj = i, j
            for _ in range(4):
                i, j = j, n - 1 - i
                matrix[i][j], matrix[ti][tj] = matrix[ti][tj], matrix[i][j]

'''
Each cell (i, j) must be moved to (j, n - 1 - i). Think about the matrix in
terms of "borders" that decrease in size from the outside to the inside. If you
rotate the elements in these borders (side_length - 1) times, the whole image
will be rotated. For example, if cells 1, 2, 3, and 4 in each matrix below are
rotated, the whole image will be rotated.

1 x x 2    x 1 x x    x x 1 x    x x x x
x x x x    x x x 2    4 x x x    x 1 2 x
x x x x    4 x x x    x x x 2    x 4 3 x
4 x x 3    x x 3 x    x 3 x x    x x x x

This can be done by using the 1 cell as the "temp" value: swap(1, 2),
swap(1, 3), swap(1, 4). For each border of side_length > 1, this process should
be done for each element in the top side of the border, except the last one.

1 1 1 2
4 1 2 2
4 4 3 2
4 3 3 3
'''

# Time: O(n^2)
# Auxiliary space: O(1)
def rotate2(matrix: list[list[int]]) -> list[list[int]]:
    n = len(matrix)

    # Transpose
    for i in range(1, n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse columns
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]


if __name__ == '__main__':
    a = [[5, 1, 9, 11],
         [2, 4, 8, 10],
         [13, 3, 6, 7],
         [15, 14, 12, 16]]
    rotate2(a)
    for row in a:
        print(row)

