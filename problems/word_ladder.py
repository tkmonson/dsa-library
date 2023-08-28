'''
Word Ladder (#127)

A transformation sequence from word `begin_word` to word `end_word` using a
dictionary `word_list` is a sequence of words `begin_word -> s_1 -> s_2 -> ...
-> s_k` such that:
    * Every adjacent pair of words differs by a single letter
    * Every `s_i` for `1 <= i <= k` is in `word_list` (`begin_word` does not
      need to be in `word_list`)
    * `s_k == end_word`

Given two words, `begin_word` and `end_word`, and a dictionary `word_list`,
return the number of words in the shortest transformation sequence from
`begin_word` to `end_word`, or 0 if no such sequence exists.

All given words have the same length and consist of lowercase letters.
`begin_word` and `end_word` are not equal. All words in `word_list` are unique.
'''

from collections import deque

# Time: O(m*n^2) where m = word length, n = number of words (worst-case: one
#       pattern maps to all words except end_word, no sequence exists)
# Auxiliary space: O(m*n)
def ladder_length(begin_word: str, end_word: str, word_list: list[str]) -> int:
    change_map = {}
    word_list.append(begin_word)
    for word in word_list:
        for i in range(len(word)):
            pattern = word[:i] + '*' + word[i + 1:]
            if pattern not in change_map:
                change_map[pattern] = []
            change_map[pattern].append(word)

    visited = set()
    next_level = [begin_word]
    path_length = 0
    while next_level:
        q = deque(next_level)
        next_level = []
        path_length += 1
        while q:
            word = q.popleft()
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                neighbors = change_map[pattern]
                for neighbor in neighbors:
                    if neighbor == end_word:
                        return path_length + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        next_level.append(neighbor)

    return 0

'''
Each word has len(word) patterns that represent the 26 * len(word) words that
it can transition to (e.g. hit -> *it, h*t, hi*). Create a map from patterns to
words for begin_word and all words in word_list. This fulfills the same role as
an adjacency list. Perform a level-order traversal (because you want the
shortest path) through the tree described by this map (using a visited set will
prevent cycles, allowing you to interpret the map as a tree rather than as a
graph).
'''

if __name__ == '__main__':
    begin_word = 'hit'
    end_word = 'cog'
    word_list = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
    print(ladder_length(begin_word, end_word, word_list))

