'''
Design Spreadsheet (from 03/24 January interview)

Design a spreadsheet application. Some values in the spreadsheet are numbers
(e.g. '5'), some values are formulas (e.g. 'A1', 'A2+B1'). Formulas only
support the addition operator. Formulas can reference other formulas.
References are always a letter plus a number.

For example,

          A        B
      |-----------------|
    1 |   3    | A1 + 5 |
      |-----------------|
    2 | B1 + 3 |        |
      |_________________|

evaluates to:

          A        B
      |-----------------|
    1 |   3    |   8    |
      |-----------------|
    2 |   11   |        |
      |_________________|

But if A1 changes, then:

          A        B
      |-----------------|
    1 |   0    |   5    |
      |-----------------|
    2 |   8    |        |
      |_________________|

Implement get and set methods for this behavior.
'''

class Table:
    def __init__(self):
        self.table = {}

    def get(self, ref: str) -> int:
        ops = self.table[ref].split('+')
        for i in range(len(ops)):
            op = ops[i]
            try:
                ops[i] = int(op)
            except ValueError:
                ops[i] = self.get(op)
        return sum(ops)

    def set(self, ref: str, val: str) -> None:
        self.table[ref] = val


if __name__ == '__main__':
    t = Table()
    t.set('A1', '2')
    t.set('A2', '3')
    t.set('B1', 'A1+A2')
    t.set('B2', 'B1+A1')
    print(t.get('B1'))
    print(t.get('B2'))
    t.set('A2', '0')
    print(t.get('B2'))

'''
References can point to references, which can point to references, which can
point to references... But eventually a reference needs to point to a number.
The number is the base case of a recursive stack.
'''

