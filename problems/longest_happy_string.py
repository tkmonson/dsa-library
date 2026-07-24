'''
Longest Happy String (#1405)

A string `s` is called happy if it satisfies the following conditions:

    * `s` only contains the letters 'a', 'b', and 'c'.
    * `s` does not contain any of "aaa", "bbb", or "ccc" as a substring.
    * `s` contains at most a occurrences of the letter 'a'.
    * `s` contains at most b occurrences of the letter 'b'.
    * `s` contains at most c occurrences of the letter 'c'.

Given three integers `a`, `b`, and `c`, return the longest possible happy
string. If there are multiple longest happy strings, return any of them. If
there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.
'''

from contextlib import suppress

# Time: O(a + b + c)
# Auxiliary space: O(a + b + c)
def longest_happy_string(a: int, b: int, c: int) -> str:
    ans = []
    while True:
        char_set = set([(a, 'a'), (b, 'b'), (c, 'c')])
        limit, char = max(char_set)

        with suppress(IndexError):
            if char == ans[-1] == ans[-2]:
                limit, char = max(char_set - set([(limit, char)]))

        if limit == 0:
            break

        ans.append(char)

        if ans[-1] == 'a':
            a -= 1
        elif ans[-1] == 'b':
            b -= 1
        else:
            c -= 1
        
    return ''.join(ans)

'''
To make the longest string possible, you want to have the remaining limit for
each character be as close as possible, so you don't have a excess for a single
character that can't be used, due to the "no three in a row" rule (e.g.
ideally, by the end, you are printing characters like "abcabcabc").

To do this, choose the character with the largest remaining limit, unless that
character was chosen the last two times, in which case choose the character
with the second largest remaining limit. Repeat until you have no characters
remaining or the only characters remaining would violate the "no three in a
row" rule.
'''

if __name__ == '__main__':
    a = 1
    b = 1
    c = 7
    print(longest_happy_string(a, b, c))
