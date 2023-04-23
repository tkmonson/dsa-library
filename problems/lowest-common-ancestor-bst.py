'''
Lowest Common Ancestor of a Binary Search Tree (#235)

Given a binary search tree, find the lowest common ancestor of two given nodes
in the tree. The lowest common ancestor of two nodes `p` and `q` is the lowest
node in the tree that has both `p` and `q` as descendants (where we allow a
node to be a descendant of itself).
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowest_common_ancestor(root: TreeNode,
                           p: TreeNode, q: TreeNode) -> TreeNode:
    if (not root or root is p or root is q or 
        p.val < root.val < q.val or
        p.val > root.val > q.val):
            return root

    if p.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    else:
        return lowest_common_ancestor(root.right, p, q)


def lowest_common_ancestor2(root: TreeNode,
                            p: TreeNode, q: TreeNode) -> TreeNode:
    while root:
        if p.val < root.val > q.val:
            root = root.left
        elif p.val > root.val < q.val:
            root = root.right
        else:
            return root

'''
If p and q are on the same side of the root, traverse in that direction because
the LCA must be on that side, too. If you traverse to a node where p and q are
on different sides of it, that node is the LCA. If you traverse to p or q, that
node is the LCA.
'''

