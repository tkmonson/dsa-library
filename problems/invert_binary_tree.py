'''
Invert Binary Tree (#226)

Given the root of a binary tree, invert the tree, and return its root.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root:
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)
        return root

def invert_tree_iterative(root: Optional[TreeNode]) -> Optional[TreeNode]:
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack += node.left, node.right
    return root

