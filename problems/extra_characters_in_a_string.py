'''
Extra Characters in a String (#2707)

You are given a 0-indexed string `s` and a dictionary of words `dictionary`.
You have to break `s` into one or more non-overlapping substrings such that
each substring is present in `dictionary`. There may be some extra characters
in `s` which are not present in any of the substrings.

Return the minimum number of extra characters in `s` which are not present in
any of the substrings.
'''

# Time: O(n^3)
# Auxiliary space: O(n)
def min_extra_char(s: str, dictionary: list[str]) -> int:
    words = set(dictionary)
    dp = { len(s): 0 }
    def dfs(i):  # n nested calls (starts)
        if i in dp:
            return dp[i]

        res = 1 + dfs(i + 1)
        for j in range(i, len(s)):  # n substrings (ends)
            if s[i:j+1] in words:  # n slice operations
                res = min(res, dfs(j + 1))

        dp[i] = res
        return res
    
    return dfs(0)

'''
If you greedily search for substrings in dictionary, you won't minimize extra
chars.

For any char in the string, you can skip. You can skip whole substrings.
You can only "take" a substring if it is in the dictionary. But you don't have
to take it: "abcdef", ["abc", "bcdef"] => better to not take "abc".

This implies that you need dynamic programming.

At each char, you can:
    1. skip the char
    2. consider different substrings starting from that char

Find the optimal answers to f(i), use them to find the optimal answer to f(0).
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for w in words:
            curr = self.root
            for c in w:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = True

# Time: O(n^2)
# Auxiliary space: O(n)
def min_extra_char_trie(s: str, dictionary: list[str]) -> int:
    dp = { len(s): 0 }
    trie = Trie(dictionary).root

    def dfs(i):  # n nested calls
        if i in dp:
            return dp[i]

        res = 1 + dfs(i + 1)
        curr = trie
        for j in range(i, len(s)):  # n substrings
            if s[j] not in curr.children:
                break
            curr = curr.children[s[j]]
            if curr.word:
                res = min(res, dfs(j + 1))
        dp[i] = res
        return res
    
    return dfs(0)

'''
You can further optimize by pruning the search for any substring that is not a
prefix of any word in the dictionary (appending more chars won't help). To do
this, turn the dictionary into a prefix tree (trie). As you append more chars,
traverse the trie.
'''

if __name__ == '__main__':
    s = 'hugecatdog'
    dictionary = ['huge', 'hugecat', 'dog']
    print(min_extra_char(s, dictionary))

