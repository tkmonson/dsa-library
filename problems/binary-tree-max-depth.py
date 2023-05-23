'''
Maximum Depth of Binary Tree (#104)

Given the root of a binary tree, return its maximum depth (the number of nodes
along the longest path from the root to the farthest leaf).
'''

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth_dfs(root: TreeNode | None) -> int:
    if not root.left and not root.right:
        return 1
    return 1 + max(max_depth(root.left), max_depth(root.right))


def max_depth_bfs(root: TreeNode | Node) -> int:
    if not root:
        return 0

    depth = 0
    queue = deque([root])
    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return depth

