'''
Add Two Numbers (#2)

Given two numbers that are represented by linked lists, where each node
contains a single digit and the digits are stored in reverse order (i.e. the
ones digit is stored at the head of the list), return the sum of the two
numbers as a linked list, with the digits in reverse order.

E.g. 617 + 295 = 912 => (7 -> 1 -> 6) + (5 -> 9 -> 2) = (2 -> 1 -> 9)
'''

'''
IN NEED OF UPDATE
'''

class Node:
    def __init__(self, value=None):
        self.val = value
        self.next = None

def add_lists(h1: Node, h2: Node) -> Node:
    if h1 is None and h2 is None:
        return None
    if h1 is None:
        return h2
    if h2 is None:
        return h1

    p1, p2 = h1, h2
    carry = 0
    while p1 is not None and p2 is not None:
        p1.val += (p2.val + carry)
        carry = 0
        if p1.val > 9:
            p1.val -= 10
            carry = 1
        
        if p1.next is None and p2.next is not None:
            p1.next = Node(0)
        elif p1.next is not None and p2.next is None:
            p2.next = Node(0)
        elif p1.next is None and p2.next is None and carry == 1:
            p1.next = Node(1)
            break
    
        p1 = p1.next
        p2 = p2.next

    return h1

if __name__ == '__main__':
    a = Node(4); a.next = Node(8); a.next.next = Node(9)
    b = Node(7); b.next = Node(1)

    r = add_lists(b, a)
    arr = []
    while r is not None:
        arr.append(f'({r.val}) -> ')
        r = r.next
    print(''.join(arr))

