from structures import binaryheap as bh
from structures import binarytree as bt

#pre_data = [0,'b',1,2,'a',3,4]
#in_data = [1,'b',2,0,3,'a',4]
#tree = bt.BinaryTree(preorder=pre_data, inorder=in_data)
#tree._swap_nodes(tree.root.right, tree.root.left)

data = [9,8,7,6,5,4,3,2,1,0,3,2,1,0]

maxheap = bh.ExplicitBinaryMaxHeap(levelorder=data)
print(maxheap)

maxheap.insert(8)
'''
maxheap.root.right.right.right = bt.BTNode(8)
maxheap.root.right.right.right.parent = maxheap.root.right.right
print(maxheap)

maxheap._sift_up(maxheap.root.right.right.right)
'''
print(maxheap)

blahheap = bh.ExplicitBinaryMaxHeap(
    levelorder=[0,1,0,2,3,1,3,9,6,5,8,2,4,7])
print(blahheap)
