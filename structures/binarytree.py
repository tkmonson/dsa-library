class BTNode:
    def __init__(self, data):
        self.data = data
        # self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=[]):
        self.root = None

    def __str__(self):
        self.traverse()

    def is_empty(self):
        return self.root == None

    def add_node(self, data):
        def dfs(node):
            if node is None:
                return BTNode(data)
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return node
        
        self.root = dfs(self.root)

    def traverse(self, myfunc, order="preorder"):
        if order == "preorder":
            self.preorder(self.root, myfunc)
        elif order == "inorder":
            self.inorder(myfunc)
        elif order == "postorder":
            self.postorder(myfunc)
        elif order == "levelorder":
            self.levelorder(myfunc)
        else:
            raise ValueError("Invalid order specified.")

    def preorder(self, node, myfunc=print):
        if node is None:
            return
        
        myfunc(node)
        self.preorder(node.left, myfunc)
        self.preorder(node.right, myfunc)

    def inorder(self, node, myfunc=print):
        if node is None:
            return

        self.inorder(node.left, myfunc)
        myfunc(node)
        self.inorder(node.right, myfunc)

    def postorder(self, node, myfunc=print):
        if node is None:
            return

        self.postorder(node.left)
        self.postorder(node.right)
        myfunc(node)

    def levelorder(self, myfunc=print):
        # Implement a queue first, then write a breadth-first traversal
        pass

#    def search(self, data, order="preorder"):
#        # Return value => reduce?
#        def _search(node):
#            if node.data == data:
#                return True
#            return False

#        self.traverse(_search, order)

    def insert(self, data, order="preorder"):
        # Input parent node or some kind of code like 'LRLRLL'?
        # Only input data, insert at first None encountered in some order?
        # Both? But the code is optional and the None idea is default?
        def _insert():
            if self.root is None:
                self.root = BTNode(data)
                return True
            return False

        self.traverse(_insert, "levelorder")

#    def remove(self, data):
        # Optional order parameter?
#        pass

    def invert(self):
        def reverse(node):
            node.left, node.right = node.right, node.left
        self.traverse(reverse)

#    def lowest_common_ancestor(self, descendantA, descendantB):
#        pass

#class BinarySearchTree(BinaryTree):
#    def search(self, data):
#        pass

#    def insert(self, data):
#        pass

#    def remove(self, data):
#        pass

