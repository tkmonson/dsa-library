from structures import binarytree as bt

my_preorder      = ['M','G','C','A','F','D','K','J','I','L','X','V',
                    'T','R','P','Q','U']
my_inorder       = ['A','C','D','F','G','I','J','K','L','M','P','Q',
                    'R','T','U','V','X']
my_postorder     = ['A','D','F','C','I','J','L','K','G','Q','P','R',
                    'U','T','V','X','M']
my_levelorder    = ['M','G','X','C','K','V','A','F','J','L','T','D',
                    'I','R','U','P','Q']
my_pre_structure = [1,1,1,1,0,0,1,1,0,0,0,1,1,1,0,0,0,1,0,0,1,1,1,1,1,
                    0,1,0,0,0,1,0,0,0,0]
my_lev_structure = [1,1,1,1,1,1,0,1,1,1,1,1,0,0,0,1,0,1,0,0,0,1,1,0,0,
                    0,0,1,0,0,0,0,1,0,0]

#tree = bt.BinaryTree.succinct_construct(my_lev_structure, my_levelorder, order="levelorder")

tree = bt.BinaryTree(preorder=my_preorder, inorder=my_inorder)

print(tree)

