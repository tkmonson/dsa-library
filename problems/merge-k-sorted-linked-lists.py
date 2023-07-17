'''
Merge k Sorted Lists (#23)

Given an array of `k` linked lists, each sorted in ascending order, merge all
of the linked lists into one sorted linked list and return it.
'''

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Written this way to appease the Leetcode testing suite
ListNode.__lt__ = lambda self, other: self.val < other.val
ListNode.__gt__ = lambda self, other: self.val > other.val
ListNode.__le__ = lambda self, other: self.val <= other.val
ListNode.__ge__ = lambda self, other: self.val >= other.val
ListNode.__eq__ = lambda self, other: self.val == other.val
ListNode.__ne__ = lambda self, other: self.val != other.val


def merge_k_lists(lists: list[ListNode] | None) -> ListNode | None:
    head = curr = ListNode()
    heap = []

    for lst in lists:
        if lst:
            heapq.heappush(heap, lst)

    while heap:
        if heap[0].next:
            curr.next = heapq.heapreplace(heap, heap[0].next)
        else:
            curr.next = heapq.heappop(heap)
        curr = curr.next

    return head.next


if __name__ == '__main__':
    lists = [
        ListNode(3, ListNode(7, ListNode(8))),
        ListNode(2, ListNode(3, ListNode(4, ListNode(9)))),
        None,
        ListNode(1, ListNode(5, ListNode(6)))
    ]
    result = merge_k_lists(lists)
    arr = []
    while result:
        arr.append(str(result.val))
        result = result.next
    print(' -> '.join(arr))

