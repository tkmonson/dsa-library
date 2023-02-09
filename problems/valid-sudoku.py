'''
Valid Sudoku (#36)

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be
validated according to the following rules:
    1. Each row must contain the digits 1-9 without repetition
    2. Each column must contain the digits 1-9 without repetition
    3. Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9
       without repetition

A valid Sudoku board is not necessarily solvable.
'''

# Slightly faster?
def is_valid_sudoku2(board: list[list[str]]) -> bool:
    s = set()

    for r in range(9):
        for c in range(9):
            if board[r][c] != '.':
                v = board[r][c]

                key = f'{v} in row {r}'
                if key in s:
                    return False
                else:
                    s.add(key)

                key = f'{v} in col {c}'
                if key in s:
                    return False
                else:
                    s.add(key)

                box_index = (r // 3) * 3 + (c // 3)
                key = f'{v} in box {box_index}'
                if key in s:
                    return False
                else:
                    s.add(key)

    return True


def is_valid_sudoku(board: list[list[str]]) -> bool:
    col_sets = [set() for _ in range(9)]
    for r, row in enumerate(board):
        row_set = set()
        if r % 3 == 0:
            box_sets = [set() for _ in range(3)]
        for c, v in enumerate(row):
            if v != '.':
                if v in row_set or v in col_sets[c] or v in box_sets[c // 3]:
                    return False
                else:
                    row_set.add(v)
                    col_sets[c].add(v)
                    box_sets[c // 3].add(v)

    return True


if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    print(is_valid_sudoku(board))

