'''
Binary Tree Preorder Traversal (#144)

Given the root of a binary tree, return the preorder traversal of its nodes' values.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time: O(n)
# Auxiliary space: O(n)
def preorder_traversal(root: TreeNode) -> list[int]:
    result = []
    def dfs(root):
        if root:
            result.append(root.val)
            dfs(root.left)
            dfs(root.right)
    dfs(root)
    return result


if __name__ == '__main__':
    root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    print(preorder_traversal(root))
