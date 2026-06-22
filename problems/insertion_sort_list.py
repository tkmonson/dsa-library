'''
Insertion Sort List (#147)

Given the head of a singly linked list, sort the list using insertion sort, and
return the sorted list's head.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time: O(n^2) (insertion sort)
# Auxiliary space: O(1)
def insertion_sort(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    dummy_head = ListNode(float('inf'), head)
    last_sorted = head
    curr = head.next

    while curr:
        if last_sorted.val <= curr.val:
            last_sorted = curr
        else:
            prev = dummy_head

            # Search for insertion point
            while prev.next.val < curr.val:
                prev = prev.next
            
            # Insert
            last_sorted.next = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = last_sorted.next

        curr = last_sorted.next

    return dummy_head.next

'''
For each unsorted element, you are searching for an insertion point within the
list of sorted elements. It is helpful to point a dummy head at the head of the
sorted list to more easily consider the insertion point at the front of the
sorted list.

Let there be two pointers: one to the last element of the sorted list (L) and
one to the next element to be inserted (C). If L <= C, they are in the right
order; increment the pointers. Otherwise, search the sorted list for the
insertion point.

      L    C
# -> -1 -> 5 -> 3 -> 4 -> 0

      P    L    C
# -> -1 -> 5 -> 3 -> 4 -> 0

      P    L    C
           _____
           v    |
# -> -1 -> 5 -> 3 -> 4 -> 0
      |    |    ^    ^
      |    |____|____|
      |_________|

                L    C
# -> -1 -> 3 -> 5 -> 4 -> 0
'''

if __name__ == '__main__':
    head = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
    result = insertion_sort(head)
    while result:
        print(result.val)
        result = result.next

