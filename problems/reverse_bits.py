'''
Reverse Bits (#190)

Given a 32-bit unsigned integer, reverse its bits and return the resulting
integer.
'''

def reverse_bits(n: int) -> int:
    result = 0
    for i in range(32):
        if n & 1:
            result += 1 << (31 - i)
        n >>= 1
    return result


def reverse_bits2(n: int) -> int:
    result = 0
    for _ in range(32):
        result = (result << 1) + (n & 1)
        n >>= 1
    return result


def reverse_bits3(n: int) -> int:
    n = bin(n)[2:]
    n = '0' * (32 - len(n)) + n
    return int(n[::-1], 2)


if __name__ == '__main__':
    n = 10
    r = reverse_bits(n)
    print(r)
    print(bin(r)[2:])

