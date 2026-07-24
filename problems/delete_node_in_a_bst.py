'''
Delete Node in a BST (#450)

Given a root reference of a BST and a key, delete the node with the given key
in the BST. Return the root node reference (possibly updated) of the BST. If a
node with the given key does not exist in the BST, return the original BST.
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def get_successor(root: TreeNode) -> TreeNode:
    root = root.right
    while root and root.left:
        root = root.left
    return root

# Time: O(h) where h is the height of the tree (O(logn) if tree is balanced)
# Auxiliary space: O(1)
def delete_node(root: TreeNode, key: int) -> TreeNode:
    if not root:
        return root
    
    if root.val > key:
        root.left = delete_node(root.left, key)
    elif root.val < key:
        root.right = delete_node(root.right, key)
    else:
        # root has 0 or 1 children
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        
        # root has 2 children
        root.val = get_successor(root).val
        root.right = delete_node(root.right, root.val)

    return root

'''
For a BST, inorder is sorted order.

For some node to be deleted D, there are three cases:

Case 1: D has zero children
    * Redirect pointer from D's parent to D to null
Case 2: D has one child
    * Redirect pointer from D's parent to D to the node's child
Case 3: D has two children
    * D needs to be replaced with some node that will preserve BST structure
    * This node must be either D's inorder predecessor or inorder successor
      (i.e. the largest node in D's left subtree or the smallest node in D's
      right subtree).
    * Traverse to this node and copy its value to D. This node will have at
      most one child. Delete this node, according to the cases above.

In order to handle the issue where you need to have a reference to the parent
to properly remove a node with 0 or 1 children, you can have delete_node return
the root of the subtree it operates on, after deletion. That result can be
assigned as the left or right child of the node one level up in the recursion.
'''