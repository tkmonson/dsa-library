'''
Edit Distance (#72)

Given two strings `a` and `b`, return the minimum number of operations required
to convert `a` to `b`.

You can perform three types of operations:
    * Insert a character
    * Delete a character
    * Replace a character
'''

from functools import cache

def edit_distance(a: str, b: str) -> int:
    @cache
    def dp(i, j):
        if i == len(a) or j == len(b):
            return (len(b) - j) + (len(a) - i)
        if a[i] == b[j]:
            return dp(i + 1, j + 1)
        return 1 + min([
            dp(i + 1, j + 1),  # replace in a
            dp(i, j + 1),      # insert in a
            dp(i + 1, j)       # delete in a
        ])
            
    return dp(0, 0)


if __name__ == '__main__':
    a = 'intention'
    b = 'execution'
    print(edit_distance(a, b))

'''
This problem could also be solved with a bottom-up algorithm.
'''

