from contextlib import suppress
import unittest

from structures import binaryheap as bh

class TestImplicitBinaryMinHeap(unittest.TestCase):
    def setUp(self):
        # State is heapified to [0,1,0,2,3,1,3,9,6,5,8,2,4,7]
        self.heap = bh.ImplicitBinaryMinHeap(
            levelorder=[9,8,7,6,5,4,3,2,1,0,3,2,1,0])

    def test_0__heapify(self):
        for i in range(len(self.heap.state)):
            with suppress(IndexError):
                if (self.heap.state[i] > self.heap.state[2 * i + 1]
                    or self.heap.state[i] > self.heap.state[2 * i + 2]):
                    self.assertTrue(False)
        self.assertTrue(True)

    def test_1_is_empty(self):
        self.assertFalse(self.heap.is_empty())

    def test_2_size(self):
        self.assertEqual(self.heap.size(), 14)

    def test_3_insert(self):
        resultant_heap = bh.ImplicitBinaryMinHeap(
            levelorder=[0,1,0,2,3,1,2,9,6,5,8,2,4,7,3])
        self.heap.insert(2)
        self.assertEqual(self.heap, resultant_heap)

    def test_4_remove(self):
        resultant_heap = bh.ImplicitBinaryMinHeap(
            levelorder=[0,1,0,2,5,1,3,9,6,7,8,2,4])
        self.heap.remove(4)
        self.assertEqual(self.heap, resultant_heap)

    def test_5_find_min(self):
        self.assertEqual(self.heap.find_min(), 0)

    def test_6_remove_min(self):
        resultant_heap = bh.ImplicitBinaryMinHeap(
            levelorder=[0,1,1,2,3,2,3,9,6,5,8,7,4])
        self.heap.remove_min()
        self.assertEqual(self.heap, resultant_heap)

    def test_7_extract_min(self):
        resultant_heap = bh.ImplicitBinaryMinHeap(
            levelorder=[0,1,1,2,3,2,3,9,6,5,8,7,4])
        self.assertEqual(self.heap.extract_min(), 0)
        self.assertEqual(self.heap, resultant_heap)

    def test_8_replace_min(self):
        resultant_heap = bh.ImplicitBinaryMinHeap(
            levelorder=[0,1,1,2,3,2,3,9,6,5,8,8,4,7])
        self.assertEqual(self.heap.replace_min(8), 0)
        self.assertEqual(self.heap, resultant_heap)


class TestImplicitBinaryMaxHeap(unittest.TestCase):
    def setUp(self):
        # State is heapified to [9,8,7,6,5,4,3,2,1,0,3,2,1,0]
        self.heap = bh.ImplicitBinaryMaxHeap(
            levelorder=[0,1,0,2,3,1,3,9,6,5,8,2,4,7])

    def test_0__heapify(self):
        for i in range(len(self.heap.state)):
            with suppress(IndexError):
                if (self.heap.state[i] < self.heap.state[2 * i + 1]
                    or self.heap.state[i] < self.heap.state[2 * i + 2]):
                    self.assertTrue(False)
        self.assertTrue(True)

    def test_1_is_empty(self):
        self.assertFalse(self.heap.is_empty())

    def test_2_size(self):
        self.assertEqual(self.heap.size(), 14)

    def test_3_insert(self):
        resultant_heap = bh.ImplicitBinaryMaxHeap(
            levelorder=[9,8,8,6,5,4,7,2,1,0,3,2,1,0,3])
        self.heap.insert(8)
        self.assertEqual(self.heap, resultant_heap)

    def test_4_remove(self):
        resultant_heap = bh.ImplicitBinaryMaxHeap(
            levelorder=[9,8,7,6,3,4,3,2,1,0,0,2,1])
        self.heap.remove(4)
        self.assertEqual(self.heap, resultant_heap)

    def test_5_find_max(self):
        self.assertEqual(self.heap.find_max(), 9)

    def test_6_remove_max(self):
        resultant_heap = bh.ImplicitBinaryMaxHeap(
            levelorder=[8,6,7,2,5,4,3,0,1,0,3,2,1])
        self.heap.remove_max()
        self.assertEqual(self.heap, resultant_heap)

    def test_7_extract_max(self):
        resultant_heap = bh.ImplicitBinaryMaxHeap(
            levelorder=[8,6,7,2,5,4,3,0,1,0,3,2,1])
        self.assertEqual(self.heap.extract_max(), 9)
        self.assertEqual(self.heap, resultant_heap)

    def test_8_replace_max(self):
        resultant_heap = bh.ImplicitBinaryMaxHeap(
            levelorder=[8,6,7,3,5,4,3,2,1,0,3,2,1,0])
        self.assertEqual(self.heap.replace_max(3), 9)
        self.assertEqual(self.heap, resultant_heap)


