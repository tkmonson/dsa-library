'''
Sum of Two Integers (#371)

Given two integers `a` and `b`, return their sum without using the binary `+`
or `-` operators. -1000 <= `a`, `b` <= 1000.
'''

def get_sum(a: int, b: int) -> int:
    N = 12
    a_neg, b_neg = a < 0, b < 0

    # Convert int to unsigned N-bit array
    a, b = bin(a)[3 if a_neg else 2:], bin(b)[3 if b_neg else 2:]
    a, b = a.zfill(N), b.zfill(N)
    a, b = [int(bit) for bit in a], [int(bit) for bit in b]

    def twos_comp(x):
        # Flip all bits
        for i in range(N):
            x[i] ^= 1

        # Add one
        for i in reversed(range(N)):
            if x[i] == 0:
                break
            x[i] = 0
        x[i] = 1

        return x

    if a_neg:
        a = twos_comp(a)
    if b_neg:
        b = twos_comp(b)

    # Add signed bit arrays
    carry = 0
    for i in reversed(range(N)):
        if a[i] & b[i] & carry:  # Three 1s
            a[i] = 1
        elif a[i] ^ b[i] ^ carry:  # One 1
            a[i] = 1
            carry = 0
        elif a[i] | b[i] | carry:  # Two 1s
            a[i] = 0
            carry = 1
        # Zero 1s, change nothing

    sign = 1
    if a[0]:  # result is negative, reverse two's complement
        sign = -1  # this `-` character is allowed; it is unary, not binary
        for i in reversed(range(N)):
            if a[i] == 1:
                break
            a[i] = 1
        a[i] = 0
        for i in range(N):
            a[i] ^= 1

    a = ''.join([str(bit) for bit in a])
    return sign * int(a, 2)


if __name__ == '__main__':
    a = -8
    b = -12
    print(get_sum(a, b))

'''
It is significant that a and b range from only -1000 to 1000. The greatest
possible sum is 2000 (11 bits) and the least possible sum is -2000 (12 bits in
two's complement representation). Two's complement numbers (negatives) have
identical addition and subtraction operations to those of unsigned binary
numbers (positives), as long as the inputs have the same bit length as the
output. So let's work with 12-bit numbers.

Convert ints to 12-bit arrays, with any negative ints represented in two's
complement. Now we need to add these bit arrays together without the addition
operator. There are three bits involved in each addition step: the a bit, the
b bit, and the carry. The current place value and the value of the future carry
are determined by how many of these bits have a value of 1:

    3 1s (A & B & C = 1) => place = 1, carry = 1
    1 1s (A ^ B ^ C = 1) => place = 1, carry = 0
    2 1s (A | B | C = 1) => place = 0, carry = 1
    0 1s (A | B | C = 0) => place = 0, carry = 0

Once the result is found, if it is negative, convert from two's complement to
unsigned. Convert from 12-bit array to int and multiply by -1 if the result is
negative.
'''

