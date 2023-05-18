'''
Middle of the Linked List (#876)

Given the head of a singly linked list, return the middle node of the list. If
there are two middle nodes, return the second middle node.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time: O(n)
# Auxiliary space: O(1)
def middle_node(head: ListNode | None) -> ListNode | None:
    count = 0
    node = head
    while node:
        node = node.next
        count += 1
    for _ in range(count // 2):
        head = head.next
    return head


# Time: O(n) (but a little faster)
# Auxiliary space: O(n)
def middle_node2(head: ListNode | None) -> ListNode | None:
    a = []
    while head:
        a.append(head)
        head = head.next
    return a[len(a) // 2]

