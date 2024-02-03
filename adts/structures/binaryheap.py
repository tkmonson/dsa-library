from abc import ABC, abstractmethod
from math import floor, log2

from . import binarytree as bt

# BT: Insert/remove input datatype asymmetry
# BT: Modified level-order traverse to accommodate node-swapping method
# Should 'remove' be considered a heap method?
# How does ABC inheritance work?
# Should the root-based operations be prefixed with _ or __?
    # The notable case of the same logic being inherited by methods in two
    #     subclasses, methods which have different names (e.g. __remove_root =>
    #     remove_min, remove_max).

# In the most general sense, a 'key' is a piece of information that is required
#     to access some data. In the context of a hash map, for example, a key is
#     segregated from its value; it is the input to a hash function, the output
#     of which is an index that indicates where the value is stored. In the
#     context of node-based data structures, a key is used to identify a
#     component of a structure. It is integrated with but distinct from the
#     'satellite data,' which is the actual payload that is of interest in any
#     given application of a data structure. Often, keys determine how
#     satellite data is stored and manipulated within the structure. For
#     example, in a min-heap, the key of each node is smaller than the keys of
#     that node's children.
# The ImplicitBinaryHeap has a _prioritize_key operation so that the structure
#     can be used effectively in Dijkstra's algorithm. To achieve an O(logn)
#     time complexity for this operation, the structure must maintain a map
#     of node keys to indicies, as this provides the ability to search in
#     constant time. Because of this map requirement, keys in the
#     ImplicitBinaryHeap must be unique.

