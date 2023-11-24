'''
Reorder List (#143)

Given the head of a list that can be represented as L_0 -> L_1 -> ... -> L_n-1
-> L_n, reorder the list to be of the form L_0 -> L_n -> L_1 -> L_n-1 -> L_2 ->
L_n-2 -> ..., without modifying the values of the list's nodes.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time: O(n)
# Auxiliary space: O(1)
def reorder_list(head: ListNode | None) -> None:
    # Put a pointer on the middle node
    slow, fast = head, head.next
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next

    # Split list at the middle, reverse the right list
    curr = slow.next
    prev = slow.next = None
    while curr:
        next = curr.next
        curr.next = prev
        prev, curr = curr, next

    # Traverse the lists synchronously, point l1 to l2 and l2 to l1.next
    l1, l2 = head, prev
    while l1 and l2:
        next1, next2 = l1.next, l2.next
        l1.next = l2
        l2.next = next1
        l1, l2 = next1, next2

    return head

'''
The output list spirals inward, so it would help to have access to node i and
node (n - 1 - i), 0 <= i < n/2, at any given step. To do this, you need to
traverse the left half of the list forward and the right half of the list
backward. To do the latter, reverse the direction of the pointers.
'''

# Time: O(n)
# Auxiliary space: O(n)
def reorder_list2(head: ListNode | None) -> None:
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    slow = slow.next

    stack = []
    while slow:
        stack.append(slow)
        slow = slow.next

    prev = head
    curr = head.next

    while stack:
        pop = stack.pop()
        prev.next = pop
        pop.next = curr
        prev = curr
        curr = curr.next

    prev.next = None

'''
Another way to traverse the right half of the list backward is to put nodes
onto a stack and pop them off, but this requires O(n) space.
'''

if __name__ == '__main__':
    head = ListNode(0, ListNode(1, ListNode(2,
           ListNode(3, ListNode(4, ListNode(5))))))
    reorder_list(head)
    a = []
    curr = head
    while curr:
        a.append(f'{curr.val} -> ')
        curr = curr.next
    print(''.join(a))

