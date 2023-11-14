'''
Subtree of Another Tree (#572)

Given the roots of two binary trees `root` and `sub_root`, return True if there
is a subtree of `root` with the same structure and node values of `sub_root` or
False otherwise.
'''

from collections import deque
from same_tree import is_same_tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    if not p and not q:
        return True
    elif not p or not q or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
'''

def is_subtree_dfs(root: TreeNode | None, sub_root: TreeNode | None) -> bool:
    if root:
        if (is_same_tree(root, sub_root) or
            is_subtree_dfs(root.left, sub_root) or
            is_subtree_dfs(root.right, sub_root)):
                return True
    return False


def is_subtree_bfs(root: TreeNode | None, sub_root: TreeNode | None) -> bool:
    queue = deque([root])
    while queue:
        root = queue.pop()
        if is_same_tree(root, sub_root):
            return True
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
    return False


if __name__ == '__main__':
    root = TreeNode(3,
                    TreeNode(4,
                             TreeNode(1),
                             TreeNode(2)),
                    TreeNode(5))
    sub_root = TreeNode(4,
                        TreeNode(1),
                        TreeNode(2))
    print(is_subtree_bfs(root, sub_root))

