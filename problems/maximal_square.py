# Given an mxn matrix of 0s and 1s, return the side length of the largest
#     square sub-matrix whose elements are all 1s.

# Naive solution (O((m * n)^2 * log(m * n)) (I think?) time, O(1) space):
    # For each cell c, check the squares whose bottom corners are c, in
    #     ascending order of side length.
# Sub-optimal solution (O(m * n) time, O(m * n) space):
    # Dynamic programming, cache maximum side length at each cell.
    # MSL[i][j] = min(MSL[i - 1][j], MSL[i][j - 1], MSL[i - 1][j - 1]) + 1
    #     if mat[i][j] is 1, 0 otherwise
# Optimal solution (O(m * n) time, O(n) space):
    # For each cell c, only three cached MSL values are needed: the one above
    #     c, the one left of c, and the top-left diagonal of c.
    #
    #     |-----------|-----------|
    #     | tl_diag   | dp[j]     |
    #     |-----------|-----------|
    #     | dp[j - 1] | mat[i][j] |
    #     |-----------|-----------|
    #
    # Cache only n MSL values at any given time; at the beginning of a row, the
    #     MSL values of the row above should be cached initially; after the MSL
    #     calculation is made at the jth element of the row, overwrite the jth
    #     element of the cache with that value but save the overwritten value
    #     to a variable first because it is the diagonal of the upcoming cell.
    #
    #     |D|C|C|C|C|C|C|C|  -->  | |D|C|C|C|C|C|C|  -->  | | |D|C|C|C|C|C|
    #     |C|J| | | | | | |       |C|C|J| | | | | |       |C|C|C|J| | | | |
    #
    # Implementation detail: loop with i = 1..n, j = 1..n, preload the cache
    #     and diagonal. This avoids bottom corners in the top row or leftmost
    #     column, which cause out-of-bounds errors.

def maximal_square(matrix):
    if not matrix:
        return 0

    max_square_length = matrix[0][0]
    dp = matrix[0]
    top_left_diagonal = dp[0]

    mrows = len(matrix)
    ncols = len(matrix[0])
    for i in range(1, mrows):
        dp[0] = matrix[i][0]
        for j in range(1, ncols):
            temp = dp[j]
            if matrix[i][j]:
                dp[j] = min(dp[j], dp[j - 1], top_left_diagonal) + 1
                max_square_length = max(max_square_length, dp[j])
            else:
                dp[j] = 0
            top_left_diagonal = temp

    return max_square_length


if __name__ == "__main__":
    my_matrix = [[0, 1, 1],
                 [1, 1, 1],
                 [1, 0, 1],
                 [0, 1, 0],
                 [1, 1, 1]]
    for row in my_matrix:
        print(row)
    print(f"Max square length: {maximal_square(my_matrix)}")

