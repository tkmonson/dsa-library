'''
Binary Tree to Doubly-Linked List

Convert a given binary tree into a doubly-linked list in-place. The left and
right pointers of the tree's nodes are to be used as the previous and next
pointers of the list's nodes, respectively. The order of the nodes in the
doubly-linked list must correspond to the in-order traversal of the tree. The
head of the doubly-linked list must point to the first node visted in an
in-order traversal.

Time: O(n)
Space: O(1)

Example:
    Input:

         1
       /   \
      2     3
     / \    /
    4   5  6

    Output:

    head
       v
       4 <-> 2 <-> 5 <-> 1 <-> 6 <-> 3
'''

