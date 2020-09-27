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
    # Discuss grafting terminology.
    # Why is size an attribute rather than a method based on traverse or fold?
    #     Because it gives you O(1) access. The count method is O(n), but it
    #     can be used to compute the size of subtrees.
    # Talk about raising exceptions vs. returning None. If you know the answer,
    #     return early. If you don't know the answer, and there is no point in
    #     continuing the computation because it's not going to get an answer,
    #     raise an exception. Sometimes the decision is between convenience for
    #     the user (no null checks, fewer possible exceptions, nop behavior)
    #     and semantic correctness (you shouldn't attempt to remove None from a
    #     tree, here's an exception telling you not to do that and why).
    # LCA: This can also be done without using parent pointers, but it would be
    #     slower: search for either dA or dB while storing the path data in a
    #     visited set; once you find one, search for the other specifically,
    #     storing path data in an array; iterate over the array, from
    #     descendant to root, and return the first node you encounter that is
    #     in the visited set.
    # STR: Only works for single-character data right now. Writing a version
    #     for data of arbitrary length would be hard. Would require
    #     preprocessing of the entire tree to fetch the lengths of each data
    #     field. This length data would then be used to produce a
    #     smallest-width string representation composed of variable-length
    #     links and spaces.
    # Single-array construction assumes that the tree is complete.
    # Level, depth, height, width

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
    # Succinct data structures allow for duplicates.

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

    # Time: O(2^h) (the number of nodes in a *complete* tree of height h)
    # Auxiliary Space:
    def __str__(self):
        if self.is_empty():
            return ""

        max_height = self.fold(self.height)
        max_depth = max_height - 1
        leftmost_node_depth = self.fold(self.left_width) - 1
        level_strings = []

        def create_double_link(depth):
            height_wrt_baseline = max_height - depth
            if height_wrt_baseline == 1:
                return ""

            def num_underscores(height_wrt_baseline):
                if height_wrt_baseline == 2:
                    return 0
                if height_wrt_baseline == 3:
                    return 1
                return 2 * num_underscores(height_wrt_baseline - 1) + 2

            left_link = "_" * num_underscores(height_wrt_baseline) + "/"
            return left_link + left_link.replace("/", "\\ ")[::-1]

        def blank(link):
            return " " * len(link)

        q = queue.Queue()
        q.enqueue(self.root)
        for depth in range(max_height):
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
                        indent_offset = len(data_indent)
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

    def is_empty(self):
        return self.size == 0

# TRAVERSAL -------------------------------------------------------------------

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

    def list_traversal_order(self, order):
        res = []
        self.traverse(lambda r: res.append(r.data), order=order)
        return res

    def list_tree_structure(self, order):
        res = []
        self.traverse(lambda r: res.append(0) if r is None else res.append(1),
            order=order, visit_nulls=True)
        return res

    def search(self, target, order="preorder"):
        res = []
        def target_found(root):
            if root.data == target:
                res.append(root)
                return True
            return False
        self.traverse(target_found, order=order)
        return res[0] if res else None

# MUTATORS --------------------------------------------------------------------

    def insert(self, data):
        def insertion_complete(root):
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
        self.traverse(insertion_complete, order="levelorder")

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

# ACCUMULATION ----------------------------------------------------------------

    def fold(self, callback, root=None, start=0):
        def preorder(root, accumulator):
            if root is None:
                return accumulator
            return callback(root,
                    preorder(root.left, accumulator),
                    preorder(root.right, accumulator))
        
        return preorder(self.root if root is None else root, start)

    def height(self, root, left, right):
        return 1 + max(left, right)

    def sum(self, root, left, right):
        return root.data + left + right

    def count(self, root, left, right):
        return 1 + left + right

    def left_width(self, root, left, right):
        return left + 1

    def right_width(self, root, left, right):
        return right + 1

# ASCENSION -------------------------------------------------------------------

    def ascend(self, callback, root):
        while root.parent is not None:
            if callback(root):
                break
            root = root.parent

    def depth(self, root):
        count = itertools.count(0)
        self.ascend(lambda r: next(count), root)
        return next(count)

    def level(self, root):
        return self.depth(root) + 1

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
    #     sorted in any particular way.

    # Can be passed to traverse method for recursive propagation.
    def invert(self, root):
        root.left, root.right = root.right, root.left

    def insert(self, data, parent=None, right=False):
        if right:
            self.invert(parent)

        new = BTNode(data)
        try: new.left = parent.left
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

    def prune(self, root):
        if root.parent is None:
            self.root = None
            self.size = 0
            return

        if root is root.parent.left:
            root.parent.left = None
        else:
            root.parent.right = None

        pruned_branch_size = self.fold(self.count, root=root)
        self.size -= pruned_branch_size