class ImplicitBinaryHeap(ABC):
    # How should implicit structures implement size? __len__?
    def __init__(self, levelorder=[]):
        self.state = levelorder
        self.index_map = {}
        for i in range(self.size()):
            self.index_map[self.state[i]] = i
        self._heapify(self.state)

    def __str__(self):
        return bt.BinaryTree(levelorder=self.state).__str__()

    def __eq__(self, other):
        return type(self) is type(other) and self.state == other.state

    def is_empty(self):
        return len(self.state) == 0

    def size(self):
        return len(self.state)

    def insert(self, data):
        self.state.append(data)
        self.index_map[data] = self.size() - 1
        self._sift_up(self.size() - 1)

    def remove(self, i):
        if i < 0:
            i += self.size
        self._swap(i, -1)
        self.index_map.pop(self.state.pop())
        parent_i = floor((i - 1) // 2)
        try:
            if self._compare(self.state[i], self.state[parent_i]):
                self._sift_up(i)
            else:
                self._sift_down(i)
        except IndexError:
            return

    # MIN/MAX -----------------------------------------------------------------

    def _get_root(self):
        return self.state[0]

    def _remove_root(self):
        self.remove(0)

    def _extract_root(self):
        ret = self._get_root()
        self.remove(0)
        return ret

    def _replace_root(self, data):
        self.state[0], data = data, self.state[0]
        self.index_map[self.state[0]] = 0
        self.index_map.pop(data)
        self._sift_down(0)
        return data

    # INTERNAL ----------------------------------------------------------------

    @abstractmethod
    def _compare(self, a, b):
        pass

    def _swap(self, i, j):
        self.state[i], self.state[j] = self.state[j], self.state[i]
        self.index_map[self.state[i]] = i
        self.index_map[self.state[j]] = j

    def _heapify(self, state):
        for i in reversed(range(len(state))):
            self._sift_down(i)

    def _sift_down(self, i):
        left_i = 2 * i + 1
        right_i = 2 * i + 2

        try:
            left_value = self.state[left_i]
        except IndexError:
            return  # i represents a leaf

        try:
            right_value = self.state[right_i]
        except IndexError:
            right_value = left_value  # i only has left child

        child_i = right_i if self._compare(right_value, left_value) else left_i
        if self._compare(self.state[child_i], self.state[i]):
            self._swap(i, child_i)
            self._sift_down(child_i)

    def _sift_up(self, i):
        if (parent_i := (i - 1) // 2) < 0:
            return  # i represents the heap's root

        if self._compare(self.state[i], self.state[parent_i]):
            self._swap(i, parent_i)
            self._sift_up(parent_i)

    # Time: O(logn)
    # Auxiliary Space: O(1)
    def _prioritize_key(self, key, value):
        i = self.index_map[key]
        self.state[i] = value
        self.index_map.pop(key)
        self.index_map[value] = i
        self._sift_up(i)


class ImplicitBinaryMinHeap(ImplicitBinaryHeap):
    def get_min(self):
        return self._get_root()

    def remove_min(self):
        self._remove_root()

    def extract_min(self):
        return self._extract_root()

    def replace_min(self, data):
        return self._replace_root(data)

    def _compare(self, a, b):
        return a < b

    def decrease_key(self, key, value):
        if key < value:
            raise ValueError("New value must be smaller than old value.");
        self._prioritize_key(key, value)


class ImplicitBinaryMaxHeap(ImplicitBinaryHeap):
    def get_max(self):
        return self._get_root()

    def remove_max(self):
        self._remove_root()

    def extract_max(self):
        return self._extract_root()

    def replace_max(self, data):
        return self._replace_root(data)

    def _compare(self, a, b):
        return a > b

    def increase_key(self, key, value):
        if key > value:
            raise ValueError("New value must be smaller than old value.");
        self._prioritize_key(key, value)


class ExplicitBinaryHeap(bt.BaseBinaryTree):
    # Min/max as a property? Would eliminate need for _compare.
    def __init__(self, preorder=[], inorder=[], postorder=[], levelorder=[]):
        selector = tuple(map(bool, (preorder, inorder, postorder, levelorder)))
        if sum(selector) > 1:
            raise ValueError(
                "A heap must be complete; constructor takes 0 or 1 arguments.")

        super().__init__(preorder, inorder, postorder, levelorder)
        self._heapify()

    @classmethod
    def succinct_construct(cls, structure, data, order="preorder"):
        print("Ignoring structure, a heap must be complete...")
        if order == "preorder":
            return super().__init__(preorder=data)
        elif order == "levelorder":
            return super().__init__(levelorder=data)
        else:
            raise ValueError("Invalid order given.")
        self._heapify()

    def insert(self, data):
        insert_i = self.size
        parent_i = (insert_i - 1) // 2
        insertee = bt.BTNode(data)
        parent = self._find_ith_node(parent_i)

        if insert_i % 2 == 0:
            parent.right = insertee
        else:
            parent.left = insertee
        insertee.parent = parent
        self.size += 1

        self._sift_up(insertee)

    def remove(self, removee):
        siftee = self._find_ith_node(self.size - 1)
        self._swap_nodes(removee, siftee)

        super().remove(removee)  # last node in level-order

        if (siftee.parent is not None
                and self._compare(siftee.data, siftee.parent.data)):
            self._sift_up(siftee)
        else:
            self._sift_down(siftee)

    # MIN/MAX -----------------------------------------------------------------

    def _get_root(self):
        return self.root.data

    def _remove_root(self):
        self.remove(self.root)

    def _extract_root(self):
        ret = self.root
        self._remove_root()
        return ret

    def _replace_root(self, data):
        replacement = bt.BTNode(data)
        replacement.left, replacement.right = self.root.left, self.root.right
        replacement.left.parent = replacement
        replacement.right.parent = replacement
        ret = self.root
        
        self.root = replacement
        self._sift_down(self.root)
        return ret

    # INTERNAL ----------------------------------------------------------------

    @abstractmethod
    def _compare(self, a, b):
        pass

    # Exceptions?
    def _find_ith_node(self, i):
        level = floor(log2(i + 1))
        level_capacity = 2 ** level
        index_in_level = i - (level_capacity - 1)

        ith_node = self.root
        lo = 0
        hi = level_capacity
        for _ in range(level):
            mid = lo + (hi - lo) // 2
            if index_in_level < mid:
                ith_node = ith_node.left
                hi = mid
            else:
                ith_node = ith_node.right
                lo = mid

        return ith_node

    def _heapify(self):
        self.traverse(self._sift_up, order="levelorder")  # slow algorithm

    def _sift_down(self, root):
        try:
            left_value = root.left.data
        except AttributeError:
            return  # root is a leaf

        try:
            right_value = root.right.data
        except AttributeError:
            right_value = left_value  # root only has left child

        if self._compare(right_value, left_value):
            swap_node = root.right
        else:
            swap_node = root.left

        if self._compare(swap_node.data, root.data):
            self._swap_nodes(root, swap_node)
            self._sift_down(root)

    def _sift_up(self, root):
        if (swap_node := root.parent) is None:
            return

        if self._compare(root.data, swap_node.data):
            self._swap_nodes(root, swap_node)
            self._sift_up(root)

  
class ExplicitBinaryMinHeap(ExplicitBinaryHeap):
    def get_min(self):
        return self._get_root()

    def remove_min(self):
        self._remove_root()

    def extract_min(self):
        return self._extract_root()

    def replace_min(self, data):
        return self._replace_root(data)

    def _compare(self, a, b):
        return a < b


class ExplicitBinaryMaxHeap(ExplicitBinaryHeap):
    def get_max(self):
        return self._get_root()

    def remove_max(self):
        self._remove_root()

    def extract_max(self):
        return self._extract_root()

    def replace_max(self, data):
        return self._replace_root(data)

    def _compare(self, a, b):
        return a > b

