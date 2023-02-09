'''
Surrounded Regions (#130)

Given an mxn matrix board containing 'X's and 'O's, capture all regions that
are 4-directionally surrounded by 'X'. A region is captured by flipping all
'O's into 'X's in that surrounded region.
'''

def solve2(board: list[list[str]]) -> None:
    m, n = len(board), len(board[0])

    def explore(r, c):
        if r < 0 or r >= m or c < 0 or c >= n:
            return
        if board[r][c] == 'O':
            board[r][c] = '#'
        else:
            return
        explore(r, c + 1)
        explore(r + 1, c)
        explore(r, c - 1)
        explore(r - 1, c)

    for r in range(0, m):
        if board[r][0] == 'O':
            explore(r, 0)
        if board[r][n - 1] == 'O':
            explore(r, n - 1)

    for c in range(1, n - 1):
        if board[0][c] == 'O':
            explore(0, c)
        if board[m - 1][c] == 'O':
            explore(m - 1, c)

    for r in range(0, m):
        for c in range(0, n):
            if board[r][c] == '#':
                board[r][c] = 'O'
            else:
                board[r][c] = 'X'


def solve(board: list[list[str]]) -> None:
    m, n = len(board), len(board[0])
    visited_Os = set()

    for r in range(m):
        for c in range(n):
            if board[r][c] == 'O' and (r, c) not in visited_Os:
                v = set()
                is_surrounded = True

                def explore(r, c):
                    nonlocal v, is_surrounded
                    if r < 0 or r >= m or c < 0 or c >= n:
                        return
                    if board[r][c] == 'X' or (r,c) in v:
                        return
                    if r == 0 or r == m - 1 or c == 0 or c == n - 1:
                        is_surrounded = False
                    v.add((r,c))
                    explore(r, c + 1)
                    explore(r + 1, c)
                    explore(r, c - 1)
                    explore(r - 1, c)

                explore(r, c)
                if is_surrounded:
                    for (x, y) in v:
                        board[x][y] = 'X'
                else:
                    visited_Os.union(v)


if __name__ == '__main__':
    board = [['X','O','X','O','X','O'],
             ['O','X','O','X','O','X'],
             ['X','O','X','O','X','O'],
             ['O','X','O','X','O','X']]

    p = lambda b: '\n'.join([' '.join(row) for row in b])
    print(p(board) + '\n')
    solve2(board)
    print(p(board))

'''
Because this problem involved islands, I knew that I would have to DFS/BFS
whenever I came across a potential island. So the general design would be to
linearly search through the board and perform a DFS whenever I came across
an 'O'. However, since an island consists of adjacent 'O's, I didn't want to
explore an island, traverse to an adjacent 'O' in the same island, and then
explore the same island. I avoided this problem by flipping 'O's to 'X's when I
determined that a region was surrounded or adding all of the coordinates of the
region to a set when I determined it was not surrounded. This solution worked
but was inefficient and inelegant.

Because a region of 'O's is surrounded if and only if none of its elements
exist on the borders of the board, one can explore all non-surrounded regions
of 'O's by traversing the borders of the board first and performing a DFS/BFS
at each encountered 'O'. Instead of keeping track of these regions in an
auxiliary set, it is more efficient to store this information in the board
itself by marking these regions with a third value like '#'. Then, one only
needs to linearly traverse the board, flipping 'O's to 'X's and '#'s to 'O's.
'''

