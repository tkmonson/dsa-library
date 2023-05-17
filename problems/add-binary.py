'''
Add Binary (#67)

Given two binary strings, return their sum as a binary string.

'01' + '11' => '100'
'''

def add_binary(a: str, b: str) -> str:
    n = max(len(a), len(b))
    a, b = list(a.zfill(n)), list(b.zfill(n))

    carry = 0
    for i in range(n - 1, -1, -1):
        count = int(a[i]) + int(b[i]) + carry
        a[i] = str(count % 2)
        carry = int(count > 1)
    if carry:
        a = ['1'] + a

    return ''.join(a)


def add_binary2(a: str, b: str) -> str:
    s = []
    carry = 0
    i, j = len(a) - 1, len(b) - 1

    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            carry += int(a[i])
            i -= 1
        if j >= 0:
            carry += int(b[j])
            j -= 1
        s.append(str(carry % 2))
        carry //= 2
    
    return ''.join(s[::-1])


def add_binary3(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == '__main__':
    a = '1011'
    b = '1000'
    print(add_binary(a, b))

