# Mergesort is a divide-and-conquer algorithm for sorting linear data structures. Most implementations produce a stable sort (the order of equal elements is not changed).

# Time Complexity: O(nlogn)
# Auxiliary Space Complexity: O(n) for arrays, O(1) for linked lists

# Mergesort has two steps:
    # 1. Divide the unsorted list into n sublists, each one containing one element (a list of one element is considered sorted).
    # 2. Merge the sorted sublists repeatedly to produce larger sorted sublists until a single sorted list of n elements remains.

# The strategy is to divide the list into halves and recur on the halves to further divide them (depth-first, dividing left before right). Then, you merge the halves as you backtrack (depth-first, merging left before right). (An iterative, bottom-up implementation is also possible, where the list is split into n sublists of length 1 that are then iteratively merged.)

import random, time

def mergesort(arr):
    # Base case: an array of length 0 or 1 is sorted
    if len(arr) <= 1:
        return
    
    # Divide array into halves
    mid = len(arr) // 2
    L = arr[:mid]
    R = arr[mid:]

    # Divide and merge left and right halves separately, sorting each
    mergesort(L)
    mergesort(R)

    # Compare elements in halves, sort into input array space
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]: # <= ensures a stable sort (unlike <)
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Sort any remaining elements into input array space
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

if __name__ == '__main__':
    for n in [100, 1000, 10000, 100000, 1000000]:
        arr = [random.randint(1,100) for _ in range(n)]
        t = time.process_time()
        mergesort(arr)
        print(f"n = {n}: {time.process_time() - t} seconds")

# ---- NOTES ---- 

# Mergesort is more efficient than quicksort for data structures with sequential access (e.g. linked lists, data stored on sequential media like disk or tape).

# When implemented on arrays, mergesort has O(n) auxiliary space complexity (the space allocated for the left and right halves). It can easily be lowered to O(n/2) by allocating space only for the left half, doing comparisons between elements of that array and elements on the right half of the input array, and writing into the input array.

# There are various, super-complicated, asterisk-ridden in-place merge algorithms that allow for an "in-place" mergesort (O(logn) stack space is still required for the recursive divide step). One example is blocksort, which is a modified mergesort that is stable and in-place.

# Mergesort parallelizes well. It is trivial to parallelize the recursion of a sequential mergesort, but it won't speed up much. Better parallelism can be achieved by parallelizing the merge algorithm instead. For machines with >2 processors, the algorithm can be further parallelized by converting the binary merge method into a K-way merge method (not halves... thirds, fourths, etc.).

# Mergesort, quicksort, and heapsort all have O(nlogn) time complexity, but mergesort is the slowest of the three when working with arrays. It also has the worst auxiliary space complexity of the three when working with arrays: O(n) versus quicksort's O(logn) and heapsort's O(1). Mergesort is valued for being a stable sort (unlike heapsort and quicksort), and for its efficient sorting of linked lists (heapsort fails, quicksort slows significantly, mergesort achieves O(1) auxiliary space complexity).
