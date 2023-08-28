'''
Evaluate Reverse Polish Notation (#150)

Given an array of string tokens that represents an arithmetic expression in
Reverse Polish Notation, evaluate the expression and return the integer that
represents the value of the expression. The valid operators are '+', '-', '*',
and '/', each operand is an integer or another expression, and the division of
two integers always truncates toward zero.
'''

def evalRPN(tokens: list[str]) -> int:
    stack = []
    operators = {'+', '-', '*', '/'}
    for token in tokens:
        if token in operators:
            op2, op1 = int(stack.pop()), int(stack.pop())
            if token == '+':
                result = op1 + op2
            if token == '-':
                result = op1 - op2
            if token == '*':
                result = op1 * op2
            if token == '/':
                result = int(op1 / op2)
            stack.append(result)
        else:
            stack.append(token)
    return int(stack.pop())


if __name__ == '__main__':
    tokens = ['10', '6' , '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5',
              '+']
    print(evalRPN(tokens))

