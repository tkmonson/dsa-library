'''
Merge Two Sorted Lists (#21)

Given the heads of two sorted linked lists, merge the two lists into one sorted
linked list. The merged list should contain the original nodes from the two
input lists. Return the head of the merged list.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1: ListNode | None,
                    list2: ListNode | None) -> ListNode | None:
    head = curr = ListNode()
    while True:
        try:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        except(AttributeError):
            curr.next = list1 if list1 else list2
            return head.next

