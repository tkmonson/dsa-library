'''
Insert Greatest Common Divisor in Linked List (#2807)

Given the head of a linked list head, in which each node contains an integer
value. Between every pair of adjacent nodes, insert a new node with a value
equal to the greatest common divisor of them. The number of nodes in the list
is in the range [1, 5000].

Return the linked list after insertion.
'''

from math import gcd

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insert_greatest_common_divisors(head: ListNode) -> ListNode:
    curr = head
    while curr.next:
        mid = ListNode(gcd(curr.val, curr.next.val), curr.next)
        curr.next = mid
        curr = mid.next

    return head


if __name__ == '__main__':
    head = ListNode(18, ListNode(6, ListNode(10, ListNode(3))))
    res = insert_greatest_common_divisors(head)
    while res:
        print(res.val)
        res = res.next
