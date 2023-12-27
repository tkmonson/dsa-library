'''
Kth Largest Element in a Stream (#703)

Design a class to find the kth largest element in a stream (kth largest in
sorted order, not kth distinct element).

Implement KthLargest class:
    * `KthLargest(int k, int[] nums)`: Initializes the object with the integer
      `k` and the stream of integers `nums`.
    * `int add(int val)`: Appends the integer `val` to the stream and returns
      the element representing the kth largest element in the stream.

It is guaranteed that there will be at least `k` elements in the array when you
search for the kth element.
'''

import heapq

class KthLargest:
    # Time: O(nlogn)
    # Auxiliary space: O(k)
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        nums.sort(reverse=True)
        self.heap = nums[:k]
        heapq.heapify(self.heap)

    # Time: O(logk)
    # Auxiliary space: O(1)
    def add(self, val: int):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]

'''
You don't need to maintain a heap with more than k elements. Initialize a
min-heap with the k largest elements in nums (or k - 1 elements, if len(nums)
== k - 1).

The heap can be initialized with only k - 1 elements. In this case, the first
add call should add its element to the heap. For a heap with k elements, you
only need to add a new element to the heap if it's greater than the min
element in the heap (in which case, also pop the heap to maintain a fixed size
of k).
'''

if __name__ == '__main__':
    k = 3
    nums = [4, 5, 8, 2]
    kl = KthLargest(k, nums)
    print(kl.add(3))
    print(kl.add(5))
    print(kl.add(10))
    print(kl.add(9))
    print(kl.add(4))

