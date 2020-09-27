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

# One-argument constructions
print("Preorder construction:")
print(bt.BinaryTree(preorder=my_preorder), end='\n\n')
print("Inorder construction:")
print(bt.BinaryTree(inorder=my_inorder), end='\n\n')
print("Postorder construction:")
print(bt.BinaryTree(postorder=my_postorder), end='\n\n')
print("Level-order construction:")
print(bt.BinaryTree(levelorder=my_levelorder), end='\n\n')

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

# Succinct constructions
print("Succinct preorder construction:")
print(bt.BinaryTree.succinct_construct(
    structure=[1,1,1,0,0,1,0,0,1,0,1,1,0,0,0],
    data=[4,7,2,1,8,3,5],
    order="preorder"))
print("Succinct level-order construction:")
print(bt.BinaryTree.succinct_construct(
    structure=[1,1,1,1,1,0,1,0,0,0,0,1,0,0,0],
    data=[4,7,8,2,1,3,5],
    order="levelorder"))

# Now go forward with one of the above trees
def reset(cls=bt.UnsortedBinaryTree):
    return cls(preorder=my_preorder,
               inorder=my_inorder)
t = reset()
print("This is your input tree for all of the following method tests:\n")
print(t, end='\n\n')

print(f"Testing BinaryTree.is_empty... it\'s {t.is_empty()}!\n")

print("Testing BinaryTree.list_traversal_order...\n")
print(f"pre:   {t.list_traversal_order('preorder')}")
print(f"in:    {t.list_traversal_order('inorder')}")
print(f"post:  {t.list_traversal_order('postorder')}")
print(f"level: {t.list_traversal_order('levelorder')}\n")

print("Testing BinaryTree.list_tree_structure...\n")
print(f"pre:   {t.list_tree_structure('preorder')}")
print(f"in:    {t.list_tree_structure('inorder')}")
print(f"post:  {t.list_tree_structure('postorder')}")
print(f"level: {t.list_tree_structure('levelorder')}\n")

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

t = reset(cls=bt.BinaryTree)
my_data = 9
print(f"Testing BinaryTree.insert({my_data})...\n")
print(t)
t.insert(my_data)
print(t, end='\n\n')
t = reset()

my_node = t.root.right
print(f"Testing BinaryTree.remove({my_node.data})...\n")
print(t)
t.remove(my_node)
print(t, end='\n\n')
t = reset()

print(f"Testing BinaryTree.fold(BinaryTree.height)... it's {t.fold(t.height)}!\n")

print(f"Testing BinaryTree.fold(BinaryTree.sum)... it's {t.fold(t.sum)}!\n")

print(f"Testing BinaryTree.fold(BinaryTree.count)... it's {t.fold(t.count)}!\n")

print(f"Testing BinaryTree.fold(BinaryTree.left_width)... it's {t.fold(t.left_width)}!\n")

print(f"Testing BinaryTree.fold(BinaryTree.right_width)... it's {t.fold(t.right_width)}!\n")

my_root = t.root.left.right
print(f"Testing BinaryTree.depth({my_root.data})... it's {t.depth(my_root)}!\n")

my_root = t.root.left.right
print(f"Testing BinaryTree.level({my_root.data})... it's {t.level(my_root)}!\n")

my_descendantA = t.root.left.right
my_descendantB = t.root.right.right
lca = t.lowest_common_ancestor(my_descendantA, my_descendantB)
lca_data = str(lca.data) if lca is not None else "None"
print(f"Testing BinaryTree.lowest_common_ancestor({my_descendantA.data}, {my_descendantB.data})... it's {lca_data}!\n")
print(t, end='\n\n')

print("Testing BinaryTree.traverse(UnsortedBinaryTree.invert)...\n")
print(t)
t.traverse(t.invert)
print(t, end='\n\n')
t = reset()

my_data = 9
my_parent = t.root.left.right
print(f"Testing UnsortedBinaryTree.insert({my_data}, {my_parent.data}, right=False)...\n")
print(t)
t.insert(my_data, my_parent, right=False)
print(t, end='\n\n')
t = reset()

my_data = 9
my_parent = t.root.left.right
print(f"Testing UnsortedBinaryTree.insert({my_data}, {my_parent.data}, right=True)...\n")
print(t)
t.insert(my_data, my_parent, right=True)
print(t, end='\n\n')
t = reset()

my_root = t.root.right
my_scion = bt.UnsortedBinaryTree(preorder=['A','B','C','D'],
                                 inorder=['B','A','C','D'])
print(f"Testing UnsortedBinaryTree.graft({my_root.data}, scion, right=False)...\n")
print(t)
t.graft(my_root, my_scion, right=False)
print(t, end='\n\n')
t = reset()

my_root = t.root.left.right
my_scion = bt.UnsortedBinaryTree(preorder=['A','B','C','D'],
                                 inorder=['B','A','C','D'])
print(f"Testing UnsortedBinaryTree.graft({my_root.data}, scion, right=True)...\n")
print(t)
t.graft(my_root, my_scion, right=True)
print(t, end='\n\n')
t = reset()

my_root = t.root.right
print(f"Testing BinaryTree.prune({my_root.data})...\n")
print(t)
t.prune(my_root)
print(t, end='\n\n')
t = reset()

print("End of testing.")
