'''
Minimum Array End (#3133)

You are given two integers `n` and `x`. You have to construct an array of
positive integers `nums` of size `n` where for every `0 <= i < n - 1`,
`nums[i + 1]` is greater than `nums[i]`, and the result of the bitwise AND
operation between all elements of nums is `x`.

Return the minimum possible value of `nums[n - 1]`.
'''

# Time: O(logn) (iterating over bits instead of values)
# Auxiliary space: O(1)
def min_end(n: int, x: int) -> int:
    res = x
    i_x, i_n = 1, 1

    while i_n <= n - 1:
        if i_x & res == 0:
            if i_n & (n - 1):
                res |= i_x
            i_n <<= 1
        i_x <<= 1

    return res

'''
If x = 010101 (21), then the next numbers in the sequence will be:
010111, 011101, 011111, 110101, 110111, 111101, 111111, ...

All numbers in the sequence need to have the same 1 bits as x, so ignore those
bits. Only the 0s in x can change.

Consider the 0s in x to be their own binary number that starts at 0. As you
increment it, x increases. This produces the numbers in the sequence.

Let # be an operator such that, for a # b, the bits of b are "merged" into the
0 bits of a.

010101 # 001 = 010111, 010101 # 010 = 011101, 010101 # 011, 011111, ...

So the function should return x # (n - 1). To implement this, create two
"pointers", one for x, one for (n - 1). i_x checks if the current position in
x has a 0, i_n checks if the current position in (n - 1) has a 1. If both are
true, put a 1 into x's current position. Shift the pointers right to left.
'''

# Time: O(n)
# Auxiliary space: O(1)
def min_end2(n: int, x: int) -> int:
    res = x

    for _ in range(n - 1):
        res += 1
        res |= x

    return res

'''
Array must be strictly increasing
a & b & c & ... = x

=> a, b, c, ... must have the same "set" bits as x
=> a must equal x (in order to minimize the (n-1)th element)

How can we ensure that b, c, d, ... all have the same "set" bits as x?
By incrementing from x and ORing each number with x.

x = 101
101 | 110 = 111, 101 | 1000 = 1101, 101 | 1111 = 1111, 101 | 10000 = 10101, ...

Do this increment and OR operation n - 1 times, starting with x.
'''
