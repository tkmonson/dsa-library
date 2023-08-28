'''
Implement Queue using Stacks (#232)

Implement a queue using only two stacks. Use only the standard stack
operations: push to top, pop from top, peek at top, and is empty.
'''

class MyQueue:
    def __init__(self):
        self._push_stack = []
        self._pop_stack = []

    def push(self, x: int) -> None:
        self._push_stack.append(x)

    def pop(self) -> int:
        self.peek()
        return self._pop_stack.pop()

    def peek(self) -> int:
        if not self._pop_stack:
            while self._push_stack:
                self._pop_stack.append(self._push_stack.pop())
        return self._pop_stack[-1]

    def empty(self) -> bool:
        return not self._push_stack and not self._pop_stack

'''
You only have to move all of the elements from _push_stack to _pop_stack when
pop is called and _pop_stack is empty. Otherwise, push elements to _push_stack
and pop elements from _pop_stack.
'''

