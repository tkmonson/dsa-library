'''
Valid Anagram (#242)

Given two strings `s` and `t`, return True if `t` is an anagram of `s` or False
otherwise. An anagram is a word or phrase formed by rearranging the letters of
a different word or phrase.
'''

from collections import defaultdict

# For an alphabet of only lowercase letters
def is_anagram(s: str, t: str) -> bool:
    if (n := len(s)) != len(t):
        return False

    a = [0] * 26
    for i in range(n):
        a[ord(s[i]) - ord('a')] += 1
        a[ord(t[i]) - ord('a')] -= 1
    for n in a:
        if n != 0:
            return False
    return True


# For an alphabet of any characters
def is_anagram2(s: str, t: str) -> bool:
    if (n := len(s)) != len(t):
        return False

    d = defaultdict(lambda: 0)
    for i in range(n):
        d[s[i]] += 1
        d[t[i]] -= 1
    for n in d.values():
        if n != 0:
            return False
    return True

