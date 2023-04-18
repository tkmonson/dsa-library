'''
String to Integer (#8)

Write an algorithm that converts a string of letters, digits, spaces, '+'s,
'-'s, and '.'s to a 32-bit signed integer according to the following steps:

    1. Ignore any leading whitespace.
    2. Check if the next character is '-' or '+'. This determines if the final
       result is negative or positive respectively. Assume the result is
       positive if neither is present.
    3. Read characters until a non-digit character is read or the end of the
       input is reached. Ignore the rest of the string. Convert this digit
       string into its integer representation. If the string contains no
       digits, return 0.
    4. If the integer is less than -2^31, return -2^31. If it is greater than
       2^31 - 1, return 2^31 - 1.
'''

def atoi(s: str) -> int:
    s = s.strip()
    i, nstr = 0, ''
    try:
        if s[i] in ('-', '+'):
            nstr += s[i]
            i += 1
        while s[i].isdigit():
            nstr += s[i]
            i += 1
    except(IndexError):
        pass

    try:
        return min(max(int(nstr), -2147483648), 2147483647)
    except(ValueError):
        return 0


if __name__ == '__main__':
    s = '    -42 blah blah'
    print(atoi(s))

