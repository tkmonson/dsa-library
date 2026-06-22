'''
Binary Tree Inorder Traversal (#94)

Given the root of a binary tree, return the inorder traversal of its nodes' values.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time: O(n)
# Auxiliary space: O(n)
def inorder_traversal(root: TreeNode) -> list[int]:
    result = []
    def dfs(root):
        if root:
            dfs(root.left)
            result.append(root.val)
            dfs(root.right)
    dfs(root)
    return result


if __name__ == '__main__':
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    print(inorder_traversal(root))
