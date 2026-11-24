'''
Word Search (#79)

Given a grid of characters `board` and a string `word`, return True if `word`
exists in `board`, False otherwise. `word` exists in `board` if it can be
constructed from letters in horizontally or vertically adjacent cells.
'''

from collections import Counter

# Time: O(R * C * 3^L), where L = len(word) (3^L paths per starting cell
#       because there are 3 useful directions per step after first step)
# Auxiliary space: O(L) (stack space)
def exists(board: list[list[str]], word: str) -> bool:
    R, C = len(board), len(board[0])

    def dfs(i, r, c):
        if board[r][c] != word[i]:
            return False

        if i == len(word) - 1:
            return True

        temp, board[r][c] = board[r][c], '#'
        for (nr, nc) in ((r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)):
            if 0 <= nr < R and 0 <= nc < C and dfs(i + 1, nr, nc):
                board[r][c] = temp
                return True

        board[r][c] = temp
        return False

    for r in range(R):
        for c in range(C):
            if dfs(0, r, c):
                return True

    return False

'''
At each potential start cell of the word, do a DFS. The DFS can move in four
directions, but it cannot intersect itself, so mark each cell visited in the
current search and restore them as you backtrack.
'''

# Time: O(R * C * 3^L)
# Auxiliary space: O(L) (stack space; counters use a fixed char set)
def exists2(board: list[list[str]], word: str) -> bool:
    # Check that board has enough of each char for word to potentially match
    count = Counter(cell for row in board for cell in row)  # generator
    for c, count_word in Counter(word).items():
        if count[c] < count_word:
            return False

    # Reverse word if last char is rarer than first char (fewer DFS calls)
    if count[word[0]] > count[word[-1]]:
        word = word[::-1]

    return exists(board, word)

'''
The optimizations in this solution greatly improve the runtime performance.
'''

if __name__ == '__main__':
    board = [['a', 'a']]
    word = 'aaa'
    print(exists(board, word))
