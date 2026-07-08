'''
Delete Leaves With a Given Value (#1325)

Given a binary tree root and an integer target, delete all the leaf nodes with
value target. If you delete a leaf node with value `target` and its parent node
becomes a leaf node with value `target`, it should also be deleted (continue
doing this until you cannot).
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time: O(n) (where n is number of nodes in tree)
# Auxiliary space: O(n) (stack)
def remove_leaf_nodes(root: TreeNode, target: int) -> TreeNode:
    def dfs(root):
        if root.left and dfs(root.left):
            root.left = None
        if root.right and dfs(root.right):
            root.right = None
        return not root.left and not root.right and root.val == target

    return None if dfs(root) else root

'''
Because a node can become a leaf after visiting its children, the tree should
be traversed in postorder.
'''

if __name__ == '__main__':
    def dfs(root):
        if not root:
            print('None')
            return
        print(root.val)
        dfs(root.left)
        dfs(root.right)

    root = TreeNode(1,
                    TreeNode(2,
                             TreeNode(2)
                            ),
                    TreeNode(3,
                             TreeNode(2),
                             TreeNode(4)
                            )
                   )
    target = 2
    dfs(root)
    print('\n')

    dfs(remove_leaf_nodes(root, target))
