from abc import ABC, abstractmethod
from math import floor, log2

from . import binarytree as bt

class ImplicitBinaryHeap(ABC):
    # How should implicit structures implement size?
    def __init__(self, data=[]):
        self.state = data
        self._heapify(self.state)

    def __str__(self):
        return bt.BinaryTree(levelorder=self.state).__str__()

    def __eq__(self, other):
        return type(self) is type(other) and self.state == other.state

    def _heapify(self, data):
        for i in reversed(range(len(data))):
            self._sift_down(i)

    @abstractmethod
    def _compare(self, a, b):
        pass

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
        if (parent_i := floor((i - 1) // 2)) < 0:
            return  # i represents the heap's root

        if self._compare(self.state[i], self.state[parent_i]):
            self.state[i], self.state[parent_i] = \
                self.state[parent_i], self.state[i]
            self._sift_up(parent_i)

    def is_empty(self):
        return len(self.state) == 0

    def size(self):
        return len(self.state)

    def insert(self, data):
        self.state.append(data)
        self._sift_up(self.size() - 1)

    def _remove(self, i):
        if i < 0:
            i += self.size
        self.state[i], self.state[-1] = self.state[-1], self.state[i]
        self.state.pop()
        self._sift_down(i)

    def _find_root(self):
        return self.state[0]

    def _remove_root(self):
        self._remove(0)

    def _extract_root(self):
        self.state[0], self.state[-1] = self.state[-1], self.state[0]
        root_value = self.state.pop()
        self._sift_down(0)
        return root_value

    def _replace_root(self, data):
        self.state[0], data = data, self.state[0]
        self._sift_down(0)
        return data


class ImplicitBinaryMinHeap(ImplicitBinaryHeap):
    def _compare(self, a, b):
        return a < b

    def find_min(self):
        return self._find_root()

    def remove_min(self):
        self._remove_root()

    def extract_min(self):
        return self._extract_root()

    def replace_min(self, data):
        return self._replace_root(data)


class ImplicitBinaryMaxHeap(ImplicitBinaryHeap):
    def _compare(self, a, b):
        return a > b

    def find_max(self):
        return self._find_root()

    def remove_max(self):
        self._remove_root()

    def extract_max(self):
        return self._extract_root()

    def replace_max(self, data):
        return self._replace_root(data)

