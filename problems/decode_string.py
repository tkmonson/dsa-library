'''
Decode String (#394)

Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside
the square brackets is being repeated exactly `k` times. Note that `k` is
guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white
spaces, square brackets are well-formed, etc. Furthermore, you may assume that
the original data does not contain any digits and that digits are only for
those repeat numbers, `k`. For example, there will not be input like `3a` or
`2[4]`. The length of the output will never exceed 10^5.
'''

def decode_string(s: str) -> str:
    n = len(s)
    L = R = 0
    stack = []
    result = []

    while L < n and R < n:
        if s[L] == ']':
            substring = stack.pop() * int(stack.pop())  # word * num
            if stack and not stack[-1].isnumeric():
                substring = stack.pop() + substring
            if stack:
                stack.append(substring)
            else:
                result.append(substring)

        elif '0' <= s[R] <= '9':
            while R < n and '0' <= s[R] <= '9':
                R += 1
            stack.append(s[L:R])
            R -= 1
            L = R
        
        elif 'a' <= s[R] <= 'z':
            while R < n and 'a' <= s[R] <= 'z':
                R += 1
            substring = s[L:R]
            if stack and not stack[-1].isnumeric():
                substring = stack.pop() + substring
            stack.append(substring)
            R -= 1
            L = R

        L += 1
        R += 1

    if stack:
        result.append(stack.pop())
    return ''.join(result)

'''
Parsing parentheses => stack

Lex substrings of digits into number tokens. Lex substrings of letters into
word tokens. The stack can contain number or word tokens.

Rule 1: The stack will never have two letter tokens in a row (e.g. ['3', 'abc',
'de]) because they can be concatenated into a single letter token. For example,
['3', 'abc', '1', 'de'] reduces to ['3', 'abcde'].

Rule 2: The stack will never contain just one word. The stack is for unresolved
terms; a single word can be sent to the result.

Ignore '[', but ']' means you should reduce the topmost term. Top will be a
word, next will be a number. After that, there may be a word to concatenate the
result with.
'''

def decode_string2(s: str) -> str:
    string_stack = []
    count_stack = []
    num = 0
    current = []

    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)

        elif ch == '[':
            count_stack.append(num)
            string_stack.append(current)
            current = []
            num = 0

        elif ch == ']':
            repeat = count_stack.pop()
            prev = string_stack.pop()
            prev.extend(current * repeat)
            current = prev

        else:
            current.append(ch)
    return ''.join(current)

'''
Another way of doing it. In this method, you maintain a current substring, put
it onto a stack of words whenever a new parenthetical starts, and pop it
whenever a parenthetical resolves.
'''

if __name__ == '__main__':
    s = '3[z]2[2[y]pq4[2[jk]e1[f]]]ef'
    print(decode_string(s))
