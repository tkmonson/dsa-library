from math import floor, log2

from adts import queue

class BTNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    # Included to support printing with BinaryTree.for_each_node.
    def __str__(self):
        return str(self.data)

class BinaryTree:
    # Should empty BTs be allowed? Tradeoffs.
    # BTs don't have indicies, so what should search return?
    # Preorder is like drawing Ls, inorder scans left-to-right, postorder is
    #     how you would build a pyramid, level-order is zig-zigs down.
    # In the context of graph theory, a tree is undirected and unrooted. In the
    #     context of computer science, specifically data structures, a tree is
    #     typically assumed to be an arborescence (a directed, rooted tree)
    #     with the additional structure of children being ordered (an ordered
    #     or plane tree). If a tree has parent pointers, it is undirected.
    # insert_left and insert_right input the parent (predecessor), while remove
    #     inputs the node to be removed (current). This is possible because of
    #     the parent pointers, similar to how linked lists can only remove
    #     using a current pointer if the nodes have prev pointers.
    # Empty/singleton/otherwise, Head/tail/middle <=> Root/leaf/internal

    # Duplicates? There's ambiguity in the tree structure if
    #     dups are allowed, I think.
    # It's biased toward the leftmost dup => it will construct
    #     the trees whose right sides have more elements. If
    #     there are more than 2 dups, this behavior will
    #     propagate recursively.
    # Duplicates are only a problem for trees that are not complete (so only a
    #     problem for two-argument constructors).
    # And, of course, trees can be modified after construction to have
    #     duplicates. The problem relates to instantiation.
    # To get duplicates working, constructors should be written to handle
    #     arrays of BTNodes. If you get arrays of ints instead, you can
    #     turn them into arrays of nodes (naturally, duplicates would
    #     not be allowed in this case).

    # Single-array construction assumes that the tree is complete.
    def __init__(self, preorder=[], inorder=[], postorder=[], levelorder=[]):
        truth_table = tuple(map(bool,
            (preorder, inorder, postorder, levelorder)))
        if sum(truth_table) == 0:
            self.root = None
            self.size = 0
            return
        if sum(truth_table) > 2:
            raise ValueError("Too many arguments, ya wanker!")

        # Preorder + inorder construction
        if truth_table == (1, 1, 0, 0):
            n = len(inorder)
            if len(preorder) != n:
                raise ValueError("Arrays have different lengths.")

            pre_index = 0
            in_dict = {}
            for i in range(n):
                in_dict[inorder[i]] = i

            def pre_in_construct(in_start, in_end):
                nonlocal preorder, in_dict, pre_index
                
                if in_start >= in_end:
                    return None

                root = BTNode(preorder[pre_index])
                pre_index += 1
                
                try:
                    partition_index = in_dict[root.data]
                except KeyError:
                    raise ValueError("Arrays do not represent a binary tree.")

                root.left = pre_in_construct(in_start, partition_index)
                if root.left is not None:
                    root.left.parent = root

                root.right = pre_in_construct(partition_index + 1, in_end)
                if root.right is not None:
                    root.right.parent = root

                return root

            self.root = pre_in_construct(0, n)
            self.size = n
            return

        # Inorder + postorder construction
        if truth_table == (0, 1, 1, 0):
            n = len(inorder)
            if len(postorder) != n:
                raise ValueError("Arrays have different lengths.")

            post_index = n - 1
            in_dict = {}
            for i in range(n):
                in_dict[inorder[i]] = i

            def in_post_construct(in_start, in_end):
                nonlocal postorder, in_dict, post_index
                
                if in_start >= in_end:
                    return None

                root = BTNode(postorder[post_index])
                post_index -= 1
                
                try:
                    partition_index = in_dict[root.data]
                except KeyError:
                    raise ValueError("Arrays do not represent a binary tree.")

                root.right = in_post_construct(partition_index + 1, in_end)
                if root.right is not None:
                    root.right.parent = root

                root.left = in_post_construct(in_start, partition_index)
                if root.left is not None:
                    root.left.parent = root

                return root

            self.root = in_post_construct(0, n)
            self.size = n
            return

        # Postorder + level-order construction
        if truth_table == (0, 1, 0, 1):
            n = len(inorder)
            if len(levelorder) != n:
                raise ValueError("Arrays have different lengths.")

            level_dict = {}
            for i in range(n):
                level_dict[levelorder[i]] = i

            def in_level_construct(in_start, in_end):
                nonlocal inorder, level_dict
                
                if in_start >= in_end:
                    return None

                in_index = in_start
                for i in range(in_start + 1, in_end):
                    if level_dict[inorder[i]] < level_dict[inorder[in_index]]:
                        in_index = i
                root = BTNode(inorder[in_index])
                
                partition_index = in_index

                root.left = in_level_construct(in_start, partition_index)
                if root.left is not None:
                    root.left.parent = root

                root.right = in_level_construct(partition_index + 1, in_end)
                if root.right is not None:
                    root.right.parent = root

                return root

            self.root = in_level_construct(0, n)
            self.size = n
            return

        # Preorder construction
        if truth_table == (1, 0, 0, 0):
            n = len(preorder)
            max_depth = floor(log2(n))
            max_depth_vacancy = n - (2 ** max_depth - 1)
            pre_index = 0
            def pre_construct(depth):
                nonlocal preorder, max_depth, max_depth_vacancy, pre_index, n

                if depth > max_depth or pre_index == n:
                    return None

                if depth == max_depth:
                    if max_depth_vacancy == 0:
                        return None
                    max_depth_vacancy -= 1

                root = BTNode(preorder[pre_index])
                pre_index += 1

                root.left = pre_construct(depth + 1)
                if root.left is not None:
                    root.left.parent = root

                root.right = pre_construct(depth + 1)
                if root.right is not None:
                    root.right.parent = root

                return root

            self.root = pre_construct(0)
            self.size = n
            return

        # Inorder construction
        if truth_table == (0, 1, 0, 0):
            n = len(inorder)
            max_depth = floor(log2(n))
            max_depth_vacancy = n - (2 ** max_depth - 1)
            in_index = 0
            def in_construct(depth):
                nonlocal inorder, max_depth, max_depth_vacancy, in_index, n

                if depth > max_depth or in_index == n:
                    return None

                if depth == max_depth:
                    if max_depth_vacancy == 0:
                        return None
                    max_depth_vacancy -= 1

                root = BTNode(None)

                root.left = in_construct(depth + 1)
                if root.left is not None:
                    root.left.parent = root

                root.data = inorder[in_index]
                in_index += 1

                root.right = in_construct(depth + 1)
                if root.right is not None:
                    root.right.parent = root

                return root

            self.root = in_construct(0)
            self.size = n
            return

        # Postorder construction
        if truth_table == (0, 0, 1, 0):
            n = len(postorder)
            max_depth = floor(log2(n))
            max_depth_vacancy = n - (2 ** max_depth - 1)
            post_index = 0
            def post_construct(depth):
                nonlocal postorder, max_depth, max_depth_vacancy, post_index, n

                if depth > max_depth or post_index == n:
                    return None

                if depth == max_depth:
                    if max_depth_vacancy == 0:
                        return None
                    max_depth_vacancy -= 1

                root = BTNode(None)

                root.left = post_construct(depth + 1)
                if root.left is not None:
                    root.left.parent = root

                root.right = post_construct(depth + 1)
                if root.right is not None:
                    root.right.parent = root

                root.data = postorder[post_index]
                post_index += 1

                return root

            self.root = post_construct(0)
            self.size = n
            return

        # Level-order construction
        if truth_table == (0, 0, 0, 1):
            n = len(levelorder)
            level_index = 1
            level_size = 1

            self.root = BTNode(levelorder[0])
            self.size = n

            q = queue.Queue([self.root])
            while level_index < n:
                for _ in range(level_size):
                    node = q.dequeue()

                    node.left = BTNode(levelorder[level_index])
                    node.left.parent = node
                    q.enqueue(node.left)
                    level_index += 1

                    if level_index == n:
                        break

                    node.right = BTNode(levelorder[level_index])
                    node.right.parent = node
                    q.enqueue(node.right)
                    level_index += 1
                level_size *= 2

            return

        raise ValueError("Wrong combo, dummy!")

    # This is not O(n) in time, it's O(h) (you have to factor in the printing
    #     of all of the empty spaces in the tree)
    # Only works for single-character data right now. Writing a version for
    #     data of arbitrary length would be hard. Would require preprocessing
    #     of the entire tree to fetch the lengths of each data field. This
    #     length data would then be used to produce a smallest-width string
    #     representation composed of variable-length links and spaces.
    def __str__(self):
        top_level = self.fold(self.height)
        level_strings = []

        def left_link_from_level(level):
            if level == 1:
                return ""
            def num_underscores(level):
                if level == 2:
                    return 0
                if level == 3:
                    return 1
                return 2 * num_underscores(level - 1) + 2
            return ''.join(["_" * num_underscores(level)]) + "/"

        def blank(link):
            return ''.join([" " * len(link)])

        q = queue.Queue()
        if self.root is not None:
            q.enqueue(self.root)
        # Should this actually be a height variable?
        # Or should these levels be zero-indexed?
        for level in range(top_level, 0, -1):
            data_strings = []
            link_strings = []
            level_size = q.size()

            for i in range(level_size):
                node = q.dequeue()
                if node is None:
                    data = " "
                    q.enqueue(None)
                    q.enqueue(None)
                else:
                    data = str(node.data)
                    q.enqueue(node.left)
                    q.enqueue(node.right)

                left_link = left_link_from_level(level)
                full_link = left_link + left_link.replace("/", "\\ ")[::-1]
                if node is None or (node.left is None and node.right is None):
                    left_link = blank(left_link)
                    full_link = blank(full_link)

                if i == 0:
                    data_indent = blank(full_link)
                    link_indent = blank(left_link) + " "
                    if level == 2:
                        data_indent = data_indent[1:]
                        link_indent = link_indent[1:] # and for h == 1 technically
                    data_strings.append(data_indent + data)
                    link_strings.append(link_indent + full_link)
                else:
                    internode_spacing = 2 * blank(full_link) + " "
                    interlink_spacing = blank(full_link) + 2 * " "
                    if level == 2:
                        internode_spacing = internode_spacing[2:]
                        interlink_spacing = interlink_spacing[2:]
                    if level == 1 and i % 2 == 1:
                        internode_spacing = 3 * " "
                    data_strings.append(internode_spacing + data)
                    link_strings.append(interlink_spacing + full_link)

            if level == 1:
                level_strings.append(''.join(data_strings))
            else:
                level_strings.append(''.join(data_strings + ["\n"]))
                level_strings.append(''.join(link_strings + ["\n"]))
        return ''.join(level_strings)

    def is_empty(self):
        return self.root == None

    # This is a generalized traverse.
    def for_each_node(self, callback, order="preorder"):
        def preorder(root):
            if root is None:
                return
            callback(root)
            preorder(root.left)
            preorder(root.right)
    
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            callback(root)
            inorder(root.right)
    
        def postorder(root):
            if root is None:
                return
            postorder(root.left)
            postorder(root.right)
            callback(root)

        def levelorder(root):
            q = queue.Queue()
            if root is not None:
                q.enqueue(root)
            while not q.is_empty():
                node = q.dequeue()
                callback(node)
                if node.left is not None:
                    q.enqueue(node.left)
                if node.right is not None:
                    q.enqueue(node.right)

        dispatcher = {"preorder": preorder, "inorder": inorder,
                      "postorder": postorder, "levelorder": levelorder}
        try:
            traverse = dispatcher[order]
            traverse(self.root)
        except KeyError:
            print("Invalid order given.")

    def fold(self, callback, start=0):
        def preorder(root, accumulator):
            if root is None:
                return accumulator
            return callback(root,
                    preorder(root.left, accumulator),
                    preorder(root.right, accumulator))
        return preorder(self.root, start)

    def to_list(self, order="preorder"):
        ret = []
        self.for_each_node(lambda n: ret.append(n.data), order=order)
        return ret

    def search(self, target, order="preorder"):
        def preorder(root, target):
            if root is None or root.data == target:
                return root
            a = preorder(root.left, target)
            if a is not None:
                return a
            return preorder(root.right, target)
    
        def inorder(root, target):
            if root is None:
                return root
            a = inorder(root.left, target)
            if a is not None:
                return a
            if root.data == target:
                return root
            return inorder(root.right, target)

        def postorder(root, target):
            if root is None:
                return root
            a = inorder(root.left, target)
            if a is not None:
                return a
            b = inorder(root.right, target)
            if b is not None:
                return b
            if root.data == target:
                return root

        def levelorder(root, target):
            q = queue.Queue()
            if root is not None:
                q.enqueue(root)
            while not q.is_empty():
                node = q.dequeue()
                if node.data == target:
                    return node
                if node.left is not None:
                    q.enqueue(node.left)
                if node.right is not None:
                    q.enqueue(node.right)

        dispatcher = {"preorder": preorder, "inorder": inorder,
                      "postorder": postorder, "levelorder": levelorder}
        try:
            _search = dispatcher[order]
            return _search(self.root, target)
        except KeyError:
            print("Invalid order given.")

    def insert_left(self, parent, data):
        temp = BTNode(data)
        if parent is None:
            if self.root is None:
                self.root = temp
            else:
                temp.left = self.root
                self.root.parent = temp
                self.root = temp
            return

        temp.left = parent.left
        if temp.left is not None:
            temp.left.parent = temp
        temp.parent = parent
        parent.left = temp

    def insert_right(self, parent, data):
        self.invert(parent)
        self.insert_left(parent, data)
        self.invert(parent.left)
        self.invert(parent)

    def remove(self, node):
        if node is None:  # return here instead?
            raise ValueError("Node to be removed does not exist.")
        if node.left is not None and node.right is not None:
            raise ValueError("Node to be removed has two children.")

        if node.left is None and node.right is None:
            node = None
            return

        if node.left is not None:
            child = node.left
        else:
            child = node.right

        child.parent = node.parent
        if node.parent is None:
            self.root = child
            return
        if node is node.parent.left:
            node.parent.left = child
        else:
            node.parent.right = child

    def graft_left(self, root, scion):
        if scion is None:
            return
        if root is None:
            return
        if root.left is None:
            root.left = scion.root
            scion.root.parent = root
        else:
            return # Occupado!

    def graft_right(self, root, scion):
        self.invert(root)
        self.graft_left(root, scion)
        self.invert(root)

    def prune(self, root):
        if root is None:
            return
        if root.parent is None:
            self.root = None
        if root is root.parent.left:
            root.parent.left = None
        else:
            root.parent.right = None

    # This can also be done without using parent pointers, but it would be
    #     slower: search for either dA or dB while storing the path data in a
    #     visited set; once you find one, search for the other specifically,
    #     storing path data in an array; iterate over the array, from
    #     descendant to root, and return the first node you encounter that is
    #     in the visited set.
    def lowest_common_ancestor(self, descendantA, descendantB):
        visited = set()
        current_node = descendantA
        while current_node is not None:
            visited.add(current_node)
            current_node = current_node.parent

        current_node = descendantB
        while current_node is not None:
            if current_node in visited:
                return current_node
            current_node = current_node.parent

        raise ValueError("Nodes do not share a common ancestor.")

# TRAVERSAL -------------------------------------------------------------------

    def invert(self, root):
        if root is not None:
            root.left, root.right = root.right, root.left

# FOLD ------------------------------------------------------------------------

    def height(self, root, left, right):
        return max(left, right) + 1

    def sum(self, root, left, right):
        return root.data + left + right

#class BinarySearchTree(BinaryTree):
#    def search(self, data):
#        pass

#    def insert(self, data):
#        pass

#    def remove(self, data):
#        pass

