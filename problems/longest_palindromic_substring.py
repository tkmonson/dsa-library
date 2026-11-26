'''
Longest Palindromic Substring (#5)

Given a string, return its longest palindromic substring.
'''

# Time: O(n^2)
# Auxiliary space: O(1)
def longest_palindrome(s: str) -> str:
    n = len(s)

    def expand(lo: int, hi: int) -> tuple[int, int]:
        # Grow the palindrome s[lo:hi] while the chars just outside it match
        while lo > 0 and hi < n and s[lo - 1] == s[hi]:
            lo -= 1
            hi += 1
        return lo, hi

    best = (0, 0)
    for i in range(n):
        for lo, hi in (expand(i, i), expand(i, i + 1)):  # even, odd
            if hi - lo > best[1] - best[0]:
                best = (lo, hi)

    return s[best[0] : best[1]]

'''
Simpler version of the expand-from-center solution below. Preferred for
test-taking scenarios.
'''

# Time: O(n^2)
# Auxiliary space: O(1)
def longest_palindrome2(s: str) -> str:
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

# Time: O(n^2)
# Auxiliary space: O(n)
def longest_palindrome3(s: str) -> str:
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

# Time: O(n^2)
# Auxiliary space: O(n)
def longest_palindrome4(s: str) -> str:
    start, size = 0, 0
    for end in range(1, len(s) + 1):
        for k in (size + 2, size + 1):
            lo = end - k
            if lo >= 0 and s[lo:end] == s[lo:end][::-1]:
                start, size = lo, k
                break
    return s[start : start + size]

'''
Simpler version of above.
(start, size) stores the longest palindrome found so far.

We look for the longest palindrome that ends at end. To do this, we consider
the size of the longest palindrome found so far and do a palindrome check on
strings of size + 1 and size + 2 that end at end.
'''

if __name__ == '__main__':
    s = 'babad'
    print(longest_palindrome(s))

'''
Manacher's algorithm can be used to solve this problem in O(n) time.
'''