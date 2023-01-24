'''
Remove Nth Node From End of List (#19)

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Time: O(n)
Space: O(n)
'''

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        printStr = ''
        while self != None:
            printStr = printStr + str(self.val) + ' -> '
            self = self.next
        return printStr


def removeNthFromEndRecursive(head: Optional[ListNode],
                     n: int) -> Optional[ListNode]:
    i = 0  # 1 is last node, 2 is second to last, etc.
    removed = False
    def helper(curr):
        nonlocal i, removed
        if curr.next is not None:
            helper(curr.next)
        i = i + 1
        if i == n + 1:
            curr.next = curr.next.next
            removed = True

    helper(head)
    return head if removed else head.next


def removeNthFromEndIterative(head: Optional[ListNode],
                              n: int) -> Optional[ListNode]:
    nodes = []
    curr = head
    while curr is not None:
        nodes.append(curr)
        curr = curr.next
    if n == len(nodes):
        return head.next
    nodes[-n - 1].next = nodes[-n - 1].next.next
    return head


if __name__ == '__main__':
    a = ListNode(2, ListNode(6, ListNode(3)))
    print(a)
    print(removeNthFromEndRecursive(a, 2))

'''
This is a singly linked list... can't start from the end, don't know its
length. So you have to traverse the entire length, and there are two ways of
doing that: recursion and iteration.

Because a singly linked list has no built-in indexing and yet we must access a
particular node in the list based on its position, both methods must somehow
compensate for this. The recursive method does this by incrementing an index
variable as subroutines are taken off of the call stack. The iterative method
does this by copying nodes to an array, which is then indexed. Both use O(n)
space, either implicitly, via the call stack, or explicitly, via an array.
'''
