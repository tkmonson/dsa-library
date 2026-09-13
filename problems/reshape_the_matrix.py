'''
Reshape the Matrix (#566)

Given an mxn matrix and two integers `r` and `c`, return a new rxc matrix that
contains the elements of the given matrix in the same row-traversing order. If
it is not possible to return a new rxc matrix, return the original matrix.
'''

# Time: O(rc)
# Auxiliary space: O(c)
def reshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    if len(mat) * len(mat[0]) != r * c:
        return mat

    result = []
    i, j = 0, 0

    for _ in range(r):
        row = []
        for _ in range(c):
            row.append(mat[i][j])
            j += 1
            if j == len(mat[0]):
                i += 1
                j = 0
        result.append(row)

    return result


if __name__ == '__main__':
    mat = [[1, 2], [3, 4]]
    r = 1
    c = 4
    print(reshape(mat, r, c))

