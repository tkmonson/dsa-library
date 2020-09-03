from structures import binarytree as bt

# Enter your orders here:
my_preorder   = [4,7,2,1,8,3,5]
my_inorder    = [2,7,1,4,8,5,3]
my_postorder  = [2,1,7,5,3,8,4]
my_levelorder = [4,7,8,2,1,3,5]

print("\nGiven:")
print(f"\tPreorder:    {my_preorder}")
print(f"\tInorder:     {my_inorder}")
print(f"\tPostorder:   {my_postorder}")
print(f"\tLevel-order: {my_levelorder}\n")

# Two-argument constructions
print("Preorder/inorder construction:")
print(bt.BinaryTree(preorder=my_preorder,
                     inorder=my_inorder), end='\n\n')
print("Inorder/postorder construction:")
print(bt.BinaryTree(inorder=my_inorder,
                  postorder=my_postorder), end='\n\n')
print("Inorder/level-order construction:")
print(bt.BinaryTree(inorder=my_inorder,
                 levelorder=my_levelorder), end='\n\n')

# One-argument constructions
print("Preorder construction:")
print(bt.BinaryTree(preorder=my_preorder), end='\n\n')
print("Inorder construction:")
print(bt.BinaryTree(inorder=my_inorder), end='\n\n')
print("Postorder construction:")
print(bt.BinaryTree(postorder=my_postorder), end='\n\n')
print("Level-order construction:")
print(bt.BinaryTree(levelorder=my_levelorder), end='\n\n')

# Now go forward with one of the above trees
def reset():
    return bt.BinaryTree(preorder=my_preorder,
                         inorder=my_inorder)
t = reset()

print("This is your input tree for all of the following method tests:\n")
print(t, end='\n\n')

# IS_EMPTY --------------------------------------

print(f"Testing BinaryTree.is_empty... it\'s {t.is_empty()}!\n")

# TO_LIST ---------------------------------------

print("Testing BinaryTree.to_list...", end='\n\n')
print(f"pre:   {t.to_list(order='preorder')}")
print(f"in:    {t.to_list(order='inorder')}")
print(f"post:  {t.to_list(order='postorder')}")
print(f"level: {t.to_list(order='levelorder')}", end='\n\n')

# TRAVERSE --------------------------------------

print("Testing BinaryTree.for_each_node(BinaryTree.invert)...\n")
print(t)
t.for_each_node(t.invert)
print(t, end='\n\n')
t = reset()

# FOLD ------------------------------------------

print(f"Testing BinaryTree.fold(BinaryTree.height)... it's {t.fold(t.height)}!\n")
print(f"Testing BinaryTree.fold(BinaryTree.sum)... it's {t.fold(t.sum)}!\n")

# SEARCH ----------------------------------------

my_target = 3
print(f"Testing BinaryTree.search({my_target})...\n")
print(t, end='\n\n')

orders = {"preorder":   "Preorder:    ",
          "inorder":    "Inorder:     ",
          "postorder":  "Postorder:   ",
          "levelorder": "Level-order: "}

for order in orders:
    node = t.search(my_target, order=order)

    if node.left is None:
        left_data = "None"
    else:
        left_data = str(node.left.data)

    if node.right is None:
        right_data = "None"
    else:
        right_data = str(node.right.data)

    if node.parent is None:
        parent_data = "None"
    else:
        parent_data = str(node.parent.data)

    print(orders[order] + f"data = {node.data}, left = {left_data}, right = {right_data}, parent = {parent_data}")
print('')

# INSERT_LEFT -----------------------------------

my_parent = t.root.left.right
my_data = 9
print(f"Testing BinaryTree.insert_left({my_parent}, {my_data})...\n")
print(t)
t.insert_left(my_parent, my_data)
print(t, end='\n\n')
t = reset()

# INSERT_RIGHT ----------------------------------

my_parent = t.root.left.right
my_data = 9
print(f"Testing BinaryTree.insert_right({my_parent}, {my_data})...\n")
print(t)
t.insert_right(my_parent, my_data)
print(t, end='\n\n')
t = reset()

# REMOVE ----------------------------------------

my_node = t.root.right
print(f"Testing BinaryTree.remove({my_node})...\n")
print(t)
t.remove(my_node)
print(t, end='\n\n')
t = reset()

# GRAFT_LEFT ------------------------------------

my_root = t.root.right
my_scion = bt.BinaryTree(preorder=['A','B','C','D'],
                          inorder=['B','A','C','D'])
print(f"Testing BinaryTree.graft_left({t.root.right}, scion)...\n")
print(t)
t.graft_left(my_root, my_scion)
print(t, end='\n\n')
t = reset()

# GRAFT_RIGHT -----------------------------------

my_root = t.root.left.right
my_scion = bt.BinaryTree(preorder=['A','B','C','D'],
                          inorder=['B','A','C','D'])
print(f"Testing BinaryTree.graft_right({t.root.left.right}, scion)...\n")
print(t)
t.graft_right(my_root, my_scion)
print(t, end='\n\n')
t = reset()

# PRUNE -----------------------------------------

my_root = t.root.right
print(f"Testing BinaryTree.prune({my_root})...\n")
print(t)
t.prune(my_root)
print(t, end='\n\n')
t = reset()

# LOWEST_COMMON_ANCESTOR ------------------------

my_descendantA = t.root.left.right
my_descendantB = t.root.right.right
lca = t.lowest_common_ancestor(my_descendantA, my_descendantB)
if lca is None:
    lca_data = "None"
else:
    lca_data = str(lca.data)
print(f"Testing BinaryTree.lowest_common_ancestor({my_descendantA}, {my_descendantB})... it's {lca_data}!\n")
print(t, end='\n\n')

print("End of testing.")
