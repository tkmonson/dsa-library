# Time: O(3^(m*n)) (3 fresh branches at each step)
# Auxiliary space: O(m*n) (stack space; path can cover whole grid)
def robotPaths(matrix):
    row_dim = len(matrix)
    col_dim = len(matrix[0])
    
    def helper(r,c):
        if (r < 0 or c < 0 or
            r >= row_dim or c >= col_dim or
            matrix[r][c] == 1):
            return 0
        if (r,c) == (row_dim-1, col_dim-1):
            return 1

        matrix[r][c] = 1

        paths = 0  
        paths += helper(r-1, c)
        paths += helper(r+1, c)
        paths += helper(r, c-1)
        paths += helper(r, c+1)
         
        matrix[r][c] = 0

        return paths
    
    return helper(0, 0)


if __name__ == '__main__':
    print(robotPaths([[0 for c in range(4)] for r in range(3)]))

'''
Dynamic programming will not work for this problem...
'''
