'''
Diameter of Binary Tree (#543)

Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two
nodes in a tree. This path may or may not pass through the root.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter_of_binary_tree(root: TreeNode | None) -> int:
    def max_depth(node, depth):
        nonlocal diameter
        if node is None:
            return depth - 1
        max_left_depth = max_depth(node.left, depth + 1)
        max_right_depth = max_depth(node.right, depth + 1)
        diameter = max(diameter, max_left_depth + max_right_depth - 2 * depth)
        return max(max_left_depth, max_right_depth)

    diameter = 0
    max_depth(root, 0)
    return diameter


def diameter_of_binary_tree2(root: TreeNode | None) -> int:
    def height(node):
        nonlocal diameter
        if node is None:
            return 0
        left_height = height(node.left)
        right_height = height(node.right)
        diameter = max(diameter, left_height + right_height)
        return max(left_height, right_height) + 1

    diameter = 0
    height(root)
    return diameter

'''
The key insight here is that the diameter of any subtree rooted at node n is
equal to the length of the longest left path (starting at n and passing through
n.left) plus the length of the longest right path (starting at n and passing
through n.right). This can be expressed in terms of the maximum depths of the
left and right subtrees or in terms of the heights of n.left and n.right.
'''

