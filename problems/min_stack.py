'''
Min Stack (#155)

Design a stack that supports constant time push, pop, top, and get_min
operations.
'''

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        try:
            self.stack.append((val, min(val, self.stack[-1][1])))
        except(IndexError):
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def get_min(self) -> int:
        return self.stack[-1][1]

'''
Initially, I thought to store the elements in a stack and a heap, to take
advantage of the heap's O(1) get_min operation. The problem with that is
that updating the heap after a MinStack.pop operation is not O(1). This
solution instead stores the min element of a substack within that substack's
top element.
'''

class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.minstack[-1]

'''
This solution eliminates the storage of redundant min element data. As the
stack grows, the min element is not stored for every substack in the stack; it
is stored only when it changes (or when an element equal to it is pushed).
'''

