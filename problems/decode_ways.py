'''
Decode Ways (#91)

A message can be encoded with the following mapping:

'A' -> '1'
'B' -> '2'
...
'Z' -> '26'

To decode an encoded message, all the digits must be grouped and mapped back
into letters using the reverse of the mapping. There may be multiple ways to
group the letters. For example, '11106' can be mapped to 'AAJF' with the
grouping (1, 1, 10, 6) or 'KJF' with the grouping (11, 10, 6). Note that the
grouping (1, 11, 06) is invalid because '06' does not exist in the mapping.

Given a string containing only digits, return the number of ways to decode it.
'''

from contextlib import suppress
from functools import cache

# Time: O(n)
# Auxiliary space: O(1)
def num_decodings_tabu(s: str) -> int:
    cache = [1, 0]
    for i in range(len(s) - 1, -1, -1):
        temp = cache[0]
        if s[i] != '0':
            if int(s[i:i + 2]) < 27:
                cache[0] += cache[1]
        else:
            cache[0] = 0
        cache[1] = temp

    return cache[0]


# Time: O(n)
# Auxiliary space: O(n)
def num_decodings_memo(s: str) -> int:
    @cache
    def f(i):
        with suppress(IndexError):
            if s[i] == '0':
                return 0
        if i >= len(s) - 1:
            return 1

        ways = f(i + 1)
        if int(s[i:i + 2]) < 27:
            ways += f(i + 2)

        return ways

    return f(0)


# Time: O(n)
# Auxiliary space: O(n)
@cache
def num_decodings_memo2(s: str) -> int:
    with suppress(IndexError):
        if s[0] == '0':
            return 0
    if len(s) <= 1:
        return 1

    ways = num_decodings_memo(s[1:])
    if int(s[:2]) < 27:
        ways += num_decodings_memo(s[2:])

    return ways

'''
This memoization function uses direct recursion, but it is slower than the
above helper-method memoization function because it must create a string slice
as an input for each recursive call.
'''

if __name__ == '__main__':
    s = '226'
    print(num_decodings_tabu(s))

'''
Starting from the smallest substring (s[-1:]), prepend a digit one at a time.

Given a substring s and a function f(s) that gives the number of ways that s
can be decoded:
    s[0] is 0 => f(s) is 0
    Can consider s[0] as a 1-digit group => f(s) includes f(s[1:]) ways
    Can consider s[:2] as a 2-digit group => f(s) includes f(s[2:]) ways

The functions assume that the string expands from right to left, but you could
just as easily write implementations where it expands from left to right.
'''

