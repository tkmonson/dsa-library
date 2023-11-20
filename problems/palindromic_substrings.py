'''
Palindromic Substrings (#647)

Given a string, return the number of palindromic substrings in it.
'''

def count_substrings(s: str) -> int:
    n = len(s)
    count = 0
    for i in range(n):
        for left, right in [[i, i], [i, i + 1]]:
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
    return count

'''
is_palim(s) = (s[0] == s[-1]) and is_palim(s[1:-1])
'''

if __name__ == '__main__':
    s = 'aaa'
    print(count_substrings2(s))

