'''
Longest Palindrome (#409)

Given a string of letters, return the length of the longest palindrome that can
be built with those letters. Letters are case-sensitive.
'''

from collections import Counter

def longest_palindrome(s: str) -> int:
    length, has_odd = 0, False
    count = Counter(s)
    for v in count.values():
        if not has_odd and v % 2:
            has_odd = True
        length += v - v % 2
    return length + has_odd


def longest_palindrome2(s: str) -> int:
    odd_count = 0
    count = Counter(s)
    for v in count.values():
        odd_count += v % 2
    return len(s) - odd_count + (1 if odd_count else 0)

