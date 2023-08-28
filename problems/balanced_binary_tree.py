'''
Balanced Binary Tree (#110)

Given a binary tree, determine if it is height-balanced. A binary tree is
height-balanced if the heights of each node's children do not differ by more
than one.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root: TreeNode | None) -> bool:
    def dfs(node):
        if not node:
            return 0
        if (left := dfs(node.left)) < 0 or (right := dfs(node.right)) < 0:
            return -1
        return max(left, right) + 1 if abs(left - right) <= 1 else -1

    return dfs(root) != -1

'''
Because we can only know whether a subtree is height-balanced after exploring
both of its subtrees, it makes sense to perform a postorder traversal.
'''

