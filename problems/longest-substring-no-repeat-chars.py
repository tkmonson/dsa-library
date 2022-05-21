'''
Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating
characters.

-------------------------------------------------------------------------------

'''

def length_of_longest_substring(s: str) -> int:
    window = set()
    left = max_length = 0

    for right in range(len(s)):
        while s[right] in window:
            window.remove(s[left])
            left += 1
        window.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

