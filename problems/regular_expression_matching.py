'''
Regular Expression Matching (#10)

Given an input string `s` and a pattern `p`, implement regular expression
matching with support for '.' and '*' where:

    - '.' matches any single character,
    - '*' matches zero or more of the preceding element.

Return a boolean indicating whether the matching covers the entire input string
(not partial).
'''

from functools import cache

# Time: O(m * n), where m = len(s), n = len(p)
# Auxiliary space: O(m * n)
def is_match(s: str, p: str) -> bool:  # left-to-right
    m, n = len(s), len(p)

    @cache
    def f(i, j):
        if j == n:
            return i == m

        first_match = i < m and (s[i] == p[j] or p[j] == '.')

        # Consume the x* token from p or consume a single x from s
        if j + 1 < n and p[j + 1] == '*':
            if f(i, j + 2):
                return True
            if first_match:
                return f(i + 1, j)
            return False

        # Single char match
        if first_match:
            return f(i + 1, j + 1)

        return False  # Single char mismatch

    return f(0, 0)


# Time: O(m * n), where m = len(s), n = len(p)
# Auxiliary space: O(m * n)
def is_match2(s: str, p: str) -> bool:  # right-to-left
    @cache
    def f(i, j):
        if j == 0:
            return i == 0

        # Consume the x* token from p or consume a single x from s
        if p[j - 1] == '*':
            if f(i, j - 2):
                return True
            if i > 0 and (s[i - 1] == p[j - 2] or p[j - 2] == '.'):
                return f(i - 1, j)

        # Single char match
        if i > 0 and (s[i - 1] == p[j - 1] or p[j - 1] == '.'):
            return f(i - 1, j - 1)

        return False  # Single char mismatch

    return f(len(s), len(p))


# Time: O(m * n), where m = len(s), n = len(p)
# Auxiliary space: O(m * n)
def is_match3(s: str, p: str) -> bool:
    @cache
    def f(i, j):
        if i == 0:
            if j == 0:
                return True
            elif p[j - 1] == '*':
                return f(i, j - 2)
            else:
                return False

        if j == 0:
            return False

        # Single char match
        if s[i - 1] == p[j - 1] or p[j - 1] == '.':
            return f(i - 1, j - 1)

        # Consume the x* token from p or consume a single x from s
        if p[j - 1] == '*':
            if f(i, j - 2):
                return True
            if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                return f(i - 1, j)
                
        return False  # Single char mismatch

    return f(len(s), len(p))

'''
My first solution. I think this one is easiest to understand because it handles
the empty string cases first.
'''

# Time: O(m * n), where m = len(s), n = len(p)
# Auxiliary space: O(m * n)
def is_match4(s: str, p: str) -> bool:
    dp = set()
    def g(i, j):
        if (i, j) in dp:
            return False
        if f(i, j):
            return True
        dp.add((i, j))
        return False

    def f(i, j):
        if i == 0:
            if j == 0:
                return True
            elif p[j - 1] == '*':
                return g(i, j - 2)
            else:
                return False

        if j == 0:
            return False

        # Single char match
        if s[i - 1] == p[j - 1] or p[j - 1] == '.':
            return g(i - 1, j - 1)

        # Consume the x* token from p or consume a single x from s
        if p[j - 1] == '*':
            if g(i, j - 2):
                return True
            if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                return g(i - 1, j)
                
        return False  # Single char mismatch

    return f(len(s), len(p))

'''
My first solution, but with explicit caching logic.
'''

if __name__ == '__main__':
    s = 'ab'
    p = '.*'
    print(is_match(s, p))

'''
Think like a parser. The pattern string contains three kinds of tokens: a
letter, a dot, or a star token (x*). When processing a star token, you cannot
immediately know how many chars of s it should match: 0, 1, 2, ... You need to
make a choice and then backtrack if it doesn't work. Recursion is a natural way
to implement this.

If s and p are empty:
    - Return True

If s is empty and p is not empty:
    - s and p can match if p contains only star tokens

If s is not empty and p is empty:
    - Return False

If s and p are not empty:
    p token is letter:
        - If match, continue
        - If not match, return False
    p token is dot:
        - Continue
    p token is star token:
        - Consume the p token (match 0 chars in s)
        - Consume 1 s token (if it matches), carry p token into next recursion

2D and 1D tabulation solutions are also possible for this problem. For long
inputs, tabulation will avoid the possibility of reaching max recursion depth.
The 1D tabulation solution would have O(n) auxiliary space.
'''
