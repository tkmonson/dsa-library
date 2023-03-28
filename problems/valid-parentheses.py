'''
Valid Parentheses (#20)

Given a string containing only the characters '(', '[', '{', ')', ']', and '}',
determine if the string is valid. The string is valid if:
    1. Open brackets are closed by the same type of brackets
    2. Open brackets are closed in the correct order
    3. Every close bracket has a corresponding open bracket of the same type
'''

def is_valid(s: str) -> bool:
    stack = []
    p_map = {'(': ')', '[': ']', '{': '}'}
    for p in s:
        if p in p_map:
            stack.append(p)
        else:
            try:
                if p != p_map[stack.pop()]:
                    return False
            except(IndexError):
                return False

    return len(stack) == 0

