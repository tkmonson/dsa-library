'''
Longest Palindromic Substring (#5)

Given a string, return its longest palindromic substring.
'''

def longest_palindrome(s: str) -> str:
    bounds = (0, 0)  # the half-closed interval [a, b)
    n = len(s)
    if n == 1: return s

    def f(left, right):
        nonlocal bounds
        while left > 0 and right < n and s[left - 1] == s[right]:
            left -= 1
            right += 1
        if right - left > bounds[1] - bounds[0]:
            bounds = (left, right)

    for i in range(n - 1):
        f(i, i + 1)
        if s[i] == s[i + 1]:
            f(i, i + 2)

    return s[bounds[0] : bounds[1]]

'''
For each character/continguous pair, build out from the middle until you make
the longest palindrome centered at that character/contiguous pair.

For each i, this algorithm builds from a string of length 1 or 2, even when the
longest palindrome found so far is larger than that.
'''

def longest_palindrome2(s: str) -> str:
    if s == s[::-1]:
        return s
    is_palindrome = lambda a, b: (c := s[a : b]) == c[::-1]
    start, size = 0, 1
    for i in range(1, len(s)):
        left = i - size
        right = i + 1
        if left > 0 and is_palindrome(left - 1, right):
            start = left - 1
            size += 2
        elif is_palindrome(left, right):
            start = left
            size += 1

    return s[start : start + size]

'''
This algorithm is faster because it only ever evaluates substrings that are
longer than the longest palindrome found so far.
'''

if __name__ == '__main__':
    s = 'babad'
    print(longest_palindrome(s))

