'''
Interleaving String (#97)

Given strings `s1`, `s2`, and `s3`, find whether `s3` is formed by an
interleaving of `s1` and `s2`. An interleaving of two strings `s` and `t`
is a configuration where `s` and `t` are divided into `a` and `b`
substrings respectively, such that:

    * s = s_1 + s_2 + ... + s_a
    * t = t_1 + t_2 + ... + t_b
    * |m - n| <= 1
    * The interleaving is s_1 + t_1 + s_2 + t_2 + s_3 + t_3 + ... or
    t_1 + s_1 + t_2 + s_2 + t_3 + s_3 + ...
'''

from functools import cache

def is_interleave_memo(s1: str, s2: str, s3: str) -> bool:
    m, n = len(s1), len(s2)
    if m + n != len(s3):
        return False

    @cache
    def dfs(i, j):
        if i == m and j == n:
            return True

        ans = False
        if i < m:
            ans |= s1[i] == s3[i + j] and dfs(i + 1, j)
        if j < n:
            ans |= s2[j] == s3[i + j] and dfs(i, j + 1)

        return ans

    return dfs(0, 0)

'''
If s3 is an interleaving of s1 and s2, s3[0] is going to be equal to either
s1[0] or s2[0]. If we take s1[0], then s3[1] = s1[1] or s2[0]. But if we take
s2[0], then s3[1] = s1[0] or s2[1]. And so on... You either expand the
substring of the current string or start a new substring from the other string.
'''

def is_interleave_tab_2d(s1: str, s2: str, s3: str) -> bool:
    m, n = len(s1), len(s2)
    if m + n != len(s3):
        return False

    dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
    dp[0][0] = True

    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] |= dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
            dp[i][j] |= dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]

    return dp[m][n]

'''
Create a 2D DP array like this, where * is a null character:

        0 1 2 3 4 5
        * d b b c a
    0 *  
    1 a
    2 a
    3 b
    4 c
    5 c

dp[i][j] = is s3[:i + j] an interleaving of s1[:i] and s2[:j]?
It is if:
    * s3[:i + j - 1] is an interleaving of s1[:i - 1] and s2[:j] and
      s1[i - 1] == s3[i + j - 1] or
    * s3[:i + j - 1] is an interleaving of s1[:i] and s2[:j - 1] and
      s2[j - 1] == s3[i + j - 1]

Because we are using cached values from above and to the left, fill out the
first row and column before filling the rest of the table.
'''

def is_interleave_tab_1d(s1: str, s2: str, s3: str) -> bool:
    s1, s2 = (s1, s2) if len(s1) > len(s2) else (s2, s1)
    m, n = len(s1), len(s2)
    if m + n != len(s3):
        return False

    dp = [False for _ in range(n + 1)]
    dp[0] = True
    for j in range(1, n + 1):
        dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

    for i in range(1, m + 1):
        dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
        for j in range(1, n + 1):
            dp[j] = dp[j] and s1[i - 1] == s3[i + j - 1]
            dp[j] |= dp[j - 1] and s2[j - 1] == s3[i + j - 1]

    return dp[n]


if __name__ == '__main__':
    print(is_interleave_tab_1d('aabcc', 'dbbca', 'aadbbcbcac'))

