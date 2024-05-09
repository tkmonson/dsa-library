'''
Reverse Nodes in k-Group (#25)

Given the head of a linked list, reverse the nodes of the list `k` at a time
and return the modified list. `k` is a positive integer and is less than or
equal to the length of the linked list. If the number of nodes is not a
multiple of `k`, then left-out nodes should remain as-is. You may not alter
node values.
'''

from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_k_group(head: ListNode | None, k: int) -> ListNode | None:
    # Check if group needs to be reversed
    curr = head
    for _ in range(k):
        if not curr:
            return head
        curr = curr.next

    # Reverse group
    prev = None
    curr = head
    for _ in range(k):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    # Point the tail of the group to the new head of the next group
    head.next = reverse_k_group(curr, k)
    return prev

'''
For each k-group, after reversal:
    * prev points to the new head of the group,
    * head points to the new tail of the group, and
    * curr points to the head of the next group before its reversal.
'''

# Fastest, hard to understand
def reverse_k_group2(head: ListNode | None, k: int) -> ListNode | None:
    q = deque()
    while len(q) < k-1:
        q.append(head)
        head = head.next

    rev_head, tail = head, ListNode()
    while head:
        q.append(head)
        head = head.next
        if len(q) == k:
            prev, edge = head, q[0]
            while q:
                curr = q.popleft()
                curr.next, prev = prev, curr
            tail.next, tail = prev, edge

    return rev_head

'''
For each k-group, before reversal, prev points to the head of the next group.
Curr moves by polling elements from the group queue, prev follows curr.

For k = 3:    C              P
              1 -> 2 -> 3 -> 4

C              P    P    C                   P    C                   P
1    2 -> 3 -> 4    1 <- 2    3 -> 4    1 <- 2 <- 3    4    1 <- 2 <- 3    4
|              ^    |              ^    |              ^    |              ^
|______________|    |______________|    |______________|    |______________|

If a k-group has been reversed, and another k-group proceeds it, then you have
to connect the tail of the proceeding group to the new head. Before doing this,
it points to the new tail (which used to be the head of the group).

T                         P                            _______________ 
1 <- 2 <- 3     4 <- 5 <- 6    7        1 <- 2 <- 3   | T             |  7
|              ^|              ^        |             | 4 <- 5 <- 6 <-   ^
|______________||______________|        |_____________| |________________|
'''

def reverse_k_group3(head: ListNode | None, k: int) -> ListNode | None:
    ret = head
    first_group = True

    curr = head
    while curr:
        prev_head = head
        head = curr
        prev = curr
        curr = curr.next
        for i in range(k - 1):
            if not curr:
                for _ in range(i):
                    prev_prev = prev.next
                    prev.next = curr
                    curr = prev
                    prev = prev_prev

                prev_head.next = prev
                return ret

            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        if first_group:
            ret = prev
            first_group = False
        else:
            prev_head.next = prev

    head.next = None
    return ret

'''
Original solution, it works, but I don't remember how (see paper notes).
'''

if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    k = 3
    def linked_print(curr):
        lst = []
        while curr:
            lst.append(str(curr.val))
            curr = curr.next
        print(' -> '.join(lst))
    linked_print(head)
    curr = reverse_k_group(head, k)
    linked_print(curr)

