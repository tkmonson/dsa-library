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
            return 2

        memo[(x, y)] = min(dfs(x - 2, y - 1), dfs(x - 1, y - 2)) + 1
        return memo[(x, y)]

    return dfs(x, y)

if __name__ == '__main__':
    print(min_knight_moves(5, 5))

