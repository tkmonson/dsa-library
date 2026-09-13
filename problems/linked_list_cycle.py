'''
Linked List Cycle (#141)

Given the head of a linked list, determine if the linked list has a cycle.
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Time: O(n)
# Auxiliary space: O(n)
def has_cycle(head: ListNode | None) -> bool:
        s = set()
        while head:
            if head in s:
                return True
            s.add(head)
            head = head.next
        return False


# Time: O(n)
# Auxiliary space: O(1) (destroys the data in the list)
def has_cycle2(head: ListNode | None) -> bool:
    while head:
        if head.val is None:
            return True
        head.val = None
        head = head.next
    return False

