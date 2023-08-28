'''
Word Search (#79)

Given a grid of characters `board` and a string `word`, return True if `word`
exists in `board`, False otherwise. `word` exists in `board` if it can be
constructed from letters in horizontally or vertically adjacent cells.
'''

def word_exists(board: list[list[str]], word: str) -> bool:
    R, C = len(board), len(board[0])
    seen = set()

    def dfs(i, r, c):
        if i == len(word):
            return True
        if (r < 0 or r >= R or c < 0 or c >= C or board[r][c] != word[i] or
            (r,c) in seen):
            return False

        seen.add((r, c))
        found = (
            dfs(i + 1, r, c + 1) or
            dfs(i + 1, r + 1, c) or
            dfs(i + 1, r, c - 1) or
            dfs(i + 1, r - 1, c)
        )
        seen.remove((r, c))
        return found

    for r in range(R):
        for c in range(C):
            if dfs(0, r, c):
                return True

    return False


def word_exists2(board: list[list[str]], word: str) -> bool:
    if len(word) > len(board) * len(board[0]):
        return False

    count = Counter(sum(board, []))
    for c, count_word in Counter(word).items():
        if count[c] < count_word:
            return False

    if count[word[0]] > count[word[-1]]:
        word = word[::-1]

    return word_exists(board, word)


if __name__ == '__main__':
    board = [['a', 'a']]
    word = 'aaa'
    print(word_exists(board, word))

