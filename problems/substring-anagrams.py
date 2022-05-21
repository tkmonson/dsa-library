'''
Substring Anagrams

Two strings are anagrams of each other if the letters of one string can be
rearranged to form the other string. Given a string, find the number of pairs
of substrings of the string that are anagrams of each other.

-------------------------------------------------------------------------------

1. Find all possible substrings.
2. Sort characters of each substring alphabetically (anagrams are now equal).
3. Count occurrences of sorted substrings.
4. If a substring occurs k times, then there are 1 + 2 + 3 + ... + (k - 1)
   anagram pairs of that substring. Return the sum of the number of pairs for
   each substring.
'''

from collections import Counter

def substring_anagrams(s: str) -> int:
    sorted_substrings = []
    for length in range(1, len(s)):
        for start in range(0, len(s) - length + 1):
            sorted_substrings.append(''.join(sorted(s[start:start+length])))
    count = Counter(sorted_substrings)
    return sum(sum(range(i)) for i in count.values())

