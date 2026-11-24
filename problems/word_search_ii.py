'''
Word Search II (#212)

Given an `m x n` board of characters and a list of strings `words`, return all
words on the board.

Each word must be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring. The same
letter cell may not be used more than once in a word.
'''

from collections import Counter

class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}


class Trie:
    def __init__(self, words: list[str]):
        self.root = TrieNode()
        for word in words:
            self.add_word(word)

    def add_word(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.word = word


def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    R, C = len(board), len(board[0])
    trie = Trie(words)
    result = []

    def dfs(curr, r, c):
        if board[r][c] not in curr.children:
            return

        # Found a word
        next = curr.children[board[r][c]]
        if next.word is not None:
            result.append(next.word)
            next.word = None

        temp, board[r][c] = board[r][c], '#'
        for (nr, nc) in ((r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)):
            if 0 <= nr < R and 0 <= nc < C:
                dfs(next, nr, nc)

        board[r][c] = temp
        # Prune the trie
        if not next.children:
            del curr.children[board[r][c]]

    for r in range(R):
        for c in range(C):
            dfs(trie.root, r, c)

    return result

'''
If you just run the function from Word Search I for each word, you will walk
the same paths for words that share a prefix. This is redundant work.

e.g. for ["cats", "cave", "cart"], you would walk "ca" paths multiple times.

We want a way to traverse a prefix path just once for all words that share that
prefix. A trie (prefix tree) can be used to do this. In a trie, each child
shares a prefix with its parent.

Similar to the Word Search I solution, traverse the board and do a DFS on each
start cell (any char that is a child of the trie's root). As you DFS through
the board looking for words, you also traverse through the trie. This allows
you to look for all words that may start at some start cell with one call
instead of making per-word calls on the same cell.

When all suffixes for some prefix are explored (all words have been found
beyond some node in the trie), you should prune the trie to avoid looking for
already-found words in future searches.

Since we are returning a list of words, it is helpful to store each word at its
terminal node in the trie instead of an is_word boolean. Otherwise, you need to
maintain path state.

Note that the optimizations from Word Search I are not needed when using a
trie. Reversing words breaks the prefixes they share with other words. The
character-count filter is potentially helpful, if the word set contains many
words that do not share prefixes.
'''

if __name__ == "__main__":
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    print(find_words(board, words))
