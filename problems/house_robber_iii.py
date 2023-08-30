'''
House Robber III (#337)

Houses in a neighborhood, each with a certain amount of money stashed, are
connected by a security system such that they form a binary tree. The security
system will contact the police if two directly-linked houses are broken into on
the same night. Given the root of the binary tree, return the maximum amount of
money you can rob without alerting the police.
'''

from functools import cache

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rob(root: TreeNode | None) -> int:
    def _rob(root):
        if not root:
            return [0, 0]

        left = _rob(root.left)
        right = _rob(root.right)

        return [
            max(left) + max(right),
            root.val + left[0] + right[0]
        ]

    return max(_rob(root))

'''
As defined in the algorithm below, rob(root) has overlapping subproblems. But
it can be defined in such a way that its subproblems do not overlap.

Let rob(root) denote the problem of finding two values:

    1. the maximum value that can be robbed from a tree rooted at root,
       assuming that root itself is not robbed
    2. the maximum value that can be robbed from a tree rooted at root,
       assuming that root itself is robbed

The first value can be expressed in terms of subproblems. It is equal to the
sum of the larger value of rob(root.left) and the larger value of
rob(root.right). The second value can be expressed in terms of the same
subproblems. It is equal to the sum of root's value, the first value of
rob(root.left), and the first value of rob(root.right).

The maximum value that can be robbed from a tree rooted at root is equal to the
larger value of rob(root). Because rob(root) has optimal substructure and does
not have overlapping subproblems, it can be solved with a divide-and-conquer
algorithm.
'''

@cache
def rob2(root: TreeNode | None) -> int:
    if not root:
        return 0

    val = 0
    if root.left:
        val += rob2(root.left.left) + rob2(root.left.right)
    if root.right:
        val += rob2(root.right.left) + rob2(root.right.right)

    return max(root.val + val, rob2(root.left) + rob2(root.right))

'''
For any root, if you take the root, you can take or not take any of its four
grandchildren, but you cannot take either of its children. If you do not take
the root, you can take or not take either of its children.

Let rob(root) denote the problem of finding the maximum value that can be
robbed from a tree rooted at root (this value may or may not require robbing
the root itself). rob(root) can be expressed as the greater of two subproblems:

    1. root.val + rob(root.left.left) + rob(root.left.right)
                + rob(root.right.left) + rob(root.right.right)
    2. rob(root.left) + rob(root.right)

Thus, this problem exhibits optimal substructure. As defined above, rob(root)
also has overlapping subproblems; for example, rob(root.left.left) is called in
the first subproblem and it will also be called in the second subproblem while
computing rob(root.left). Thus, dynamic programming is a useful approach here.
'''

if __name__ == '__main__':
    root = TreeNode(1,
                    TreeNode(4,
                             TreeNode(1),
                             TreeNode(1)),
                    TreeNode(5,
                             None,
                             TreeNode(9)))
    print(rob(root))

