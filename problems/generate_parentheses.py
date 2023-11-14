'''
Generate Parentheses (#22)

Given `n` pairs of parentheses, generate all combinations of well-formed
parentheses.

E.g. 3 => ['((())))', '(()())', '(())()', '()(())', '()()()']
'''

from collections import deque

def generate_parentheses_two_stacks(n: int) -> list[str]:
    s1, s2 = [['(', 1]], []
    while len(s1[-1][0]) != 2 * n:
        while s1:
            a = s1.pop()
            if a[1] < n:
                s2.append([a[0] + '(', a[1] + 1])
            if a[1] > len(a[0]) - a[1]:
                s2.append([a[0] + ')', a[1]])
        s1, s2 = s2, s1

    return list(map(lambda x: x[0], s1))


def generate_parentheses_queue(n: int) -> list[str]:
    queue = deque([['(', 1]])
    while len(queue[0][0]) != 2 * n:
        a = queue.popleft()
        if a[1] < n:
            queue.append([a[0] + '(', a[1] + 1])
        if a[1] > len(a[0]) - a[1]:
            queue.append([a[0] + ')', a[1]])

    return list(map(lambda x: x[0], queue))


# More space-efficient during computation but slower
def generate_parentheses_recur(n: int) -> list[str]:
    result = []
    def dfs(s, left, right):
        if n == left == right:
            result.append(''.join(s))
            return
        if left < n:
            s.append('(')
            dfs(s, left + 1, right)
            s.pop()
        if right < left:
            s.append(')')
            dfs(s, left, right + 1)
            s.pop()

    dfs([], 0, 0)
    return result


if __name__ == '__main__':
    print(generate_parentheses_queue(16))

