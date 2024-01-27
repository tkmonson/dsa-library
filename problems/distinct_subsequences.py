'''
Distinct Subsequences (#115)

Given two strings `s` and `t`, return the number of distinct subsequences of
`s` which equal `t`.
'''

from functools import cache

def num_distinct(s: str, t: str) -> int:
    m, n = len(s), len(t)
    @cache
    def dfs(i, j):
        if j == n:
            return 1
        if n - j > m - i:
            return 0
        a = 0 if s[i] != t[j] else dfs(i + 1, j + 1)
        b = dfs(i + 1, j)
        return a + b

    return dfs(0, 0)

'''
dfs(i, j) = number of subsequences of s[i:] that equal s[j:]
          = dfs(i + i, j + 1) + dfs(i + 1, j)
          = a + b

a is when you include s[i] in the subsequence. You can only do this if
s[i] == t[j]. Otherwise, there are 0 subsequences that can be formed beyond
this point.

b is when you skip s[i] in the subsequence. You can always do this.
'''

if __name__ == '__main__':
    s = 'babgbag'
    t = 'bag'
    print(num_distinct(s, t))

