'''
Pow(x, n) (#50)

Implement `pow(x, n)`, which calculates `x` raised to the power `n`.
'''

def pow(x: float, n: int):
    neg = False
    if n < 0:
        neg = True
        n = -n

    def f(x, n):
        if n == 0:
            return 1
        half = f(x, n // 2)
        if n % 2:
            return half * half * x
        else:
            return half * half

    return 1 / f(x, n) if neg else f(x, n)

'''
The naive way to calculate x^n is to multiply x n times. But this is slow for
large n. Instead, you can use the property of powers:

x^n = x^(n/2) * x^(n/2)
'''

if __name__ == '__main__':
    x = 1.000000001
    n = 2147483647
    print(pow(x, n))
