'''
Basic Calculator (#224)

Given a string `s` representing a valid expression, implement a basic
calculator to evaluate it and return the result of the evaluation. `s` consists
of digits, `+`, `-`, `(`, `)`, and spaces. `s` represents a valid expression.
`-` can be used as a unary operator, but `+` cannot. There will be no two
consecutive operators in the input.
'''

# Faster
def calculate(s: str) -> int:
    calc = num = 0
    sign = 1
    stack = []

    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c in '+-':
            calc += sign * num
            num = 0
            sign = -1 if c == '-' else 1
        elif c == '(':
            stack.append(calc)
            stack.append(sign)
            sign = 1
            calc = 0
        elif c == ')':
            calc += sign * num
            num = 0
            calc *= stack.pop()
            calc += stack.pop()

    return calc + sign * num


def calculate2(s: str) -> int:
    s = s.replace(' ', '')
    stack = []

    i = 0
    while i < len(s):
        if s[i] == '+':
            i += 1
            continue

        j = i + 1
        is_num = False

        if s[i].isdigit():
            is_num = True
            while j < len(s) and s[j].isdigit():
                j += 1

        token = s[i : j]
        if token == ')':
            is_num = True
            token = 0
            while stack[-1] != '(':
                token += stack.pop()
            stack.pop()
        if is_num:
            token = int(token)
            if stack and stack[-1] == '-':
                stack.pop()
                if not stack or stack[-1] == '(':
                    token = -token
                else:
                    token = stack.pop() - token

        stack.append(token)
        i = j

    return sum(stack)

'''
All types of tokens are pushed to the stack, except '+' (we assume that
adjacent numbers in the stack will be added). Subtraction and negation
operations are evaluated ASAP, and the result is pushed to the stack. When a
')' is read, it is guaranteed that all elements in the stack before the
corresponding '(' are numbers, and we reduce the parenthetical expression by
adding them together and pushing the result to the stack.
'''

if __name__ == '__main__':
    s = '(1 + (-4 + 5 + 2) - 3) + (6 + 8)'
    s = '1 + 1'
    print(calculate(s))

