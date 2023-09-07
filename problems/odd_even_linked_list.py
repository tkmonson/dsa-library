'''
Odd Even Linked List (#328)

Given the head of a singly linked list, group all the nodes with odd indicies
together followed by the nodes with even indicies and return the reordered
list. The first node is considered odd, and the second node is considered even,
and so on. The relative order of the nodes in the odd and even groups should
remain the same as it was in the input. The problem must be solved in O(n) time
and O(1) space.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def odd_even_list(head: ListNode | None) -> ListNode | None:
    try:
        head2 = head.next
    except(AttributeError):
        return None
    p1, p2 = head, head2

    while p2:
        p1.next = p1.next.next
        if not p1.next:
            break
        p1 = p1.next
        p2.next = p2.next.next
        p2 = p2.next

    p1.next = head2
    return head


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    odd_even_list(head)
    linked_list = []
    while head:
        linked_list.append(f'{head.val} -> ')
        head = head.next
    print(''.join(linked_list))

