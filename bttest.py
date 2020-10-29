import unittest

from structures import binarytree as bt

class TestBinaryTree(unittest.TestCase):
    my_preorder      = [4,7,2,1,8,3,5]
    my_inorder       = [2,7,1,4,8,5,3]
    my_postorder     = [2,1,7,5,3,8,4]
    my_levelorder    = [4,7,8,2,1,3,5]
    my_pre_structure = [1,1,1,0,0,1,0,0,1,0,1,1,0,0,0]
    my_lev_structure = [1,1,1,1,1,0,1,0,0,0,0,1,0,0,0]

    def setUp(self):
        self.tree = bt.BinaryTree(
            preorder=self.__class__.my_preorder,
            inorder=self.__class__.my_inorder)

    def test_0_is_empty(self):
        self.assertEqual(self.tree.is_empty(), False)

    def test_1_list_traversal_order(self):
        self.assertEqual(
            self.tree.list_traversal_order("preorder"),
            self.__class__.my_preorder)
        self.assertEqual(
            self.tree.list_traversal_order("inorder"),
            self.__class__.my_inorder)
        self.assertEqual(
            self.tree.list_traversal_order("postorder"),
            self.__class__.my_postorder)
        self.assertEqual(
            self.tree.list_traversal_order("levelorder"),
            self.__class__.my_levelorder)

    def test_2_list_tree_structure(self):
        self.assertEqual(
            self.tree.list_tree_structure("preorder"),
            self.__class__.my_pre_structure)
        self.assertEqual(
            self.tree.list_tree_structure("levelorder"),
            self.__class__.my_lev_structure)

    def test_3_search(self):
        my_node = self.tree.root.left.right
        self.assertIs(self.tree.search(1, "preorder"), my_node)
        self.assertIs(self.tree.search(1, "inorder"), my_node)
        self.assertIs(self.tree.search(1, "postorder"), my_node)
        self.assertIs(self.tree.search(1, "levelorder"), my_node)

    def test_4_width(self):
        self.assertEqual(self.tree.width(), 3)

    def test_5_insert(self):
        resultant_tree = bt.BinaryTree(
            preorder=[4,7,2,1,8,9,3,5],
            inorder=[2,7,1,4,9,8,5,3])
        self.tree.insert(9)

        self.assertEqual(self.tree, resultant_tree)

    def test_6_remove(self):
        resultant_tree = bt.BinaryTree(
            preorder=[4,7,2,1,3,5],
            inorder=[2,7,1,4,5,3])
        self.tree.remove(self.tree.root.right)

        self.assertEqual(self.tree, resultant_tree)

    def test_7_sum(self):
        self.assertEqual(self.tree.sum(), 30)

    def test_8_count(self):
        self.assertEqual(self.tree.count(), 7)

    def test_9_height(self):
        self.assertEqual(self.tree.height(), 3)

    def test_A_depth(self):
        my_node = self.tree.root.left.right
        self.assertEqual(self.tree.depth(my_node), 2)

    def test_B_level(self):
        my_node = self.tree.root.left
        self.assertEqual(self.tree.level(my_node), 1)

    def test_C_lowest_common_ancestor(self):
        my_dA = self.tree.root.left.right
        my_dB = self.tree.root.right.right
        self.assertIs(
            self.tree.lowest_common_ancestor(my_dA, my_dB),
            self.tree.root)

class TestUnsortedBinaryTree(unittest.TestCase):
    def setUp(self):
        my_preorder      = [4,7,2,1,8,3,5]
        my_inorder       = [2,7,1,4,8,5,3]
        my_postorder     = [2,1,7,5,3,8,4]
        my_levelorder    = [4,7,8,2,1,3,5]
        my_pre_structure = [1,1,1,0,0,1,0,0,1,0,1,1,0,0,0]
        my_lev_structure = [1,1,1,1,1,0,1,0,0,0,0,1,0,0,0]

        self.tree = bt.UnsortedBinaryTree(
            preorder=my_preorder,
            inorder=my_inorder)

    def test_0_invert(self):
        resultant_tree = bt.UnsortedBinaryTree(
            preorder=[4,8,3,5,7,1,2],
            inorder=[3,5,8,4,1,7,2])
        self.tree.traverse(self.tree.invert)

        self.assertEqual(self.tree, resultant_tree)

    def test_1_insert_left(self):
        resultant_tree = bt.UnsortedBinaryTree(
            preorder=[4,7,2,1,9,8,3,5],
            inorder=[2,7,9,1,4,8,5,3])
        self.tree.insert(9, parent=self.tree.root.left.right)

        self.assertEqual(self.tree, resultant_tree)

    def test_2_insert_right(self):
        resultant_tree = bt.UnsortedBinaryTree(
            preorder=[4,7,2,1,9,8,3,5],
            inorder=[2,7,1,9,4,8,5,3])
        self.tree.insert(9, parent=self.tree.root.left.right, right=True)

        self.assertEqual(self.tree, resultant_tree)

    def test_3_graft_left(self):
        my_scion = bt.BinaryTree(
            preorder=['A','B','C','D'],
            inorder=['B','A','C','D'])
        resultant_tree = bt.UnsortedBinaryTree(
            preorder=[4,7,2,1,8,'A','B','C','D',3,5],
            inorder=[2,7,1,4,'B','A','C','D',8,5,3])
        self.tree.graft(self.tree.root.right, my_scion)

        self.assertEqual(self.tree, resultant_tree)

    def test_4_graft_right(self):
        my_scion = bt.BinaryTree(
            preorder=['A','B','C','D'],
            inorder=['B','A','C','D'])
        resultant_tree = bt.UnsortedBinaryTree(
            preorder=[4,7,2,1,'A','B','C','D',8,3,5],
            inorder=[2,7,1,'B','A','C','D',4,8,5,3])
        self.tree.graft(self.tree.root.left.right, my_scion, right=True)

        self.assertEqual(self.tree, resultant_tree)

    def test_4_prune(self):
        resultant_tree = bt.UnsortedBinaryTree(
            preorder=[4,7,2,1],
            inorder=[2,7,1,4])
        self.tree.prune(self.tree.root.right)

        self.assertEqual(self.tree, resultant_tree)

if __name__ == "__main__":
    unittest.main()

