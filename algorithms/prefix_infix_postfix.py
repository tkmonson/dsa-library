'''
Binary operations have a choice of where the operator is positioned in the
expression. There are three notations: prefix (+AB), infix (A+B), and postfix
(AB+). The functions below convert string representations of arithmetic
expressions from one notation to another.

Prefix and postfix notation have an advantage over infix notation in that they
do not require parentheses to specify operator precedence.

These notations correspond to preorder, inorder, and postorder traversals of
abstract syntax trees. Just as a unique tree may be constructed from its
inorder traversal combined with either its preorder or postorder traversal, the
unique structure of an arithmetic expression, represented by an AST, may be
constructed from an infix string combined with either its prefix or postfix
equivalent.

Prefix and postfix notation are also known as Polish and Reverse Polish
notation, respectively.
'''

def polish_parse(expression, conversion_format):
    stack = []
    for ch in expression:
        if is_operator(ch):
            operand1 = stack.pop()
            operand2 = stack.pop()
            temp = conversion_format(operand1, operand2, ch)
            stack.append(temp)
        else:
            stack.append(ch)
    return stack[-1]


def postfix2prefix(expression):
    return polish_parse(expression, lambda a, b, op: op + b + a)


def prefix2postfix(expression):
    expression = expression[::-1]
    return polish_parse(expression, lambda a, b, op: a + b + op)


def postfix2infix(expression):
    return polish_parse(expression, lambda a, b, op: '(' + b + op + a + ')')


def prefix2infix(expression):
    expression = expression[::-1]
    return polish_parse(expression, lambda a, b, op: '(' + a + op + b + ')')

'''
When parsing left-to-right, postfix input is natural because the operands come
first, and the operator denotes the end of the group. Prefix input is natural
for right-to-left parsing, but it must be reversed here to comply with the
direction of the loop.
'''

def shunting_yard(expression, assoc):
    stack = []
    out = []

    for ch in expression:
        if is_operator(ch):
            while (stack
                and stack[-1] != '('
                and (precedence(stack[-1]) > precedence(ch) or
                    (precedence(stack[-1]) == precedence(ch) and assoc(ch)))):
                out.append(stack.pop())
            stack.append(ch)
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack: 
                if stack[-1] == '(':
                    stack.pop()
                    break
                out.append(stack.pop())
        else:    # ch is operand
            out.append(ch)
    while stack:
        out.append(stack.pop())
    return ''.join(out)


def infix2postfix(expression):
    return shunting_yard(expression, lambda op: op != '^')


def infix2prefix(expression):
    expression = mirror(expression)
    return shunting_yard(expression, lambda op: op == '^')[::-1]

'''
Converting from infix to either prefix or postfix requires the use of the
shunting-yard algorithm, named after railroad yards where cars are detached,
one-by-one, from a train and switched onto different tracks so that they can be
grouped and sorted by destination before the train's departure. In this case,
operands continue on the track, and operators are sent to the shunting-yard
(stack), where they are grouped and released back to the track based on
precedence.

Because humans typically prefer infix and computers are more efficient using
postfix, the shunting-yard algorithm was influential in the development of
early instruction set architectures. Because it inputs infix and outputs either
prefix or postfix, the algorithm can also be modified to produce abstract
syntax trees.

When parsing infix input, one must be mindful of operator associativity. In
mathematics, + and * are (fully) associative, and, in programming, they are
traditionally evaluated as left-associative; - and / are left-associative; ^ is
right-associative. This means that A^B^C is parsed as A^(B^C), which is a
special case.

When parsing infix input, you will always read a ( or an operand first. Postfix
output is natural because operands can be enqueued without waiting for a
potential higher-precedence operator farther down the string. For prefix
output, the infix input must be mirrored, processed (with the
left-associativity check swapped for right-), and reversed.
'''

def is_operator(ch):
    return ch in ('+', '-', '*', '/', '^')


def precedence(operator):
    if operator == '^': return 2
    if operator in ('*', '/'): return 1
    if operator in ('+', '-'): return 0
    return -1


def mirror(expression):
    out = []
    expression = expression[::-1]
    for ch in expression:
        if ch == '(':
            ch = ')'
        elif ch == ')':
            ch = '('
        out.append(ch)
    return ''.join(out)


if __name__ == '__main__':
    prefix = "+A/*BC^-DE^FG"
    infix = "A+B*C/(D-E)^F^G"
    postfix = "ABC*DE-FG^^/+"
    
    print(f"post2pre: {postfix} --> {postfix2prefix(postfix)}")
    print(f"pre2post: {prefix} --> {prefix2postfix(prefix)}")
    print(f"post2in:  {postfix} --> {postfix2infix(postfix)}")
    print(f"pre2in:   {prefix} --> {prefix2infix(prefix)}")
    print(f"in2post:  {infix} --> {infix2postfix(infix)}")
    print(f"in2pre:   {infix} --> {infix2prefix(infix)}")

