'''
Valid Palindrome (#125)

A string is a palindrome if, after converting all uppercase letters to
lowercase letters and removing all non-alphanumeric characters, it reads the
same forward and backward. Given a string, return True if it is a palindrome or
False otherwise.
'''

from re import sub

# Time: O(n)
# Auxiliary space: O(n)
def is_palindrome(s: str) -> bool:
    # slower: [i for i in s.lower() if i.isalnum()]
    s = sub('[^a-z0-9]', '', s.lower())
    for i in range(len(s) // 2):
        if s[i] != s[~i]:
            return False
    return True


# Time: O(n)
# Auxiliary space: O(1)
def is_palindrome2(s: str) -> bool:
    i, j = 0, len(s) - 1
    while i < j:
        a, b = s[i].lower(), s[j].lower()
        if a.isalnum() and b.isalnum():
            if a != b:
                return False
            i, j = i + 1, j - 1
            continue
        i, j = i + (not a.isalnum()), j - (not b.isalnum())
    return True


if __name__ == '__main__':
    s = 'A man, a plan, a canal: Panama'
    print(is_palindrome2(s))

