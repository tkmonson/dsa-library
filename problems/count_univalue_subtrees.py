# Given a binary tree, return the number of univalue subtrees in that tree.

# Input: [5, 1, 5, 5, 5, null, 5]

#        5
#       / \
#      1   5
#     / \   \
#    5   5   5

# Output: 4 (the three leaves, and the right child of the root)

from structures import TreeNode, Tree

def count_univalue_subtrees(bintree):
    count = 0
    def helper(root):
        nonlocal count

        if root is None:
            return True

        left_is_univalue = helper(root.left)
        right_is_univalue = helper(root.right)

        if (left_is_univalue and
            right_is_univalue and
            (root.left is None or root.data == root.left.data) and
            (root.right is None or root.data == root.right.data)):
            count += 1
            return True
        else:
            return False

    helper(bintree.root)
    return count

def arr_to_tree(arr):
    root = None
    i = 0
    n = len(arr)

    def helper(arr, root, i, n):
        if i < n:
            root = TreeNode(arr[i])
            root.left = helper(arr, root.left, 2*i + 1, n)
            root.right = helper(arr, root.right, 2*i + 2, n)
        return root
    
    root = helper(arr, root, i, n)
    return Tree(root)

arr = [5, 1, 5, 5, 5, None, 5]
tree = arr_to_tree(arr)

print(count_univalue_subtrees(tree))

# ---- PSEUDOCODE ----

# At any given node, you need to know the values under it to know if it is the root of a univalue subtree. This implies that we need to DFS the tree in postorder (traverse first, make decisions after).

# A node is the root of a univalue subtree if:
    # Left child is root of univalue subtree (or null)
    # Right child is root of univalue subtree (or null)
    # Parent value is equal to left value (or left is null)
    # Parent value is equal to right value (or right is null)

# We need a helper method that decides whether a given tree is univalue. If it is, increment a nonlocal count variable and return True. Otherwise, return False.

# Base case: Node is null => True (but don't increment count)
