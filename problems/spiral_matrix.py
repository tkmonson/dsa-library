'''
Spiral Matrix (#54)

Given an rxc matrix, return all elements of the matrix in spiral order.

    [                    1 > 2 > 3
     [1, 2, 3],                  v
     [4, 5, 6],    =>    4 > 5   6    =>    [1, 2, 3, 6, 9, 8, 7, 4, 5]
     [7, 8, 9]           ^       v
    ]                    7 < 8 < 9

'''

def spiral_order(matrix: list[list[int]]) -> list[int]:
    r, c = len(matrix) - 1, len(matrix[0]) - 1
    i, j = 0, c
    result = matrix[0]

    while True:
        if r <= 0: break
        for _ in range(r):
            i += 1
            result.append(matrix[i][j])
        r -= 1

        if c <= 0: break
        for _ in range(c):
            j -= 1
            result.append(matrix[i][j])
        c -= 1

        if r <= 0: break
        for _ in range(r):
            i -= 1
            result.append(matrix[i][j])
        r -= 1

        if c <= 0: break
        for _ in range(c):
            j += 1
            result.append(matrix[i][j])
        c -= 1
    
    return result


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(spiral_order(matrix))

