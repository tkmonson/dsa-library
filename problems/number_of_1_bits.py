'''
Number of 1 Bits (#191)

Given an integer, return the number of `1` bits that its binary representation
has (also known as its Hamming weight).
'''

def hamming_weight(n: int) -> int:
    weight = 0
    while n:
        n &= (n - 1)
        weight += 1
    return weight

'''
To transform an integer n into (n - 1), you can flip the rightmost block of 0s
to 1s and flip the rightmost 1 to a 0. Thus, n & (n - 1) will be the same as n
but with the rightmost 1 flipped to a zero. Perform n &= (n - 1) repeatedly,
flipping one bit at a time, until n == 0.
'''

def hamming_weight2(n: int) -> int:
    weight = 0
    while n:
        if n & 1:
            weight += 1
        n >>= 1
    return count

'''
Shift bits to the right, increment the count whenever the rightmost bit is a 1.
'''

if __name__ == '__main__':
    n = 12383
    print(f'{bin(n)} has {hamming_weight(n)} 1s')

'''
Production implementations of the Hamming weight operation are faster and more
complicated than the implementations given above.
'''
