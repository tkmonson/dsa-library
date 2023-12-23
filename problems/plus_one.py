'''
Plus One (#66)

You are given an integer represented as an integer array `digits`, where each
`digits[i]` is the ith digit of the integer. The digits are ordered from most
significant to least significant in left-to-right order. There are no leading
zeros. Increment the integer by one and return the resulting array of digits.
'''

def plus_one(digits: list[int]) -> list[int]:
    i = -1
    try:
        while digits[i] == 9:
            digits[i] = 0
            i -= 1
    except IndexError:
        digits = [1] + digits
        return digits

    digits[i] += 1
    return digits


if __name__ == '__main__':
    digits = [1, 9, 9]
    print(plus_one(digits))

