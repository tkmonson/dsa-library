'''
Validate Binary Search Tree (#98)

Given the root of a binary tree, determine if it is a valid binary search tree.
A valid BST is defined as follows:
    1. The left subtree of a node contains only nodes with keys less than the
       node's key.
    2. The right subtree of a node contains only nodes with keys greater than
       the node's key.
    3. Both the left and right subtrees must also be BSTs.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst_inorder(root: TreeNode | None) -> bool:
    prev = float('-inf')
    def check(val):
        nonlocal prev
        if val > prev:
            prev = val
            return True
        return False

    def dfs(node):
        if not node:
            return True
        return dfs(node.left) and check(node.val) and dfs(node.right)

    return dfs(root)


def is_valid_bst_preorder(root: TreeNode | None,
        minimum=float('-inf'), maximum=float('inf')) -> bool:
    if not root: return True
    if not minimum < root.val < maximum: return False
    return (is_valid_bst(root.left, minimum, root.val)
            and is_valid_bst(root.right, root.val, maximum))


'''
Inorder traversal is a natural choice for this problem because the inorder
traversal of a BST is strictly ascending. However, preorder traversal allows
for a more elegant, pure-recursive function.

Note that arguments can be added to the function to be tested by Leetcode as
long as they are given default values.
'''

