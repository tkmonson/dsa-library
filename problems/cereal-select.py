# Problem from Coinbase HackerRank

# Input: array of cereal prices (int) and a subarray size (int)
# Output: the maximum price of the minimums of the subarrays

# Example:
# arr = [8,2,4,7,5], x = 2
# Subarrays: [8,2], [2,4], [4,7], [7,5]
# Minimums of subarrays: 2, 2, 4, 5
# Maximum: 5

from heapq import heappop, heappush, heapify
import numpy as np

def cereal_select(arr, x):
    n = len(arr)
    last_subarray_index = n - x + 1
    maxheap = []

    for i in range(last_subarray_index):
        minheap = arr[i:i+x]
        heapify(minheap)
        heappush(maxheap, -1 * heappop(minheap))

    return -1 * heappop(maxheap)

randnums = list(np.random.randint(1,101,10000000))
print(randnums)
print(cereal_select(randnums, 5))
