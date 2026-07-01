'''
Integer Break (#343)

Given an integer n, break it into the sum of k positive integers, where k >= 2,
and maximize the product of those integers.

Return the maximum product you can get.

2 <= n <= 58
'''

# Time: O(1)
# Auxiliary space: O(1)
def integer_break(n: int) -> int:
    if n == 2:
        return 1
    if n == 3:
        return 2

    threes = n // 3
    remainder = n % 3

    if remainder == 1:
        threes -= 1
        remainder = 4
    if remainder == 0:
        remainder = 1

    return 3 ** threes * remainder

'''
What number should be subtracted from n?
Not 1, multiplying by one does not increase the product.
Not 5 or greater, 5 = 2 + 3, 2 * 3 = 6.
4 is just 2 + 2, so same as choosing 2.
So the answer is either 2 or 3.
2 * 2 * 2 = 8, 3 * 3 = 9 => you should never have more than 2 2s.
So 3 is optimal, you want the maximum number of 3s.
'''

# Time: O(1)
# Auxiliary space: O(1)
def integer_break2(n: int) -> int:
    max_product = 0
    product = 1
    k = 2
    while max_product < product:
        max_product = product
        a = n // k
        b = n % k
        product = ((a + 1) ** b) * (a ** (k - b))
        k += 1

    return max_product

'''
Product is maximized if operands are as close in value as possible.
As k increases, product will peak and then decrease.
The max product occurs right before the first decrease.
'''

if __name__ == '__main__':
    n = 10
    print(integer_break(n))
