'''
Range Sum Query 2D - Immutable (#304)

Given a 2D matrix `matrix`, handle multiple queries of the following type:
    * Calculate the sum of the elements of matrix inside the rectangle defined
      by its upper left corner `(row1, col1)` and lower right corner
      `(row2, col2)`.

Implement the NumMatrix class:
    * `NumMatrix(int[][] matrix)`: Initializes the object with the integer matrix
      `matrix`.
    * `int sum_region(int row1, int col1, int row2, int col2)`: Returns the sum
      of the elements of matrix inside the rectangle defined by its upper left
      corner `(row1, col1)` and lower right corner `(row2, col2)`.

You must design an algorithm where `sum_region` is O(1) in time.
'''

class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        R, C = len(matrix), len(matrix[0])
        pm = [[0 for _ in range(C)] for _ in range(R)]

        pm[0][0] = matrix[0][0]
        for r in range(1, R):
            pm[r][0] = pm[r - 1][0] + matrix[r][0]
        for c in range(1, C):
            pm[0][c] = pm[0][c - 1] + matrix[0][c]

        for r in range(1, R):
            for c in range(1, C):
                pm[r][c] = (pm[r - 1][c] + pm[r][c - 1]
                            - pm[r - 1][c - 1] + matrix[r][c])
                
        self.pm = pm

    def sum_region(self, row1: int, col1: int, row2: int, col2: int):
        row1 -= 1
        col1 -= 1
        top = self.pm[row1][col2] if row1 >= 0 else 0
        left = self.pm[row2][col1] if col1 >= 0 else 0
        diag = self.pm[row1][col1] if row1 >= 0 and col1 >= 0 else 0
        return (self.pm[row2][col2] - top - left + diag)

'''
Create a prefix sum matrix that stores the sum of every submatrix with top-left
corner of (0, 0) and bottom-right corner of (i, j). This can be used to compute
the sum for any submatrix in O(1) time.
'''

if __name__ == '__main__':
    nm = NumMatrix([
        [3,0,1,4,2],
        [5,6,3,2,1],
        [1,2,0,1,5],
        [4,1,0,1,7],
        [1,0,3,0,5]
    ])
    print(nm.sum_region(2,1,4,3))
    print(nm.sum_region(1,1,2,2))
    print(nm.sum_region(1,2,2,4))
