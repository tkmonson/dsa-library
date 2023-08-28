'''
Binary Tree Right Side View (#199)

Given the root of a binary tree, imagine yourself standing on the right side of
it. Return the values of the nodes you can see ordered from top to bottom. That
is, return the values of the rightmost nodes at each level.
'''

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_side_view_bfs(self, root: TreeNode | None) -> list[int]:
    if not root:
        return []

    result = []
    queue = deque([root])
    while queue:
        result.append(queue[-1].val)
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


def right_side_view_dfs(self, root: TreeNode | None) -> list[int]:
    result = []
    def f(node, level):
        if node:
            if level == len(result):
                result.append(node.val)
            f(node.right, level + 1)
            f(node.left, level + 1)
    f(root, 0)
    return result

