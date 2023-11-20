'''
Count Good Nodes in Binary Tree (#1448)

A node X in a binary tree is considered "good" if there are no nodes in the
path from X to the root with values greater than X. Return the number of good
nodes in the binary tree.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def good_nodes(root: TreeNode) -> int:
    result = 0
    def dfs(root, curr_max):
        nonlocal result
        if root.val >= curr_max:
            result += 1
            curr_max = root.val
        if root.left:
            dfs(root.left, curr_max)
        if root.right:
            dfs(root.right, curr_max)
        
    dfs(root, float('-inf'))
    return result

def good_nodes2(root: TreeNode) -> int:
    def dfs(root, curr_max):
        if not root:
            return 0
        is_good = 0
        if root.val >= curr_max:
            curr_max = root.val
            is_good = 1
        return is_good + dfs(root.left, curr_max) + dfs(root.right, curr_max)

    return dfs(root, float('-inf'))

