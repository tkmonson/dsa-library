from collections import defaultdict
from contextlib import suppress
import itertools
from math import floor, log2

from adts import queue

class BTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class BinaryTree:
    # In graph theory, a tree is an undirected, unrooted graph in which any two
    #     vertices are connected by exactly one path. In computer science, a
    #     tree is typically assumed to be an arborescence (a directed, rooted
    #     tree in which there is exactly one path from the root to any other
    #     node) whose children are ordered (that is, a child is distinguishable
    #     as left/right or 1st/2nd/.../Kth; that is, it is an ordered or plane
    #     tree). Thus, a binary tree is a bifurcating arborescence in which
    #     each node has at most two children. This implementation has parent
    #     pointers, which means that the tree is functionally undirected.
    #
    # The set of all binary trees may or may not include the empty tree. This
    #     implementation does allow for binary trees to be empty.
    #
    # There are four standard orders in which the nodes of a binary tree may
    #     be traversed: preorder, inorder, postorder, and level-order. Preorder
    #     is like drawing hockey sticks, inorder scans nodes from left to
    #     right, postorder is how you would build a pyramid, and level-order is
    #     top-to-bottom, left-to-right.
    #
    # If a binary tree is complete, its structure can be described by a single
    #     order. For non-complete binary trees with unique values, two orders
    #     are required to fully describe the structure, one of which must be
    #     inorder. For non-complete binary trees with duplicate values, two-
    #     order construction will be structurally ambiguous. In this case, one
    #     should instead use succinct construction, which inputs an order and a
    #     list representing the structure of the tree.
    #
    # __str__ only works for single-character data right now. Writing a version
    #     for data of arbitrary length would be hard. One potential solution
    #     would involve preprocessing the entire tree to fetch the lengths of
    #     each data field. This length data would then be used to produce a
    #     smallest-width string representation composed of variable-length
    #     links and spaces.
    #
    # This class has an interesting functional implementation of some of its
    #     methods: a traverse method is called to recursively propagate
    #     functions over a full or partial traversal of the tree's nodes, a
    #     fold method is called to accumulate the tree's nodes to produce a
    #     single value, and an ascend method is called to propagate functions
    #     over a path toward the root. Traverse, fold, and ascend cannot pass
    #     data in between nodes; if this is required, a custom method must be
    #     written (see, e.g., the width method).
    #
    # The traverse method takes both void functions (procedures), which operate
    #     on every node in the tree, and Boolean functions (predicates), which
    #     cease traversal upon returning True.
    #
    # The insert method inserts a node at the first null found in a level-order
    #     traversal. Subtypes of the binary tree like the binary search tree
    #     and the binary heap do not have a choice of insertion location, so
    #     this class cannot have a choice either (per Liskov Substitution
    #     Principle). See the UnsortedBinaryTree subclass for a more flexible
    #     insert method.
    #
    # Despite having a size attribute, this implementation also has an O(n)
    #     count method, provided for computing the size of subtrees.
    #
    # The height of a node is the number of edges on the longest path from that
    #     node to a leaf; the height of a tree is the height of its root node.
    #     The depth of a node is the number of edges from that node to the
    #     root; the maximum depth in a tree is equal to that tree's height. A
    #     level is a set of all the nodes of equal depth in a tree; level n
    #     contains all of the nodes of depth n; the level of a node is equal to
    #     its depth. The width of a tree is the size of its largest level.
    #
    # Without parent pointers, the lowest_common_ancestor algorithm would be
    #     slower: search for dA while storing path data in a visited set
    #     (backtracking where necessary), search for dB while storing path data
    #     in a list (backtracking where necessary), traverse the list from dB
    #     to root, return the first node contained in the visited set.

    # Time: O(n)
    # Auxiliary Space: O(1) for empty, pre, in, and post constructions,
    #                  O(n) for level and two-order constructions
    def __init__(self, preorder=[], inorder=[], postorder=[], levelorder=[]):
        selector = tuple(map(bool, (preorder, inorder, postorder, levelorder)))
        if sum(selector) > 2:
            raise ValueError("Constructor takes 0, 1, or 2 arguments.")

        # Empty construction
        if selector == (0, 0, 0, 0):
            self.root = None
            self.size = 0
            return

        # Preorder construction (complete tree)
        if selector == (1, 0, 0, 0):
            n = len(preorder)
            max_depth = floor(log2(n))
            last_level_vacancy = n - (2 ** max_depth - 1)
            pre_index = 0
            def pre_construct(depth):
                nonlocal pre_index, last_level_vacancy

                if depth > max_depth or pre_index == n:
                    return None

                if depth == max_depth:
                    if last_level_vacancy == 0:
                        return None
                    last_level_vacancy -= 1

                root = BTNode(preorder[pre_index])
                pre_index += 1

                root.left = pre_construct(depth + 1)
                with suppress(AttributeError):
                    root.left.parent = root

                root.right = pre_construct(depth + 1)
                with suppress(AttributeError):
                    root.right.parent = root

                return root

            self.root = pre_construct(0)
            self.size = n
            return

        # Inorder construction (complete tree)
        if selector == (0, 1, 0, 0):
            n = len(inorder)
            max_depth = floor(log2(n))
            last_level_vacancy = n - (2 ** max_depth - 1)
            in_index = 0
            def in_construct(depth):
                nonlocal in_index, last_level_vacancy

                if depth > max_depth or in_index == n:
                    return None

                if depth == max_depth:
                    if last_level_vacancy == 0:
                        return None
                    last_level_vacancy -= 1

                root = BTNode(None)

                root.left = in_construct(depth + 1)
                with suppress(AttributeError):
                    root.left.parent = root

                root.data = inorder[in_index]
                in_index += 1

                root.right = in_construct(depth + 1)
                with suppress(AttributeError):
                    root.right.parent = root

                return root

            self.root = in_construct(0)
            self.size = n
            return

        # Postorder construction (complete tree)
        if selector == (0, 0, 1, 0):
            n = len(postorder)
            max_depth = floor(log2(n))
            last_level_vacancy = n - (2 ** max_depth - 1)
            post_index = 0
            def post_construct(depth):
                nonlocal post_index, last_level_vacancy

                if depth > max_depth or post_index == n:
                    return None

                if depth == max_depth:
                    if last_level_vacancy == 0:
                        return None
                    last_level_vacancy -= 1

                root = BTNode(None)

                root.left = post_construct(depth + 1)
                with suppress(AttributeError):
                    root.left.parent = root

                root.right = post_construct(depth + 1)
                with suppress(AttributeError):
                    root.right.parent = root

                root.data = postorder[post_index]
                post_index += 1

                return root

            self.root = post_construct(0)
            self.size = n
            return

        # Level-order construction (complete tree)
        if selector == (0, 0, 0, 1):
            n = len(levelorder)
            level_index = 1
            level_size = 1

            self.root = BTNode(levelorder[0])
            self.size = n

            q = queue.Queue([self.root])
            while level_index < n:
                for _ in range(level_size):
                    root = q.dequeue()

                    root.left = BTNode(levelorder[level_index])
                    root.left.parent = root
                    q.enqueue(root.left)
                    level_index += 1

                    try:
                        root.right = BTNode(levelorder[level_index])
                    except IndexError:
                        break
                    root.right.parent = root
                    q.enqueue(root.right)
                    level_index += 1
                level_size *= 2
            return

        # By this point, we know that exactly two non-empty orders were given.
        two_orders = tuple(filter(bool,
            (preorder, inorder, postorder, levelorder)))
        if (n := len(two_orders[0])) != len(two_orders[1]):
            raise ValueError("Orders must have the same length.")

        not_bt_error = ValueError("Orders do not represent a binary tree.")

        # Preorder + inorder construction
        if selector == (1, 1, 0, 0):

            # A dictionary is utilized for its O(1) search time.
            inorder_value_to_index = {inorder[i]: i for i in range(n)}
            pre_index = 0

            def pre_in_construct(in_start, in_end):
                nonlocal pre_index
                
                if in_start >= in_end:
                    return None

                root = BTNode(preorder[pre_index])
                pre_index += 1
                
                # Find the index of the preorder value in the inorder sublist.
                try:
                    partition_index = inorder_value_to_index[root.data]
                except KeyError:
                    raise not_bt_error

                # Values in inorder[:index] belong to the left subtree.
                root.left = pre_in_construct(in_start, partition_index)
                with suppress(AttributeError):
                    root.left.parent = root

                # Values in inorder[index + 1:] belong to the left subtree.
                root.right = pre_in_construct(partition_index + 1, in_end)
                with suppress(AttributeError):
                    root.right.parent = root

                return root

            self.root = pre_in_construct(0, n)
            self.size = n
            return

        # Inorder + postorder construction
        if selector == (0, 1, 1, 0):

            # A dictionary is utilized for its O(1) search time.
            inorder_value_to_index = {inorder[i]: i for i in range(n)}
            post_index = n - 1

            def in_post_construct(in_start, in_end):
                nonlocal post_index
                
                if in_start >= in_end:
                    return None

                root = BTNode(postorder[post_index])
                post_index -= 1
                
                # Find the index of the postorder value in the inorder sublist.
                try:
                    partition_index = inorder_value_to_index[root.data]
                except KeyError:
                    raise not_bt_error

                # Values in inorder[index + 1:] belong to the right subtree.
                root.right = in_post_construct(partition_index + 1, in_end)
                with suppress(AttributeError):
                    root.right.parent = root

                # Values in inorder[:index] belong to the left subtree.
                root.left = in_post_construct(in_start, partition_index)
                with suppress(AttributeError):
                    root.left.parent = root

                return root

            self.root = in_post_construct(0, n)
            self.size = n
            return

        # Inorder + level-order construction
        if selector == (0, 1, 0, 1):

            # A dictionary is utilized for its O(1) search time.
            level_value_to_index = {levelorder[i]: i for i in range(n)}

            def in_level_construct(in_start, in_end):
                if in_start >= in_end:
                    return None

                # Find the index in the inorder sublist whose value has the
                # minimum index in the level-order list.
                in_index = in_start
                for i in range(in_start + 1, in_end):
                    try:
                        if (level_value_to_index[inorder[i]] <
                                level_value_to_index[inorder[in_index]]):
                            in_index = i
                    except KeyError:
                        raise not_bt_error

                root = BTNode(inorder[in_index])
                partition_index = in_index

                # Values in inorder[:index] belong to the left subtree.
                root.left = in_level_construct(in_start, partition_index)
                with suppress(AttributeError):
                    root.left.parent = root

                # Values in inorder[index + 1:] belong to the right subtree.
                root.right = in_level_construct(partition_index + 1, in_end)
                with suppress(AttributeError):
                    root.right.parent = root

                return root

            self.root = in_level_construct(0, n)
            self.size = n
            return

        raise ValueError("Given two lists, one must be inorder.")

    # Time: O(n)
    # Auxiliary Space: O(1) for preorder, O(n) for level-order
    @classmethod
    def succinct_construct(cls, structure, data, order="preorder"):
        if sum(structure) != len(data):
            raise ValueError("Wrong length of data list for given structure.")

        # Create an uninitialized BT, call its parent constructor.
        obj = cls.__new__(cls)
        super(BinaryTree, obj).__init__()

        # Empty construction
        if (not structure or not structure[0]) and not data:
            obj.root = None
            obj.size = 0
            return obj

        structure_index = 0
        data_index = 0

        def preorder():
            nonlocal structure_index, data_index

            try:
                root_exists = structure[structure_index]
            except IndexError:
                raise ValueError("Some structural information is missing.")
            structure_index += 1

            if root_exists:
                root = BTNode(data[data_index])
                data_index += 1
            else:
                return None

            root.left = preorder()
            with suppress(AttributeError):
                root.left.parent = root

            root.right = preorder()
            with suppress(AttributeError):
                root.right.parent = root

            return root

        def levelorder():
            nonlocal structure_index, data_index
            q = queue.Queue()
            q.enqueue(top_root := BTNode(data[data_index]))
            structure_index += 1
            data_index += 1
            while not q.is_empty():
                root = q.dequeue()

                try:
                    left_exists = structure[structure_index]
                    right_exists = structure[structure_index + 1]
                except IndexError:
                    raise ValueError("Some structural information is missing.")
                structure_index += 2

                if left_exists:
                    root.left = BTNode(data[data_index])
                    data_index += 1
                    root.left.parent = root
                    q.enqueue(root.left)

                if right_exists:
                    root.right = BTNode(data[data_index])
                    data_index += 1
                    root.right.parent = root
                    q.enqueue(root.right)

            return top_root

        dispatcher = {"preorder": preorder, "levelorder": levelorder}
        try:
            _construct = dispatcher[order]
        except KeyError:
            raise ValueError("Invalid order given.")

        obj.root = _construct()
        obj.size = len(data)
        return obj

    # Time: O(2^h) (the number of nodes in a complete tree of height h)
    # Auxiliary Space: O(2^h)
    def __str__(self):
        if self.is_empty():
            return ""

        max_depth = self.height()
        leftmost_node_depth = self.fold(lambda root, left, right: left + 1) - 1

        def create_double_link(depth):
            height_wrt_baseline = max_depth - depth

            if height_wrt_baseline == 0:
                return ""
            if height_wrt_baseline == 1:
                return "/ \\"

            def num_underscores(height_wrt_baseline):
                if height_wrt_baseline == 2:
                    return 1
                return 2 * num_underscores(height_wrt_baseline - 1) + 2

            left_link = "_" * num_underscores(height_wrt_baseline) + "/"
            return left_link + left_link.replace("/", "\\ ")[::-1]

        def blank(link):
            return " " * len(link)

        level_strings = []
        q = queue.Queue()
        q.enqueue(self.root)
        for depth in range(max_depth + 1):
            data_strings = []
            link_strings = []

            double_link = create_double_link(depth)
            interdata_spacing = blank(create_double_link(depth - 1))
            interlink_spacing = blank(double_link) + 2 * " "
            if depth == max_depth - 1:
                interlink_spacing = interlink_spacing[2:]

            for row_position in range(level_capacity := 2 ** depth):
                if (root := q.dequeue()) is None:
                    data = " "
                    q.enqueue(None)
                    q.enqueue(None)
                else:
                    data = str(root.data)
                    q.enqueue(root.left)
                    q.enqueue(root.right)

                # Nulls and leaves don't print links, other nodes do.
                link = double_link
                if root is None or (root.left is None and root.right is None):
                    link = blank(link)

                # Last level: spacing is 3 between siblings, 1 between cousins.
                if depth == max_depth:
                    interdata_spacing = 3 * " " if row_position % 2 else " "

                if row_position == 0:
                    data_indent = " " * (len(interdata_spacing) // 2)
                    link_indent = " " * (len(interlink_spacing) // 2)
                    data_strings.append(data_indent + data)
                    link_strings.append(link_indent + link)

                    # Find length of excess whitespace on the left.
                    if depth == leftmost_node_depth:
                        if root.right is None:  # root is leaf
                            indent_offset = len(data_indent)
                        else:
                            indent_offset = len(link_indent)
                else:
                    data_strings.append(interdata_spacing + data)
                    link_strings.append(interlink_spacing + link)

            level_strings.append(''.join(data_strings + ["\n"]))
            level_strings.append(''.join(link_strings + ["\n"]))

        # Trim left whitespace such that the leftmost node has an indent of 0.
        level_strings = [level[indent_offset:] for level in level_strings]

        # Trim \n from last data level, trim last link level from final string.
        level_strings[-2] = level_strings[-2][:-1]
        return ''.join(level_strings[:-1])

    # Time: O(n)
    # Auxiliary Space: O(1)
    def __eq__(self, other):
        if type(self) is not type(other):
            return False

        def preorder(self_node, other_node):
            if self_node is None and other_node is None:
                return True
            if self_node is None or other_node is None:
                return False
            return (self_node.data == other_node.data
                and preorder(self_node.left, other_node.left)
                and preorder(self_node.right, other_node.right))

        return preorder(self.root, other.root)

    # Time: O(1)
    # Auxiliary Space: O(1)
    def is_empty(self):
        return self.size == 0

    # TRAVERSAL ---------------------------------------------------------------

    # Time: O(n) (for full traversals)
    # Auxiliary Space: O(1) for DFS, O(n) for BFS
    def traverse(self, callback, root=None, order="preorder",
            visit_nulls=False):
        def preorder(root):
            if root is None:
                if visit_nulls:
                    callback(root)
                return
            if callback(root) or preorder(root.left) or preorder(root.right):
                return True

        def inorder(root):
            if root is None:
                if visit_nulls:
                    callback(root)
                return
            if inorder(root.left) or callback(root) or inorder(root.right):
                return True

        def postorder(root):
            if root is None:
                if visit_nulls:
                    callback(root)
                return
            if postorder(root.left) or postorder(root.right) or callback(root):
                return True

        def levelorder(root):
            q = queue.Queue()
            if root is not None:
                q.enqueue(root)
            while not q.is_empty():
                root = q.dequeue()
                if callback(root):
                    break
                with suppress(AttributeError):
                    if root.left is not None or visit_nulls:
                        q.enqueue(root.left)
                    if root.right is not None or visit_nulls:
                        q.enqueue(root.right)

        dispatcher = {"preorder": preorder, "inorder": inorder,
                      "postorder": postorder, "levelorder": levelorder}
        try:
            _traverse = dispatcher[order]
        except KeyError:
            raise ValueError("Invalid traversal order given.")
        _traverse(self.root if root is None else root)

    # Time: O(n)
    # Auxiliary Space: O(n)
    def list_traversal_order(self, order):
        res = []
        self.traverse(lambda r: res.append(r.data), order=order)
        return res

    # Time: O(n)
    # Auxiliary Space: O(n)
    def list_tree_structure(self, order):
        res = []
        self.traverse(lambda r: res.append(0) if r is None else res.append(1),
            order=order, visit_nulls=True)
        return res

    # Time: O(n)
    # Auxiliary Space: O(1) for DFS, O(n) for BFS
    def search(self, target, order="preorder"):
        res = []
        def target_found(root):
            if root.data == target:
                res.append(root)
                return True
            return False
        self.traverse(target_found, order=order)
        return res[0] if res else None

    # Time: O(n)
    # Auxiliary Space: O(h)
    def width(self, root=None):
        if root is None:
            root = self.root

        level_widths = defaultdict(int)
        def preorder(root, level_index):
            if root is None:
                return
            level_widths[level_index] += 1
            preorder(root.left, level_index + 1)
            preorder(root.right, level_index + 1)

        preorder(root, 0)
        try:
            return max(level_widths.values())
        except ValueError:
            return 0  # empty tree

    # MUTATORS ----------------------------------------------------------------

    # Time: O(n)
    # Auxiliary Space: O(n)
    def insert(self, data):
        def insertion_completed(root):
            if root.left is None:
                new = BTNode(data)
                root.left = new
                new.parent = root
                return True
            if root.right is None:
                new = BTNode(data)
                root.right = new
                new.parent = root
                return True
            return False
        self.traverse(insertion_completed, order="levelorder")

    # Time: O(1)
    # Auxiliary Space: O(1)
    def remove(self, root):
        if root.left is not None and root.right is not None:
            raise ValueError("Node to be removed has two children.")

        # If not left, child is either right or None.
        child = root.left if root.left is not None else root.right
        with suppress(AttributeError):
            child.parent = root.parent

        if root.parent is None:
            self.root = child
        elif root is root.parent.left:
            root.parent.left = child
        else:
            root.parent.right = child
        self.size -= 1

    # ACCUMULATION ------------------------------------------------------------

    # Time: O(n)
    # Auxiliary Space: O(1)
    def fold(self, callback, root=None, start=0):
        if root is None:
            root = self.root

        def preorder(root, accumulator):
            if root is None:
                return accumulator
            return callback(root,
                    preorder(root.left, accumulator),
                    preorder(root.right, accumulator))
        
        return preorder(root, start)

    # Time: O(n)
    # Auxiliary Space: O(1)
    def sum(self, root=None):
        return self.fold(lambda root, left, right: root.data + left + right,
                         root=root)

    # Time: O(n)
    # Auxiliary Space: O(1)
    def count(self, root=None):
        if root is None or root is self.root:
            return self.size
        return self.fold(lambda root, left, right: 1 + left + right,
                         root=root)

    # Time: O(n)
    # Auxiliary Space: O(1)
    def height(self, root=None):
        return self.fold(lambda root, left, right: 1 + max(left, right),
                         root=root) - 1

    # ASCENSION ---------------------------------------------------------------

    # Time: O(d)
    # Auxiliary Space: O(1)
    def ascend(self, callback, root):
        while root is not None:
            if callback(root):
                break
            root = root.parent

    # Time: O(d)
    # Auxiliary Space: O(1)
    def depth(self, root):
        counter = itertools.count(-1)
        def iterate(root):
            next(counter)
        self.ascend(iterate, root)
        return next(counter)

    # Time: O(d)
    # Auxiliary Space: O(1)
    def level(self, root):
        return self.depth(root)

    # Time: O(d) where d is the depth of the deeper descendant
    # Auxiliary Space: O(d_A) where d_A is the depth of descendant A
    def lowest_common_ancestor(self, descendantA, descendantB):
        visited = set()
        res = []
        def lca_found(root):
            if root in visited:
                res.append(root)
                return True
            return False

        self.ascend(lambda r: visited.add(r), descendantA)
        self.ascend(lca_found, descendantB)
        return res[0] if res else None


class UnsortedBinaryTree(BinaryTree):
    # Curiously, an UnsortedBinaryTree can be sorted. The "unsorted" descriptor
    #     denotes that there is no structural requirement that elements be
    #     sorted in any particular way. As such, this class contains mutator
    #     methods that cannot be inherited by subtypes of BinaryTree that do
    #     have a structural requirement for sorted elements, such as the binary
    #     search tree or binary heap.

    # Time: O(1)
    # Auxiliary Space: O(1)
    def invert(self, root):  # can be propagated through traverse/ascend
        root.left, root.right = root.right, root.left

    # Time: O(1)
    # Auxiliary Space: O(1)
    def insert(self, data, parent=None, right=False):
        if right:
            self.invert(parent)

        new = BTNode(data)
        try:
            new.left = parent.left
        except AttributeError:  # inserting at self.root
            new.left = self.root
            with suppress(AttributeError):
                self.root.parent = new
            self.root = new
        with suppress(AttributeError):
            new.left.parent = new
        new.parent = parent
        parent.left = new

        if right:
            self.invert(parent.left)
            self.invert(parent)

    # Time: O(1)
    # Auxiliary Space: O(1)
    def graft(self, root, scion, right=False):
        if not right and root.left is None:
            root.left = scion.root
        elif right and root.right is None:
            root.right = scion.root
        else:
            raise ValueError("Grafting location is occupied.")

        with suppress(AttributeError):
            scion.root.parent = root
        self.size += scion.size

    # Time: O(n) (because of the call to count)
    # Auxiliary Space: O(1)
    def prune(self, root):
        if root.parent is None:
            self.root = None
            self.size = 0
            return

        if root is root.parent.left:
            root.parent.left = None
        else:
            root.parent.right = None

        pruned_branch_size = self.count(root)
        self.size -= pruned_branch_size


class BinarySearchTree(BinaryTree):
    # Time: O(n)
    # Auxiliary Space: O(1) for empty, pre, in, and post constructions,
    #                  O(n) for level and two-order constructions
    def __init__(self, preorder=[], inorder=[], postorder=[], levelorder=[]):
        super().__init__(preorder, inorder, postorder, levelorder)
        if not self._is_BST():
            raise ValueError("Orders do not represent a binary search tree.")

    # Time: O(n)
    # Auxiliary Space: O(1) for preorder, O(n) for level-order
    @classmethod
    def succinct_construct(cls, structure, data, order="preorder"):
        tree = super().succinct_construct(structure, data, order)
        if not tree._is_BST():
            raise ValueError("Orders do not represent a binary search tree.")
        return tree
        
    # Time: O(n)
    # Auxiliary Space: O(1)
    def _is_BST(self):
        def _is_BST_helper(root, min_data, max_data):
            if root is None:
                return True
            with suppress(TypeError):
                if root.data < min_data or root.data > max_data:
                    return False
    
            return (_is_BST_helper(root.left, min_data, root.data)
                and _is_BST_helper(root.right, root.data, max_data))

        return _is_BST_helper(self.root, None, None)

    # Time: O(logn) for binary search, O(n) otherwise
    # Auxiliary Space: O(1)
    def search(self, target, order="binary"):
        if order != "binary":
            return super().search(target, order=order)

        def binary_search(root):
            if root is None or root.data == target:
                return root
            if target < root.data:
                return binary_search(root.left)
            else:
                return binary_search(root.right)

        return binary_search(self.root)

    # Time: O(h)
    # Auxiliary Space: O(1)
    def insert(self, data):
        if self.is_empty():
            self.root = BTNode(data)
            return

        def binary_insert(root):
            if data < root.data:
                if root.left is None:
                    root.left = BTNode(data)
                    root.left.parent = root
                    return
                binary_insert(root.left)
            else:
                if root.right is None:
                    root.right = BTNode(data)
                    root.right.parent = root
                    return
                binary_insert(root.right)

        binary_insert(self.root)
        self.size += 1

    # Time: O(h)
    # Auxiliary Space: O(1)
    def remove(self, root):
        if root.left is not None and root.right is not None:
            inorder_successor = root.right
            while inorder_successor.left is not None:
                inorder_successor = inorder_successor.left
            root.data = inorder_successor.data
            root = inorder_successor

        super().remove(root)

