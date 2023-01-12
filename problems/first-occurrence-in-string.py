'''
Find the Index of the First Occurrence in a String (#28)

Given two strings needle and haystack, return the index of the first occurrence
of needle in haystack, or -1 if needle is not part of haystack.
'''

def strStr4(haystack: str, needle: str) -> int:
    if needle not in haystack: return -1
    return haystack.index(needle) if needle else 0

def strStr3(haystack: str, needle: str) -> int:
    i = 0
    while i <= len(haystack) - len(needle):
        if haystack[i] == needle[0]:
            isMatch = True
            for j in range(0, len(needle)):
                if haystack[i + j] != needle[j]:
                    isMatch = False
            if isMatch:
                return i
        i = i + 1
    return -1

def strStr2(haystack: str, needle: str) -> int:
    i = 0
    while i <= len(haystack) - len(needle):
        if haystack[i] == needle[0]:
            if haystack[i : i + len(needle)] == needle:
                return i
        i = i + 1
    return -1

# INCORRECT
def strStr1(haystack: str, needle: str) -> int:
    i = 0
    while i <= len(haystack) - len(needle):
        if haystack[i] == needle[0]:
            if haystack[i : i + len(needle)] == needle:
                return i
            i = i + len(needle) - 1
        i = i + 1
    return -1


if __name__ == '__main__':
    print(strStr4('thehorriblehorseishappy', 'horse'))
    print(strStr4('grandfather', 'dog'))

'''
Need to shoot for O(n) time.

The algorithm can be solved by using two pointers when checking for a match or
by directly comparing needle to a substring of haystack with the same length as
needle, but the latter method is less space-efficient. When using the latter
method, you cannot move i forward by len(needle) after a match is not found
because a future match may begin within that previously checked pattern.

You can also use Python's built-in methods to write a short, fast algorithm,
but that almost feels like cheating...

This problem is an excellent opportunity to implement the Rabin-Karp algorithm,
which is a string-searching algorithm that computes a rolling hash for each
substring with length equal to that of the target pattern. If this hash is
equal to the hash of the target, the algorithm performs an exact comparison.
'''

