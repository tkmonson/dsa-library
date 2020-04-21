# https://leetcode.com/problems/longest-univalue-path/

# Input: binary tree
# Output: int (the edge length of longest univalue path, starting from any node)

#       5 
#     /  \
#   4     5
#  / \    /
# 1  4   5
#     \
#     4
#      \
#      4

# Output: 3 (3 edges in path of 4s)

# Traverse the tree
# Increment count going down, decrement count going up
# If next node has different value, start a new count
# Update a max count var when you get to a leaf

# create a max_count var
# define helper(root, count)
    # if root is leaf
        # update max_count (if count is bigger)
        # return
    
    # left_count = count + 1 or 0 (if chars mismatch) 
    # right_count = count + 1 or 0 (if chars mismatch)
    
    # helper(root.left, left_count) 
    # helper(root.right, right_count)

# call helper(root, 0)
# return max_count

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def longestUnivaluePath(root):
    max_count = 0

    def helper(root, count):
        nonlocal max_count
        if root.left is None and root.right is None:
            if count > max_count:
                max_count = count
            return
                
        if root.left is not None:
            if root.left.val == root.val: 
                helper(root.left, count + 1)
            else:
                helper(root.left, 0)
            
        if root.right is not None:
            if root.right.val == root.val: 
                helper(root.right, count + 1)
            else:
                helper(root.right, 0)
        
    helper(root, 0)
    return max_count
       
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)
root.left.right.right = TreeNode(4)
root.left.right.right.right = TreeNode(4) 

print(longestUnivaluePath(root)) 
