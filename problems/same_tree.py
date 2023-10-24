'''
Same Tree (#100)

Given the roots of two binary trees, write a function to check if they are the
same or not. Two binary trees are considered the same if they are structurally
identical and the nodes have the same values.
'''

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
    if not p and not q:
        return True
    elif not p or not q or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

'''
Two trees are the same if their roots are the same, their left subtrees are the
same, and their right subtrees are the same.
'''

def is_same_tree_dfs(p: TreeNode | None, q: TreeNode | None) -> bool:
    if p and q:
        if p.val != q.val:
            return False

        for pc, qc in [(p.left, q.left), (p.right, q.right)]:
            if pc and qc:
                if not is_same_tree_dfs(pc, qc):
                    return False
            elif pc or qc:
                return False
    elif p or q:
        return False

    return True


def is_same_tree_bfs(p: TreeNode | None, q: TreeNode | None) -> bool:
    queue = deque()
    if p and q:
        if p.val != q.val:
            return False
        queue.append(p)
        queue.append(q)
    elif p or q:
        return False

    while queue:
        p = queue.popleft()
        q = queue.popleft()
        for pc, qc in [(p.left, q.left), (p.right, q.right)]:
            if pc and qc:
                if pc.val != qc.val:
                    return False
                queue.append(pc)
                queue.append(qc)
            elif pc or qc:
                return False

    return True

