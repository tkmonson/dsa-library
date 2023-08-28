'''
Reverse Linked List (#206)

Given the `head` of a singly-linked list, reverse the list, and return the
reversed list.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode | None) -> ListNode | None:
    prev, curr = None, head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

