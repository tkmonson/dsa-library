'''
Kth Smallest Element in a BST (#230)

Given the root of a binary search tree and an integer k, return the kth
smallest value (1-indexed) of all the values of the nodes in the tree.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kth_smallest(root: TreeNode | None, k: int) -> int:
    def dfs(root):
        nonlocal k
        if not root:
            return -1
        if (left := dfs(root.left)) >= 0:
            return left
        k -= 1
        if k == 0:
            return root.val
        if (right := dfs(root.right)) >= 0:
            return right
        return -1

    return dfs(root)


def kth_smallest2(root: TreeNode | None, k: int) -> int:
    stack = []

    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if not k:
            return root.val
        root = root.right

'''
A BST is sorted inorder. Traverse the tree inorder, navigate to the kth node in
that order, and return its value.
'''

if __name__ == '__main__':
    root = TreeNode(5,
                    TreeNode(3,
                             TreeNode(2,
                                      TreeNode(1)
                                     ),
                             TreeNode(4)
                            ),
                    TreeNode(6)
                   )
    print(kth_smallest(root, 3))

