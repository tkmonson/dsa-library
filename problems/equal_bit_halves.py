# Find all the n-digit binary strings with an equal sum of bits in their two halves. The strings cannot start with 0.

# Input: 6
# Output: ['100001', '100010', '100100', '110011', '110101', '110110',
#          '101011', '101101', '101110', '111111']

# If n is odd, the middle bit can be 0 or 1 (it's not a part of the left and right sides).

def equal_bit_halves(n):
    result = []
    def helper(left, right, diff, n):
        if n and (2 * abs(diff) <= n):
            if n == 1:
                helper(left + '0', right, diff, 0)
                helper(left + '1', right, diff, 0)
                return

            if left != "":
                helper(left + '0', right + '0', diff, n - 2)
                helper(left + '0', right + '1', diff + 1, n - 2)

            helper(left + '1', right + '0', diff - 1, n - 2)
            helper(left + '1', right + '1', diff, n - 2)

        elif n == 0 and diff == 0:
            result.append(left + right)

    helper("", "", 0, n)
    return result

n = 6
print(equal_bit_halves(n))
