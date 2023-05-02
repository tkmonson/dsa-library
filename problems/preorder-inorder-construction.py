'''
Construct Binary Tree from Preorder and Inorder Traversal (#105)

Given the preorder and inorder traversals of a binary tree, construct and
return the binary tree.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_recur(preorder: list[int],
                     inorder: list[int]) -> TreeNode | None:
    n = len(inorder)
    in_index = {inorder[i]: i for i in range(n)}
    pre_index = 0

    def build_subtree(in_start, in_end):
        nonlocal pre_index

        if in_start >= in_end:
            return None

        root = TreeNode(preorder[pre_index])
        pre_index += 1

        partition_index = in_index[root.val]
        root.left = build_subtree(in_start, partition_index)
        root.right = build_subtree(partition_index + 1, in_end)

        return root

    return build_subtree(0, n)


def build_tree_iter(preorder: list[int],
                    inorder: list[int]) -> TreeNode | None:
    root = TreeNode(preorder[0])
    stack = [root]
    i, j = 1, 0
    
    while i < len(preorder):
        node = TreeNode(preorder[i])
        if stack[-1].val != inorder[j]:
            stack[-1].left = node
        else:
            while stack and stack[-1].val == inorder[j]:
                last_node = stack.pop()
                j += 1
            last_node.right = node
        stack.append(node)
        i += 1

    return root

