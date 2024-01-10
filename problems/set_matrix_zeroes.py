'''
Set Matrix Zeroes (#73)

Given an mxn integer matrix, if an element is 0, set its entire row and column
to 0s. The solution should be in-place.
'''

# Time: O(mn)
# Auxiliary space: O(1)
def set_zeroes(matrix: list[list[int]]) -> None:
    m, n = len(matrix), len(matrix[0])

    # Determine if the 0th row and/or 0th col need to be zeroed
    row0 = 0 in matrix[0]
    col0 = False
    for i in range(m):
        if matrix[i][0] == 0:
            col0 = True
            break

    # Find which rows/cols need to be zeroed
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Zero the rows
    for i in range(1, m):
        if matrix[i][0] == 0:
            for j in range(1, n):
                matrix[i][j] = 0

    # Zero the cols
    for j in range(1, n):
        if matrix[0][j] == 0:
            for i in range(1, m):
                matrix[i][j] = 0

    # Zero the 0th row
    if row0:
        for j in range(n):
            matrix[0][j] = 0

    # Zero the 0th col
    if col0:
        for i in range(m):
            matrix[i][0] = 0

'''
Similar to the solution below, but uses the 0th row and 0th column to store
information about which rows and columns to zero out instead of auxiliary
arrays.
'''

# Time: O(mn)
# Auxiliary space: O(m + n)
def set_zeroes2(matrix: list[list[int]]) -> None:
    m, n = len(matrix), len(matrix[0])
    rows_to_0, cols_to_0 = [False] * m, [False] * n

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows_to_0[i] = True
                cols_to_0[j] = True

    for i in range(m):
        if rows_to_0[i]:
            for j in range(n):
                matrix[i][j] = 0

    for j in range(n):
        if cols_to_0[j]:
            for i in range(m):
                matrix[i][j] = 0


# Time: O(mn)
# Auxiliary space: O(1)
def set_zeroes3(matrix: list[list[int]]) -> None:
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                for i2 in range(m):
                    if matrix[i2][j] != 0:
                        matrix[i2][j] = '*'
                for j2 in range(n):
                    if matrix[i][j2] != 0:
                        matrix[i][j2] = '*'

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '*':
                matrix[i][j] = 0

'''
This solution could be considered "cheating" because it relies on the fact that
Python is a dynamically-typed language.
'''

if __name__ == '__main__':
    matrix = [[0, 1, 2, 0],
              [3, 4, 5, 2],
              [1, 3, 1, 5]]
    set_zeroes2(matrix)
    print(matrix)

