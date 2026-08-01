'''
Bitwise AND of Numbers Range (#201)

Given two integers left and right that represent the range [left, right],
return the bitwise AND of all numbers in this range, inclusive.
'''

# Time: O(1)
# Auxiliary space: O(1)
def range_bitwise_and(left: int, right: int) -> int:
    while left < right:
        right &= right - 1
    return right

'''
This is Brian Kernighan's algorithm. Similar to below, but relies on the fact
that n & (n - 1) zeros out the rightmost bit of n.
'''

# Time: O(1)
# Auxiliary space: O(1)
def range_bitwise_and2(left: int, right: int) -> int:
    c = 0
    while left != right:
        left >>= 1
        right >>= 1
        c += 1
    return left << c

'''
This finds a common prefix by right shifting the top and bottom of the range.

As you increment starting from any number, you will eventually have a string of
1s starting at the LSB and a 0 to the left of it. When you increment by one
from here, the 1s will become 0s and the 0 will become a 1: e.g. 0111 -> 1000.

The AND of these sections is 0. So you can consider, as you are incrementing
over a large range of numbers, the AND of all of them is progressively zeroing
out from right to left, leaving only the MSBs.

You know that the AND must have the bits that left and right share that are not
zeroed out by the numbers in between. Thus, you can just zero out the LSBs in
left and right by right shifting them until they are equal and left shifting
the zeros back into them.
'''

if __name__ == '__main__':
    print(range_bitwise_and(48, 51))
