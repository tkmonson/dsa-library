'''
N-Queens (#51)

The n-queens puzzle is the problem of placing n queens on an nxn chessboard
such that no two queens can attack each other. Given an integer n, return all
distinct solutions to the n-queens problem, in any order. 'Q' indicates a queen
and '.' indicates an empty space.

E.g. n = 4  =>  [['.Q..',  ['..Q.',
                  '...Q',   'Q...',
                  'Q...',   '...Q',
                  '..Q.'],  '.Q..']]
'''

from itertools import permutations

# READ SOLUTION COMMENTS BOTTOM TO TOP

# Considers 15720 placements, running an O(1) check on each
def solve_n_queens(n: int) -> list[list[str]]:
    col = set()
    pos_diag = set()  # (r + c)
    neg_diag = set()  # (r - c)

    result = []
    board = [['.'] * n for _ in range(n)]

    def dfs(r):
        if r == n:
            result.append([''.join(row) for row in board])
            return

        for c in range(n):
            if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                continue

            col.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = 'Q'

            dfs(r + 1)

            col.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = '.'

    dfs(0)
    return result

'''
If a queen is placed at (r, c), for every cell (r_i, c_i) along its positive
diagonal, r + c = r_i + c_i, and for every cell (r_j, c_j) along its negative
diagonal, r - c = r_j - c_j. By storing these cells in sets, we eliminate the
O(n) diagonal check function.
'''

# Considers 5508 placements, running an O(n) check on each
def solve_n_queens2(n: int) -> list[list[str]]:
    def is_valid_placement(state, col):
        lcol = rcol = col
        for r in range(len(state) - 1, -1, -1):
            lcol -= 1
            rcol += 1
            if lcol == state[r] or rcol == state[r]:
                return False
        return True

    def dfs():
        if len(state) == n:
            board = ['.' * c + 'Q' + '.' * (n - c - 1) for c in state]
            result.append(board)
            return

        for c in remaining_columns.copy():
            if is_valid_placement(state, c):
                state.append(c)
                remaining_columns.remove(c)
                dfs()
                state.pop()
                remaining_columns.add(c)

    result = []
    state = []
    remaining_columns = set(range(n))
    dfs()
    return result

'''
Similar to the backtracking solution below, but instead of considering every
column for each row, consider only the columns that have not already been
filled in a previous row. By doing this, you need only check for diagonal
attacks.

Note that creating a set in every recursive call is memory-inefficient. But
there isn't really a good way to avoid this while keeping the set in a for-each
loop.
'''

# Considers 15720 placements, running an O(n) check on each
def solve_n_queens3(n: int) -> list[list[str]]:
    def is_valid_placement(state, col):
        lcol = rcol = col
        for r in range(len(state) - 1, -1, -1):
            lcol -= 1
            rcol += 1
            if col == state[r] or lcol == state[r] or rcol == state[r]:
                return False
        return True

    def dfs():
        if len(state) == n:
            board = ['.' * c + 'Q' + '.' * (n - c - 1) for c in state]
            result.append(board)
            return

        for i in range(n):
            if is_valid_placement(state, i):
                state.append(i)
                dfs()
                state.pop()

    result = []
    state = []
    dfs()
    return result

'''
Given a partial board (n columns, <n rows), consider all columns where a queen
could be placed in the next row. For each column, check if placing a queen
there will produce a vertical or diagonal attack. Once you find a valid column,
put a queen there and move on to the next row. When you create a full board,
save it as a solution. Then, backtrack (remove the deepest queen to consider
other possible placements for it in the same row).
'''

# Considers 40320 placements, running an O(n^2) check on each
def solve_n_queens4(n: int) -> list[list[str]]:
    def is_valid_board(state):
        for i in range(n):
            lcol = rcol = state[i]
            for j in range(i + 1, n):
                lcol -= 1
                rcol += 1
                if lcol == state[j] or rcol == state[j]:
                    return False
        return True

    result = []
    perms = permutations(range(n))
    for p in perms:
        if is_valid_board(p):
            board = ['.' * c + 'Q' + '.' * (n - c - 1) for c in p]
            result.append(board)

    return result

'''
Let an nxn board with 1 placement per row be represented by an n-tuple where an
element of the tuple represents the column of a placement. Generate all
permutations of [0, 1, ..., n] (all solutions to the n-rooks problem). Filter
out any solutions that contain a diagonal attack.
'''

if __name__ == '__main__':
    n = 8
    print(solve_n_queens(n))

