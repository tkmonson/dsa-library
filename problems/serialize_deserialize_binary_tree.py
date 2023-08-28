'''
Serialize and Deserialize Binary Tree (#297)

Design algorithms to serialize and deserialize a binary tree. That is, design
an algorithm to convert a binary tree into a sequence of bits (a string) and an
algorithm to convert that sequence of bits back into the original binary tree.
'''

from collections import deque

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def serialize_recur(root: TreeNode | None) -> str:
    values = []
    def preorder(root):
        if not root:
            values.append('N')
            return

        values.append(str(root.val))
        preorder(root.left)
        preorder(root.right)

    preorder(root)

    return ','.join(values)


def serialize_stack(root: TreeNode | None) -> str:
    values = []

    stack = [root]
    while stack:
        root = stack.pop()
        if not root:
            values.append('N')
            continue

        values.append(str(root.val))
        stack.append(root.right)
        stack.append(root.left)

    return ','.join(values)


def deserialize_recur(data: str) -> TreeNode | None:
    values = iter(data.split(','))

    def preorder():
        if (v := next(values)) == 'N':
            return None

        root = TreeNode(v)
        root.left = preorder()
        root.right = preorder()

        return root

    return preorder()


def deserialize_stack(data: str) -> TreeNode | None:
    if data == 'N':
        return None

    values = iter(data.split(','))

    stack = [root := TreeNode(next(values))]
    while stack:
        node = stack.pop()
        v = next(values)
        if not node.left:
            stack.append(node)
            if v != 'N':
                node.left = TreeNode(int(v))
                stack.append(node.left)
            else:
                node.left = TreeNode(None)
        else:
            if node.left.val is None:
                node.left = None
            if v != 'N':
                node.right = TreeNode(int(v))
                stack.append(node.right)

    return root


if __name__ == '__main__':
    bt = TreeNode(4,
                  TreeNode(7, TreeNode(2), TreeNode(1)),
                  TreeNode(8, None, TreeNode(3, TreeNode(5), None))
                 )
    s = serialize_recur(bt)
    print(s)

    def preorder(root):
        if not root:
            print('None')
            return
        print(root.val)
        preorder(root.left)
        preorder(root.right)

    t = deserialize_recur(s)
    preorder(t)

'''
You have to store two kinds of information: the node values and the structure
of the tree. This can be done by traversing the tree via DFS and sequentially
writing node values or null values to a string. This can also be done by
traversing the tree via BFS and writing a null value for every "missing" node
(that is, null nodes and the "children" of null nodes), but this is generally
less space-efficient. DFS solutions are given above, in recursive and stack
implementations.
'''

