'''
Lowest Common Ancestor of a Binary Tree (#236)

Given a binary tree, find the lowest common ancestor of two given nodes in the
tree. The lowest common ancestor of two nodes `p` and `q` is the lowest node in
the tree that has both `p` and `q` as descendants (where we allow a node to be
a descendant of itself).
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowest_common_ancestor(root: TreeNode,
                           p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or root is p or root is q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root
    return left or right

'''
If q exists in the subtree rooted at p, p is the LCA (and vice-versa).
Otherwise, the LCA is the node where the parent chains of p and q intersect.
When this algorithm finds p or q (F) in a subtree, it propagates F up the call
stack and looks for the other node (S) outside of that subtree. If it doesn't
find S, then the LCA is F. If it does, then it propagates S up the call stack
until it reaches a node whose other subtree returned F. Then, that node is the
LCA.

This algorithm has both preorder and postorder qualities. That is, a node may
propagate a result upward immediately or after processing both of its subtrees.
'''

def lowest_common_ancestor_naive(root: TreeNode,
                                 p: TreeNode, q: TreeNode) -> TreeNode:
    def dfs(node):
        if not node:
            return True
        path.append(node)
        if (not node is target) and dfs(node.left) and dfs(node.right):
            path.pop()
            return True
        return False

    p_path, q_path = [], []
    for target, path in [(p, p_path), (q, q_path)]:
        dfs(root)

    for i in range(min(len(p_path), len(q_path))):
        if p_path[i] is not q_path[i]:
            return p_path[i - 1]
    return p_path[i]

'''
Maintain a path that expands and shrinks as the tree is explored via DFS. When
p or q is found, save a snapshot of the path. Traverse the two paths, starting
at the root, until the paths diverge. The last node before divergence is the
LCA.
'''

