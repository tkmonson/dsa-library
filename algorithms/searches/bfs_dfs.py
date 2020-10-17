class BinaryTree:
    def __init__(self, d=None):
        self.data = d
        self.left = None
        self.right = None

def bfs(root):
    res = []
    queue = []
    if root is not None:
        queue.append(root)
    while queue:
        current = queue.pop(0)
        res.append(current.data)
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    return res

def dfs_preorder(root):
    res = []
    def traverse(current):
        if current is None:
            return
        res.append(current.data)
        traverse(current.left)
        traverse(current.right)
    traverse(root)
    return res

def dfs_inorder(root):
    res = []
    def traverse(current):
        if current is None:
            return
        traverse(current.left)
        res.append(current.data)
        traverse(current.right)
    traverse(root)
    return res

def dfs_postorder(root):
    res = []
    def traverse(current):
        if current is None:
            return
        traverse(current.left)
        traverse(current.right)
        res.append(current.data)
    traverse(root)
    return res

if __name__ == "__main__":

    tree = BinaryTree(7)
    
    tree.left = BinaryTree(4)
    tree.right = BinaryTree(5)
    
    tree.left.left = BinaryTree(1)
    tree.left.right = BinaryTree(9)
    tree.right.left = BinaryTree(8)
    
    print("BFS: " + str(bfs(tree)))
    print("DFS pre: " + str(dfs_preorder(tree)))
    print("DFS in: " + str(dfs_inorder(tree)))
    print("DFS post: " + str(dfs_postorder(tree)))
