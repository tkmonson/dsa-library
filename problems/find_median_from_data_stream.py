'''
Find Median from Data Stream (#295)

Implement an object that can input integers from a data stream and can return
the median element of all integers seen so far. For an even number of integers,
the median is the mean of the two middle integers.
'''

import heapq
from random import randint

class MedianFinder:
    def __init__(self):
        self.left_heap = []
        self.right_heap = []

    # Time: O(logn)
    # Auxiliary space: O(1)
    def add_num(self, num: int) -> None:
        if not self.left_heap:
            heapq.heappush(self.left_heap, -num)
        elif num <= -self.left_heap[0]:
            if len(self.left_heap) > len(self.right_heap):
                num = heapq.heappushpop(self.left_heap, -num)
                heapq.heappush(self.right_heap, -num)
            else:
                heapq.heappush(self.left_heap, -num)
        else:
            if len(self.left_heap) == len(self.right_heap):
                num = heapq.heappushpop(self.right_heap, num)
                heapq.heappush(self.left_heap, -num)
            else:
                heapq.heappush(self.right_heap, num)

    # Time: O(1)
    # Auxiliary space: O(1)
    def find_median(self) -> float:
        if len(self.left_heap) > len(self.right_heap):
            return float(-self.left_heap[0])
        else:
            return (-self.left_heap[0] + self.right_heap[0]) / 2


if __name__ == '__main__':
    mf = MedianFinder()
    for _ in range(20):
        num = randint(1, 100)
        print(f'adding: {num}')
        mf.add_num(num)
        print(f'left: {mf.left_heap}')
        print(f'right: {mf.right_heap}')
        print(f'median: {mf.find_median()}\n')

'''
Because find_median can be called at any time, the structure should remain
sorted after adding an element. This can be done in O(logn) time with
structures like balanced BSTs and heaps. For a BST, find_median would be
O(logn) (using the "find kth smallest element in a BST" algorithm), but only if
it is balanced. A self-balancing BST like a red-black or AVL tree would be
helpful in this case. However, while a single heap would have an O(n)
find_median (popping all elements into a sorted list, getting the median, and
re-heapifying the list), one can achieve an O(1) find_median by using two
heaps: one for the left half of a sorted list, one for the right.
'''

