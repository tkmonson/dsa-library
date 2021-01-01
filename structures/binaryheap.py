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

class ImplicitBinaryHeap(ABC):
    # How should implicit structures implement size? __len__?
    def __init__(self, levelorder=[]):
        self.state = levelorder
        self._heapify(self.state)

    def __str__(self):
        return bt.BaseBinaryTree(levelorder=self.state).__str__()

    def __eq__(self, other):
        return type(self) is type(other) and self.state == other.state

    def is_empty(self):
        return len(self.state) == 0

    def size(self):
        return len(self.state)

    def insert(self, data):
        self.state.append(data)
        self._sift_up(self.size() - 1)

    def remove(self, i):
        if i < 0:
            i += self.size
        self.state[i], self.state[-1] = self.state[-1], self.state[i]
        self.state.pop()
        parent_i = floor((i - 1) // 2)
        if self._compare(self.state[i], self.state[parent_i]):
            self._sift_up(i)
        else:
            self._sift_down(i)

    # MIN/MAX -----------------------------------------------------------------

    def _find_root(self):
        return self.state[0]

    def _remove_root(self):
        self.remove(0)

    def _extract_root(self):
        ret = self._find_root()
        self.remove(0)
        return ret

    def _replace_root(self, data):
        self.state[0], data = data, self.state[0]
        self._sift_down(0)
        return data

    # INTERNAL ----------------------------------------------------------------

    @abstractmethod
    def _compare(self, a, b):
        pass

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

        swap_i = right_i if self._compare(right_value, left_value) else left_i
        if self._compare(self.state[swap_i], self.state[i]):
            self.state[i], self.state[swap_i] = \
                self.state[swap_i], self.state[i]
            self._sift_down(swap_i)

    def _sift_up(self, i):
        if (parent_i := (i - 1) // 2) < 0:
            return  # i represents the heap's root

        if self._compare(self.state[i], self.state[parent_i]):
            self.state[i], self.state[parent_i] = \
                self.state[parent_i], self.state[i]
            self._sift_up(parent_i)


class ImplicitBinaryMinHeap(ImplicitBinaryHeap):
    def find_min(self):
        return self._find_root()

    def remove_min(self):
        self._remove_root()

    def extract_min(self):
        return self._extract_root()

    def replace_min(self, data):
        return self._replace_root(data)

    def _compare(self, a, b):
        return a < b


class ImplicitBinaryMaxHeap(ImplicitBinaryHeap):
    def find_max(self):
        return self._find_root()

    def remove_max(self):
        self._remove_root()

    def extract_max(self):
        return self._extract_root()

    def replace_max(self, data):
        return self._replace_root(data)

    def _compare(self, a, b):
        return a > b


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

    def _find_root(self):
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
    def find_min(self):
        return self._find_root()

    def remove_min(self):
        self._remove_root()

    def extract_min(self):
        return self._extract_root()

    def replace_min(self, data):
        return self._replace_root(data)

    def _compare(self, a, b):
        return a < b


class ExplicitBinaryMaxHeap(ExplicitBinaryHeap):
    def find_max(self):
        return self._find_root()

    def remove_max(self):
        self._remove_root()

    def extract_max(self):
        return self._extract_root()

    def replace_max(self, data):
        return self._replace_root(data)

    def _compare(self, a, b):
        return a > b

