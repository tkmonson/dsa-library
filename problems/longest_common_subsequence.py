'''
Longest Common Subsequence (#1143)

Given two strings, return the length of their longest common subsequence. If
there is no common subsequence, return 0.
'''

from functools import cache

# Time: O(2^(m + n))?
# Auxiliary space: O(m + n)
def longest_common_subsequence_memo(s1: str, s2: str) -> int:
    @cache
    def lcs(i, j):
        if i < 0 or j < 0:
            return 0
        if s1[i] == s2[j]:
            return dfs(i - 1, j - 1) + 1
        return max(dfs(i, j - 1), dfs(i - 1, j))

    return lcs(len(s1) - 1, len(s2) - 1)


# Time: O(m*n)
# Auxiliary space: O(m*n)
def longest_common_subsequence_tab_2d(s1: str, s2: str) -> int:
    m, n = len(s1) + 1, len(s2) + 1
    dp = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    return dp[-1][-1]


# Time: O(m*n)
# Auxiliary space: O(n), where n <= m
def longest_common_subsequence_tab_1d(s1: str, s2: str) -> int:
    lil, big = (s1, s2) if s1 < s2 else (s2, s1)
    m, n = len(big), len(lil) + 1
    dp = [0 for _ in range(n)]

    for i in range(m):
        diag = 0
        for j in range(1, n):
            if big[i] == lil[j - 1]:
                dp[j], diag = diag, dp[j]
                dp[j] += 1
            else:
                diag = dp[j]
                dp[j] = max(dp[j - 1], dp[j])

    return dp[-1]

'''
To minimize space complexity, the 1D table should have length equal to that of
the smaller string + 1.
'''

if __name__ == '__main__':
    s1 = 'GAC'
    s2 = 'AGCAT'
    print(longest_common_subsequence_tab_1d(s1, s2))

'''
Let LCS(x, y) be a function that computes a longest subsequence common to x and
y. Such a function has two interesting properties.

1. LCS(x + c, y + c) = LCS(x, y) + c, where `x` and `y` are strings, `c` is a
character, and `+` denotes string concatenation.

    e.g. LCS('ABCDEFG', 'BCDG') = LCS('ABCDEF', 'BCD') + 'G'

2. If c and d are distinct characters (c != d), then LCS(x + c, y + d) is one
of the maximal-length strings in {LCS(x + c, y), LCS(x, y + d)}.

    e.g. If LCS('ABCDEFG', 'BCDGK') ends with a 'G', then the final 'K' is not
         in the LCS. LCS('ABCDEFG', 'BCDGK') = LCS('ABCDEFG', 'BCDG').

         If LCS('ABCDEFG', 'BCDGK') does not end with a 'G', then the final 'G'
         is not in the LCS. LCS('ABCDEFG', 'BCDGK') = LCS('ABCDEF', 'BCDGK').

Note that if x or y are empty, LCS(x, y) is also empty.

Construct an mxn table where m = len(x) + 1 and n = len(y) + 1. The 0th row and
col should be pre-loaded with empty strings.

    |   | * | B | C | D | G | K |
    | * | *   *   *   *   *   *
    | A | *
    | B | *
    | C | *
    | D | *
    | E | *
    | F | *
    | G | *

Let the prefix `s_n` of `s` be the first `n` characters of `s`.
If x_i and y_j have the same last character c:
    => LCS(x_i, y_j) = LCS(x_(i - 1), y_(j - 1)) + c
    => dp[i][j] = dp[i - 1][j - 1] + c.
Else:
    => LCS(x_i, y_j) = max(LCS(x_i, y_(j - 1)), LCS(x_(i - 1), y_j))
    => dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]).
'''

