'''
Multiply Strings (#43)

Given two non-negative integers represented as strings, return their product,
also represented as a string. You cannot convert the inputs to integers
directly.
'''

# Time: O(n + m)
# Auxiliary space: O(1)
def multiply(num1: str, num2: str) -> str:
    d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
         '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    a = 0
    for x in num1:
        a = a * 10 + d[x]

    b = 0
    for x in num2:
        b = b * 10 + d[x]

    return str(a * b)


# Time: O(n * m)
# Auxiliary space: O(1)
def multiply2(num1: str, num2: str) -> str:
    d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
         '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    count1, count2 = 1, 1
    product = 0
    for i in range(-1, -len(num1) - 1, -1):
        for j in range(-1, -len(num2) - 1, -1):
            product += d[num1[i]] * count1 * d[num2[j]] * count2
            count2 *= 10
        count1 *= 10
        count2 = 1

    return str(product)


if __name__ == '__main__':
    print(multiply('23', '45'))

