'''
Insert into a Binary Search Tree (#701)

You are given the root node of a binary search tree (BST) and a value to insert
into the tree. Return the root node of the BST after the insertion. It is
guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as
the tree remains a BST after insertion. You can return any of them.
'''

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time: O(logn) where n is the number of nodes in the BST
# Auxiliary space: O(1)
def insert_into_bst(root: TreeNode, val: int) -> TreeNode:
    if not root:
        return TreeNode(val)
    
    curr, next = None, root
    while next:
        curr = next
        next = curr.left if curr.val > val else curr.right

    if curr.val > val:
        curr.left = TreeNode(val)
    else:
        curr.right = TreeNode(val)

    return root


# Time: O(logn) where n is the number of nodes in the BST
# Auxiliary space: O(1)
def insert_into_bst2(root: TreeNode, val: int) -> TreeNode:
    if not root:
        return TreeNode(val)

    node = root
    while True:
        if node.val > val:
            if node.left:
                node = node.left
            else:
                node.left = TreeNode(val)
                break
        else:
            if node.right:
                node = node.right
            else:
                node.right = TreeNode(val)
                break
    
    return root

'''
Traverse through the BST as if you were searching for val.
Stop when you get to a node that could insert val as a child (a leaf or a
parent with no left child if val is less or no right child if val is greater).
Insert val as a child of the node you are at.
Return root.
'''