class TestExplicitBinaryMinHeap(unittest.TestCase):
    def setUp(self):
        self.heap = bh.ExplicitBinaryMinHeap(
            levelorder=[9,8,7,6,5,4,3,2,1,0,3,2,1,0])  # pre-heapify state

    def test_0__heapify(self):
        resultant_heap = bh.ExplicitBinaryMinHeap(
            levelorder=[0,1,0,3,2,2,1,9,6,7,3,8,4,5])  # post-heapify state
        self.assertEqual(self.heap, resultant_heap)

    def test_1_insert(self):
        self.heap.insert(2)
        resultant_heap = bh.ExplicitBinaryMinHeap(
            levelorder=[0,1,0,3,2,2,1,9,6,7,3,8,4,5,2])
        self.assertEqual(self.heap, resultant_heap)

    def test_2_remove(self):
        self.heap.remove(self.heap.root.right.left)
        resultant_heap = bh.ExplicitBinaryMinHeap(
            levelorder=[0,1,0,3,2,4,1,9,6,7,3,8,5])
        self.assertEqual(self.heap, resultant_heap)

    def test_3_find_min(self):
        self.assertEqual(self.heap.find_min(), 0)

    def test_4_remove_min(self):
        self.heap.remove_min()
        resultant_heap = bh.ExplicitBinaryMinHeap(
            levelorder=[0,1,1,3,2,2,5,9,6,7,3,8,4])
        self.assertEqual(self.heap, resultant_heap)

    def test_5_extract_min(self):
        self.assertEqual(self.heap.extract_min().data, 0)
        resultant_heap = bh.ExplicitBinaryMinHeap(
            levelorder=[0,1,1,3,2,2,5,9,6,7,3,8,4])
        self.assertEqual(self.heap, resultant_heap)

    def test_6_replace_min(self):
        self.assertEqual(self.heap.replace_min(8).data, 0)
        resultant_heap = bh.ExplicitBinaryMinHeap(
            levelorder=[0,1,1,3,2,2,5,9,6,7,3,8,4,8])
        self.assertEqual(self.heap, resultant_heap)


class TestExplicitBinaryMaxHeap(unittest.TestCase):
    def setUp(self):
        self.heap = bh.ExplicitBinaryMaxHeap(
            levelorder=[0,1,0,2,3,1,3,9,6,5,8,2,4,7])  # pre-heapify state

    def test_0__heapify(self):
        resultant_heap = bh.ExplicitBinaryMaxHeap(
            levelorder=[9,8,7,3,6,3,4,0,2,1,5,0,2,1])  # post-heapify state
        self.assertEqual(self.heap, resultant_heap)

    def test_1_insert(self):
        self.heap.insert(8)
        resultant_heap = bh.ExplicitBinaryMaxHeap(
            levelorder=[9,8,8,3,6,3,7,0,2,1,5,0,2,1,4])
        self.assertEqual(self.heap, resultant_heap)

    def test_2_remove(self):
        self.heap.remove(self.heap.root.left.right)
        resultant_heap = bh.ExplicitBinaryMaxHeap(
            levelorder=[9,8,7,3,5,3,4,0,2,1,1,0,2])
        self.assertEqual(self.heap, resultant_heap)

    def test_3_find_max(self):
        self.assertEqual(self.heap.find_max(), 9)

    def test_4_remove_max(self):
        self.heap.remove_max()
        resultant_heap = bh.ExplicitBinaryMaxHeap(
            levelorder=[8,6,7,3,5,3,4,0,2,1,1,0,2])
        self.assertEqual(self.heap, resultant_heap)

    def test_5_extract_max(self):
        self.assertEqual(self.heap.extract_max().data, 9)
        resultant_heap = bh.ExplicitBinaryMaxHeap(
            levelorder=[8,6,7,3,5,3,4,0,2,1,1,0,2])
        self.assertEqual(self.heap, resultant_heap)

    def test_6_replace_max(self):
        self.assertEqual(self.heap.replace_max(3).data, 9)
        resultant_heap = bh.ExplicitBinaryMaxHeap(
            levelorder=[8,6,7,3,5,3,4,0,2,1,3,0,2,1])
        self.assertEqual(self.heap, resultant_heap)


if __name__ == "__main__":
    unittest.main()

