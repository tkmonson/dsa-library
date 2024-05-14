'''
Reverse Integer (#7)

Given a signed 32-bit integer `x`, return `x` with its digits reversed. If
reversing `x` causes the value to go outside the signed 32-bit integer range
`[-2^31, 2^31 - 1]`, then return 0. Assume the environment does not allow you
to store 64-bit integers (signed or unsigned). String conversion/manipulation
is not allowed.
'''

def reverse(x: int) -> int:
    limit = 147483647  # 2^31 - 1 without its most significant digit
    if (is_negative := x < 0):
        x = -x

    m = x % 10  # most significant digit of output
    x //= 10

    r = 0
    n = 0  # digit counter
    while x:
        r *= 10
        r += x % 10
        x //= 10
        n += 1

    # 32-bit integer overflow check
    if n == 9:
        if m > 2 or (m == 2 and r > limit):
            return 0

    r += m * 10 ** n

    return -r if is_negative else r

'''
The value of the least significant digit of a 10-digit input determines whether
the reversed integer can be represented in 32 bits. Save this digit, reverse
the rest of the integer without it. After reversing, you will know how many
digits the integer has. If it has 10 digits, the output may be 0 (invalid),
depending on the value of the saved digit. We must determine if the reversed
integer can be represented in 32 bits before attempting to do so because we
cannot store 64-bit integers.
'''

if __name__ == '__main__':
    x = 1137464807
    print(reverse(x))

