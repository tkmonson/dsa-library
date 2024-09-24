'''
Diagonal Traverse (#498)

Given an mxn matrix, return an array of all its elements in diagonal order.

E.g. [[1, 2, 3],
      [4, 5, 6],  =>  [1, 2, 4, 7, 5, 3, 6, 8, 9]
      [7, 8, 9]]
'''

from collections import defaultdict

# Time: O(mn)
# Auxiliary space: O(n)
def find_diagonal_order(mat: list[list[int]]) -> list[int]:
    diagonal_dict = defaultdict(list)

    for r in range(len(mat)):
        for c in range(len(mat[0])):
            diagonal_dict[r + c].append(mat[r][c])

    result = []
    for i, v in enumerate(diagonal_dict.values()):
        if i % 2 == 0:
            result += v[::-1]
        else:
            result += v

    return result

'''
Insight: elements along a "top-right to bottom-left" diagonal have the same
         r + c value, where r and c are row and column indicies, respectively.

Group the elements by diagonal while traversing the matrix left-to-right,
top-to-bottom. Flip the order of every other diagonal.
'''

# Time: O(mn)
# Auxiliary space: O(n)
def find_diagonal_order2(mat: list[list[int]]) -> list[int]:
    result = []
    for i in range(len(mat[0]) - 1):
        diag = []
        r, c = 0, i
        while r < len(mat) and c >= 0:
            diag.append(mat[r][c])
            r += 1
            c -= 1
        result += diag if i % 2 else diag[::-1]

    down = len(mat[0]) % 2 == 0
    for i in range(len(mat)):
        diag = []
        r, c = i, len(mat[0]) - 1
        while r < len(mat) and c >= 0:
            diag.append(mat[r][c])
            r += 1
            c -= 1
        result += diag if down else diag[::-1]
        down = not down

    return result

'''
Instead of traversing the diagonals in alternating directions, traverse all of
them from top-right to bottom-left. The starting points are contained in the
top row and the last column. Flip the order of every other diagonal.
'''

if __name__ == '__main__':
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(find_diagonal_order2(mat))

'''
While you could traverse the matrix in diagonal order, the associated logic is
complicated and requires a lot of finicky checks. The above strategies are
simpler to understand and implement.
'''

