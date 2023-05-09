'''
Letter Combinations of a Phone Number (#17)

Given a string containing digits from 2-9 inclusive, return, in any order, all
possible letter combinations that the number could represent, according to the
standardized mapping of digits to letters as seen on telephone keypads:

    2: abc, 3: def, 4: ghi, 5: jkl, 6: mno, 7: pqrs, 8: tuv, 9: wxyz
'''

from collections import deque
from itertools import product

def letter_combinations(digits: str) -> list[str]:
    if not digits:
        return []

    letters = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    combs = deque([''])
    for digit in digits:
        n = len(combs)
        for _ in range(n):
            comb = combs[0]
            for letter in letters[digit]:
                combs.append(comb + letter)
            combs.popleft()

    return combs


def letter_combinations2(digits: str) -> list[str]:
    if not digits:
        return []

    letters = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    combs = []
    def backtrack(comb):
        if (i := len(comb)) == len(digits):
            combs.append(comb)
            return
        for letter in letters[digits[i]]:
            backtrack(comb + letter)

    backtrack('')
    return combs


def letter_combinations3(digits: str) -> list[str]:
    if not digits:
        return []

    letters = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    a = [letters[d] for d in digits]
    return list(map(''.join, product(*a)))


if __name__ == '__main__':
    digits = '23'
    print(letter_combinations3(digits))

