# Input: matrix of ints (mxn)
# Output: array in spiral order

# Example:

# [[1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]]

# [1,2,3,6,9,8,7,4,5]

# Time: O(mn)
# Space: O(mn)

import numpy as np

def spiral_array(matrix):
    result = []
    if not matrix:
        return result

    m, n = len(matrix), len(matrix[0])
    k = 0
    r, c = 0, -1

    while(True):
        right = n - k*2
        down = m - 1 - k*2
        left = right - 1
        up = down - 1

        if right == 0: break
        for _ in range(right):
            c += 1
            result.append(matrix[r][c])

        if down == 0: break
        for _ in range(down):
            r += 1
            result.append(matrix[r][c])

        if left == 0: break
        for _ in range(left):
            c -= 1
            result.append(matrix[r][c])

        if up == 0: break
        for _ in range(up):
            r -= 1
            result.append(matrix[r][c])

        k += 1

    return result

arr = [[1,2,3],[4,5,6],[7,8,9]]
print(arr)
print(spiral_array(arr))

# Old solution method. Involves boundary pointers that need to be updated.
# Does not work for mx1 and 1xn matricies.

def spiral_array(matrix):
    result = []

    if not matrix:
        return result

    L, T = 0, 0
    B, R = len(matrix) - 1, len(matrix[0]) - 1
    r, c = 0, 0

    while L <= R and T <= B:
        while c <= R:
            result.append(matrix[r][c])
            c += 1
        c -= 1
        r += 1
        T += 1

        while r <= B:
            result.append(matrix[r][c])
            r += 1
        r -= 1
        c -= 1
        R -= 1

        while c >= L:
            result.append(matrix[r][c])
            c -= 1
        c += 1
        r -= 1
        B -= 1

        while r >= T:
            result.append(matrix[r][c])
            r -= 1
        r += 1
        c += 1
        L += 1

    return result

# arr = [[np.random.randint(10) for c in range(10)] for r in range(10)]
# arr = [[1,2,3],[4,5,6],[7,8,9]]
# print(arr)
# print(spiral_array(arr))
