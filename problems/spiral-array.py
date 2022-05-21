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

