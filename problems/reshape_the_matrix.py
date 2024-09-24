'''
Reshape the Matrix (#566)

Given an mxn matrix and two integers `r` and `c`, return a new rxc matrix that
contains the elements of the given matrix in the same row-traversing order. If
it is not possible to return a new rxc matrix, return the original matrix.
'''

# Time: O(mn)
# Auxiliary space: O(mn)
def reshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    if len(mat) * len(mat[0]) != r * c:
        return mat

    mat2 = [[0 for _ in range(c)] for _ in range(r)]
    i, j = 0, 0

    for i2 in range(r):
        for j2 in range(c):
            mat2[i2][j2] = mat[i][j]
            j += 1
            if j == len(mat[0]):
                i += 1
                j = 0

    return mat2


if __name__ == '__main__':
    mat = [[1, 2], [3, 4]]
    r = 1
    c = 4
    print(reshape(mat, r, c))

