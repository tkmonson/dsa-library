'''
Minimum Knight Moves

A knight is located at (0,0) on an infinite chess board. Given a destination
(x, y), return the minimum number of moves from (0, 0) to (x, y).
'''

def min_knight_moves(x: int, y: int) -> int:
    memo = {}
    def dfs(x, y):
        x, y = abs(x), abs(y)
        if (x, y) in memo:
            return memo[(x, y)]
        if x + y == 0:
            return 0
        if x + y == 2:
            return 4

        memo[(x, y)] = min(dfs(x - 2, y - 1), dfs(x - 1, y - 2)) + 1
        return memo[(x, y)]

    return dfs(x, y)

def min_knight_moves2(x1: int, y1: int, x2: int, y2: int) -> int:
    if x2 < x1:
        x2 += 2 * (x1 - x2)
    if y2 < y1:
        y2 += 2 * (y1 - y2)

    return min_knight_moves(x2 - x1, y2 - y1)

if __name__ == '__main__':
    print(min_knight_moves(1, 1))

