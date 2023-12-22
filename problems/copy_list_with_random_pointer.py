'''
Copy List with Random Pointer (#138)

Given a linked list of nodes where each node has an additional "random" pointer
that can point to any node in the list or None, construct a deep copy of the
list and return its head.
'''

from contextlib import suppress

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


# Time: O(n) (faster)
# Auxiliary space: O(n)
def copy_random_list(head: Node | None) -> Node | None:
    if not head:
        return None

    old_to_new = {}

    # Map old nodes to new nodes
    curr = head
    while curr:
        old_to_new[curr] = Node(curr.val)
        curr = curr.next

    # Set next and random pointers
    curr = head
    while curr:
        old_to_new[curr].next = old_to_new[curr.next]
        old_to_new[curr].random = old_to_new[curr.random]
        curr = curr.next

    return old_to_new[head]


# Time: O(n) (slower)
# Auxiliary space: O(1)
def copy_random_list2(head: Node | None) -> Node | None:
    if not head:
        return None

    # Create new nodes and interweave them with the original list
    curr = head
    while curr:
        node = Node(curr.val, curr.next)
        curr.next = node
        curr = curr.next.next

    # Set random pointers
    curr = head
    while curr:
        with suppress(AttributeError):  # random points to None
            curr.next.random = curr.random.next
        curr = curr.next.next

    # Set next pointers and separate the lists
    curr = head
    new_head = head.next
    while curr:
        node = curr.next
        with suppress(AttributeError):
            curr.next = curr.next.next
            node.next = node.next.next
        curr = curr.next

    return new_head


# Time: O(n)
# Auxiliary space: O(n)
def copy_random_list3(head: Node | None) -> Node | None:
    if not head:
        return None

    d = {head: 0}  # map of original nodes to indicies
    a = [Node(head.val)]  # list of new nodes

    curr = head.next
    i = 1
    while curr:
        d[curr] = i
        a[-1].next = Node(curr.val)
        a.append(a[-1].next)

        curr = curr.next
        i += 1

    curr = head
    i = 0
    while curr:
        with suppress(KeyError):
            a[i].random = a[d[curr.random]]
        curr = curr.next
        i += 1

    return a[0]

'''
My first solution. Traverse original list, construct map of original nodes to
indicies, construct list of new nodes with their next pointers set correctly.
Traverse original list again: for each node, get the node its random pointer is
pointing to, look up the index of that node in the map, use that index to
access its "new" counterpart.
'''

if __name__ == '__main__':
    a = [Node(7), Node(13), Node(11), Node(10), Node(1)]
    for i in range(len(a) - 1):
        a[i].next = a[i + 1]
    a[1].random = a[0]
    a[2].random = a[4]
    a[3].random = a[2]
    a[4].random = a[0]

    curr = copy_random_list(a[0])
    while curr:
        print(f'V: {curr.val}')
        print(f'N: {curr.next.val if curr.next else None}')
        print(f'R: {curr.random.val if curr.random else None}\n')
        curr = curr.next

