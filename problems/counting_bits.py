'''
Counting Bits (#338)

Given an integer `n`, return an array `a` of length `n + 1` such that for each
`i`, where `0 <= i <= n`, `a[i]` is the number of 1s in the binary
representation of `i`.
'''

# Time: O(n)
# Auxiliary space: O(1)
def count_bits(n: int) -> list[int]:
    a = [0]
    i = 0
    for _ in range(n):
        a.append(a[i] + 1)
        i += 1
        if i == (len(a) + 1) >> 1:  # >> 1 == // 2
            i = 0

    return a

'''
1000 (8) is the 9th unsigned binary integer. The 8 integers that come before it
can be represented with 3 or fewer bits; they can be stored within the 0s of
1000. Thus, for a = [000, ..., 111] and b = [1000, ..., 1111],
num_1s(b[i]) = num_1s(a[i]) + 1. So when the bit length of the numbers you are
appending increases, set i to 0. Append a[i] + 1, increment i, and repeat.
'''

# Time: O(n)
# Auxiliary space: O(1)
def count_bits2(n: int) -> list[int]:
    a = [0] * (n + 1)
    for i in range(1, n + 1):
        a[i] = a[i >> 1] + (i & 1)
    return a

'''
If you're processing an integer of bit length n, you already have access to the
Hamming weights of all integers of bit length n - 1. So shift your integer
right, get the Hamming weight of the result, and then add 1 if the bit you
eliminated during the shift was a 1.
'''

# Time: O(nlogn)
# Auxiliary space: O(1)
def count_bits3(n: int) -> list[int]:
    return [bin(i).count('1') for i in range(n + 1)]


if __name__ == '__main__':
    n = 16
    print(count_bits(n))

