'''
Random Number Generator with No Repeats (from 03/24 Current interview)

Given a range [a, b], generate a number in this range randomly, but do not
repeat a number until all other numbers in the range have been generated first.
'''

from random import randint

class Generator:
    def __init__(self, a, b):
        if b < a:
            raise ValueError('b must be >= a')
        self.lst = list(range(a, b + 1))
        self.i = 0

    def next(self):
        if self.i == len(self.lst):
            self.i = 0
        j = randint(self.i, len(self.lst) - 1)
        self.lst[self.i], self.lst[j] = self.lst[j], self.lst[self.i]
        self.i += 1

        return self.lst[self.i - 1]

if __name__ == '__main__':
    g = Generator(1, 5)
    for _ in range(15):
        print(g.next())

