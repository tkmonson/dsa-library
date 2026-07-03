'''
Reverse Linked List II (#92)

Given the `head` of a singly linked list and two integers `left` and `right`
where `left <= right`, reverse the nodes of the list from the position `left`
to position `right` and return the reversed list.

e.g. 1 -> 2 -> 3 -> 4 -> 5 ->, left = 2, right = 4
     1 -> 4 -> 3 -> 2 -> 1 ->
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time: O(n)
# Auxiliary space: O(1)
def reverse_between(head: ListNode, left: int, right: int) -> ListNode:
    dummy = ListNode(0, head)
    prev = dummy
    curr = head
    for _ in range(left - 1):
        prev = curr
        curr = curr.next
    
    prev_left_p = prev
    left_p = curr

    prev = curr
    curr = curr.next

    for _ in range(right - left):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    prev_left_p.next = prev
    left_p.next = curr

    return dummy.next

'''
To avoid handling the special case of reversing at the head, prepend a "dummy"
node. Note that indexes given in the input are 1-indexed.

(2, 4)
X -> 1 -> 2 -> 3 -> 4 -> 5 ->
X -> 1 -> 2 <- 3 <- 4 -> 5 ->
     |--------------v
X -> 1    2 <- 3 <- 4    5 ->
          |--------------^

(1, 4)
X -> 1 -> 2 -> 3 -> 4 -> 5 ->
X -> 1 <- 2 <- 3 <- 4 -> 5 ->
|-------------------v
X    1 <- 2 <- 3 <- 4    5 ->
     |-------------------^

The strategy is to reverse some inner part of the list and reconnect it to the
outer parts. You need pointers to nodes at indexes: left - 1, left, right,
right + 1. To reverse the nodes in the inner list, prev should start at left
and curr should start at left + 1.
'''

# Time: O(n)
# Auxiliary space: O(1)
def reverse_between2(head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next

'''
This solution is more clever, but I find it harder to understand. Essentially,
temp moves forward and we keep placing it right behind prev.

(2, 4)
     P    C
X -> 1 -> 2 -> 3 -> 4 -> 5 ->

     P    C    T
     |---------v
X -> 1    2 <- 3    4 -> 5 -> 
          |---------^

     P    C         T
     |--------------v
X -> 1    2 <- 3 <- 4    5 ->
          |--------------^
'''

if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))
    head = reverse_between(head, 3, 7)
    while head:
        print(head.val)
        head = head.next
