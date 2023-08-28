'''
Word Break (#139)

Given a string `s` and a list of strings `word_dict`, return True if `s` can be
segmented into a space-separated sequence of one or more words in `word_dict`.
The same word may be reused multiple times in the segmentation.
'''

from functools import lru_cache

# Top-down
# Time: O(n^3 + m) where n = len(s), m = len(word_dict)
# Auxiliary space: O(n + m)
def word_break_memo(s: str, word_dict: list[str]) -> bool:
    n = len(s)
    word_dict = set(word_dict)

    @lru_cache
    def dfs(i):
        if i == n:
            return True

        word = ''
        for j in range(i, n):
            word += s[j]  # O(n)
            if word in word_dict and dfs(j + 1):
                return True
        return False

    return dfs(0)

'''
Start at beginning of s, add characters one at a time to word. When word is in
word_dict, repeat the process with a new empty word, starting at the character
to the right of the previous word. If you get to the end of s and the current
word is not in word_dict, backtrack to the previous word and add characters to
it until it is in word_dict, and then repeat the process with the rest of s.

When dfs(i) returns True or False, that indicates whether or not s[i:] can be
segmented into words in word_dict. This answer is cached so that that section
of s is not explored again in the future after backtracking and resegmenting.
'''

# Bottom-up
# Time: O(n^3 + m) where n = len(s), m = len(word_dict)
# Auxiliary space: O(n + m)
def word_break_tab(s: str, word_dict: list[str]) -> bool:
    word_dict = set(word_dict)
    n = len(s)
    
    dp = [False] * (n + 1)
    dp[n] = True
    for i in range(n - 1, -1, -1):
        word = ''
        for j in range(i, n):
            word += s[j]  # O(n)
            if word in word_dict and dp[j + 1]:
                dp[i] = True
                break
    
    return dp[0]

'''
Consider the smallest substring that starts at n - 1. If it is in word_dict,
then s[n - 1:] can be segmented into words in word_dict. Consider the smallest
substring that starts at n - 2. If it is in word_dict and s[n - 1:] can be
segmented into words in word_dict, then s[n - 2:] can also be segmented.
Otherwise, expand the substring to the right to consider the substring of
length 2 that starts at n - 2. If it is in word_dict, then s[n - 2:] can be
segmented. Continue this process of moving the start of the substring to the
left, checking if the substring is in word_dict and if the rest of s to the
right of it can be segmented, and expanding the substring to the right if not.
'''

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.child = defaultdict(TrieNode)
    
    def add_word(self, word):
        curr = self
        for c in word:
            curr = curr.child[c]
        curr.is_word = True


# Time: O(n^2 + t) where n = len(s), t = sum([len(w) for w in word_dict])
# Auxiliary space: O(n + m)
def word_break_trie(s: str, word_dict: list[str]) -> bool:
    root = TrieNode()
    for word in word_dict:
        root.add_word(word)
        
    n = len(s)
    dp = [False] * (n + 1)
    dp[n] = True
    
    for i in range(n - 1, -1, -1):
        curr = root
        for j in range(i, n):
            c = s[j]
            if c not in curr.child:
                break  # s[i : j + 1] does not exist in trie
            curr = curr.child[c]
            if curr.is_word and dp[j + 1]:
                dp[i] = True
                break
    
    return dp[0]

'''
Put words from word_dict in a trie. Perform the tabulation algorithm but
instead of appending characters to a substring, which is O(n), traverse the
trie and only move i to the left and begin a new search if you know the word
does not exist in the trie or if you have found the word in the trie and
s[j + 1:] can be segmented.
'''

if __name__ == '__main__':
    # s = 'catsandog'
    # word_dict = ['cats', 'dog', 'sand', 'and', 'cat']
    s = 'aaaaaaaaaaaaaaaaaaaab'
    word_dict = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa']
    print(word_break_memo(s, word_dict))

'''
When considering top-down and bottom-up dynamic programming algorithms for a
string, the top is the largest possible substring (that is, the entire string)
and the bottom is the smallest possible substring (in this case, a string of
length 1). Because this problem specifies that words from word_dict must fit
between the boundaries of the start and end of s (that is, words cannot overlap
the boundaries), the bottom must be located at the start (s[0]) or end
(s[n - 1]) of the string. Because words are traditionally read left-to-right,
it makes the most sense to consider the bottom to be located at the right side
of s, but you could do it on the left by reading the characters in reverse
order. Similarly, it makes the most sense to consider the top to be located at
the left side of s because reading s left-to-right in one pass (as in the case
where word_dict = [s]) is processing the largest problem first. The problem is
only broken into subproblems if matches are found in word_dict.
'''

