'''
Binary Tree Maximum Path Sum (#124)

A path is a sequence of nodes where each pair of adjacent nodes in the sequence
has an edge between them. The path sum of a path is the sum of the values of
the nodes in the path. Given the root of a binary tree, return the maximum path
sum of all possible paths in the tree.
'''

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def maximum_path_sum(root: TreeNode) -> int:
    ans = root.val
    def dfs(root):
        nonlocal ans
        if not root:
            return 0
        left = max(0, dfs(root.left))
        right = max(0, dfs(root.right))
        ans = max(ans, root.val + left + right)
        return root.val + max(left, right)

    dfs(root)
    return ans

'''
Let the root of a path be the node in the path that is highest in the tree. In
a DFS traversal of a path, we can only "split" (take both paths) from the root;
for all other nodes in the path, we can only take the left or right path.

For each node n, we want to find the maximum path sum for both a path that is
rooted at n (allowed to split) and for a subpath that starts n and is part of a
path that is rooted at some higher node (not allowed to split). The latter sum
will be returned upward to the parent node.
'''
    
if __name__ == '__main__':
    root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(maximum_path_sum(root))
    
