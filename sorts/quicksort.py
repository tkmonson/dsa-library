'''
Quicksort is a divide-and-conquer algorithm for sorting arrays. Efficient
implementations do not produce a stable sort (the order of equal elements may
change).

Time complexity: O(nlogn) average, O(n^2) worst
Auxiliary space complexity: O(logn)

Quicksort has three steps:
    1. Select a pivot.
    2. Partition the array according to a partitioning scheme. As a result of
       this step, the array will have a partial order between two subarrays.
    3. Recur on both subarrays.

The general idea is that you achieve a partial order over your input after
each partition. By applying this recursively, you achieve a total ordering in
the end. There are two common partitioning schemes that achieve partial order:
    Lomuto: for all x in L, p in M, y in R: x <= p < y, where M is a singleton
    Hoare: for all x in L, y in R, x < y
Note that Hoare partitions the array into two subarrays whereas Lomuto
partitions it into three, the middle of which is a singleton array containing
only the pivot element.

Hoare is the partitioning scheme of the original 1956 quicksort algorithm, and
it is more efficient than Lomuto. Lomuto was written for a 1990 algorithms
textbook, and it is considered by many to be the more intuitive algorithm.

Lomuto places the pivot in its final position and returns its index.
Everything to the left of the pivot is <= pivot and everything to right of the
pivot is > pivot. This is a partial order. When the algorithm is applied
recursively on those left and right subarrays, the elements of the whole
gradually become totally ordered. In some sense, Lomuto is like generating a
BST top down, filling in the details one at a time as each unsorted subarray
achieves partial order:

    {*}             50                       50
                   /  \                    /    \
               {<=}    {>}              20        70
         =>                   =>        /\        /\
                                    {<=}  {>} {<=}  {>}
'''


import random, time

def lomuto_partition(arr, lo, hi):
    # Select the last index as pivot
    pivot = arr[hi]
    
    # Leader loops through the list
    # If leader finds an element <= pivot, it swaps elements with follower
    # When a swap occurs, follower increments
    # Thus, all elements that we want left of pivot are now left of follower
    # And all elements that we want right of pivot are now right of follower
    follower = lo
    for leader in range(lo, hi):
        if arr[leader] <= pivot:
            arr[follower], arr[leader] = arr[leader], arr[follower]
            follower += 1

    # Swap follower and pivot elements, return index of pivot element
    arr[follower], arr[hi] = arr[hi], arr[follower]
    return follower


'''
Hoare does not necessarily place the pivot in its final position. All it
guarantees is that there is a partial order between two subarrays. It returns
the index of the left subarray's rightmost element. With this boundary
information, you know which subarrays to recur on. At the bottom of the
recursion, the subarrays degenerate into singletons; all ambiguity is removed
when they are compared, and total order is achieved. In some sense, Hoare is
like a binary tree where every child is a member of a binary partition of its
parent (for all (c,p) in T: c in P, where P = partition(p) = {L, R}):

    {*}            {*}                        {*}
                  /   \                     /     \
               {<}     {>}              {<}         {>}
         =>                   =>       /   \       /   \
                                    {2}     {3} {<}     {>}
'''


def hoare_partition(arr, lo, hi):
    # Select the middle element as pivot
    pivot = arr[lo + (hi-lo) // 2]

    lp, rp = lo, hi
    while True:
        
        # Pointers move inward and stop at elements on the wrong side
        # When both have stopped, a swap opportunity has been found
        # If a wrong element is not found, the pointer will stop at pivot
        while arr[lp] < pivot:
            lp += 1
        while arr[rp] > pivot:
            rp -= 1

        if lp >= rp:
            return rp
        
        # Swap the elements to put them on their correct sides
        # If one pointer is at a wrong element and the other is at pivot,
            # The pivot element will swap
        # Move the pointers inward by one
        arr[lp], arr[rp] = arr[rp], arr[lp]
        lp += 1
        rp -= 1


'''
Quicksort, as implemented in _quicksort, is a tail-recursive subroutine. That
means that the final instruction of its control flow is a recursive subroutine
call, a tail call to itself. Normally, when a subroutine call is made, a new
stack frame is added to the call stack. In the case of a tail call, there is no
need to return to the calling subroutine. Thus, the calling subroutine's stack
frame can be overwritten by the called subroutine's stack frame, and control can
be transferred directly to the called subroutine with a jump instruction. This
is called tail call elimination or tail call optimization, and it can
significantly lower space complexity in the call stack for tail-recursive
subroutines. It is often written into the compilers of programming languages
(functional ones especially) and performed automatically (not in Python though).

Consider the worst-case space complexity of _quicksort. After partitioning, the
sizes of the left and right subarrays differ by the maximum amount, and this
happens for every recursive call. The size of the larger subarray (initially n -
1) decreases by 1 with each partition, and the recursive call tree becomes very
unbalanced, reaching an O(n) depth and thus an O(n) space complexity. To
maintain the O(logn) average-case space complexity in the worst case, we must
ensure that we do not recur on a subarray that will produce an unbalanced
recursive call tree (i.e. anything of size > n/2). To do this, we change the
recursion strategy.

_quicksort recurs on both subarrays (left before right). _tco_quicksort recurs
on only the smaller subarray, then it partitions the larger subarray, and then
it recurs on the smaller of the subsubarrays, and then it partitions the larger
subsubarray... until every top-level interval is covered by a recursive call. By
always recurring on the smaller subarray, we guarantee that the maximum depth of
any recursive call tree will be bounded above by O(logn). To implement this
strategy, we ensure that the tail call is over the larger subarray by recurring
over the smaller one first. We then eliminate that tail cail, updating
parameters (overwriting the stack frame) and jumping to the top of the
subroutine instead (via a while construct).
'''


def _quicksort(arr, lo, hi, partition):
    if lo < hi:
        p1 = partition(arr, lo, hi)
        p2  = p1 + 1
        if partition == lomuto_partition:
            p1 -= 1
            
        _quicksort(arr, lo, p1, partition)
        _quicksort(arr, p2, hi, partition)


def _tco_quicksort(arr, lo, hi, partition):
    while lo < hi:
        p1 = partition(arr, lo, hi)
        p2  = p1 + 1
        if partition == lomuto_partition:
            p1 -= 1

        if p1 - lo < hi - p2:
            _tco_quicksort(arr, lo, p1, partition)
            lo = p2
        else:
            _tco_quicksort(arr, p2, hi, partition)
            hi = p1


def quicksort(arr, partition=hoare_partition, tail_call_opt=True):
    if tail_call_opt:
        _tco_quicksort(arr, 0, len(arr) - 1, partition)
    else:
        _quicksort(arr, 0, len(arr) - 1, partition)


if __name__ == "__main__":
    arr = [random.randrange(10) for _ in range(10)]
    print(arr)
    quicksort(arr)
    print(f"{arr}\n")
   
    print("Lomuto")
    for n in [100, 1000, 10000, 100000, 1000000]:
        arr = [random.randrange(n) for _ in range(n)]
        t = time.process_time()
        quicksort(arr, partition=lomuto_partition)
        print(f"n = {n}: {time.process_time() - t} seconds")

    print("\nHoare")
    for n in [100, 1000, 10000, 100000, 1000000]:
        arr = [random.randrange(n) for _ in range(n)]
        t = time.process_time()
        quicksort(arr, partition=hoare_partition)
        print(f"n = {n}: {time.process_time() - t} seconds")

'''
---- FURTHER NOTES ----

Ideally, you want to select a pivot that will generate two subarrays that are as
similar in size as possible (equal or difference of 1). This will minimize the
number of recursive steps. Stated another way, this will maximize the number of
relations in the partial order. This optimal pivot is the median of the unsorted
array, whose location and value is unknowable, barring an unjustifiably
expensive O(n) search for every recursive call. Thus, we must select a pivot
according to a heuristic.

Because the array is unsorted, choosing a pivot by index is a random selection,
no better than choosing an index at random. In theory, any index is as good as
any other; in practice, you don't want to choose the first or last element
because that will cause worst-case behavior on an already sorted array, which is
a common use-case. Pivot selection is hard-coded in the partitioning schemes:
last element for Lomuto (for simplicity), middle element for Hoare (for
efficiency).

While the choice of pivot index is fixed in the partitioning schemes, the choice
of pivot value is not. For example, the last element of an array may be swapped
for a different element before a Lomuto partitioning begins. This pre-partition
swapping allows us to choose a pivot that is, on average, closer to the median.
For example, median-of-three pivot selection finds the median of the first,
middle, and last elements of the list and swaps it into the pivot index. This
heuristic produces runtimes that are statistically faster than those produced by
random pivot selection (and it fixes Lomuto's worst-case behavior on already
sorted arrays).

Quickselect is an O(n) selection algorithm (returns kth smallest element in
unsorted list) that uses the same general approach as quicksort. The key
difference is that quickselect only recurs on the subarray that contains the
desired element. It is easy to implement with Lomuto partitioning because the
pivot will be in its final position, so you will have your answer when the pivot
stops at k. Quickselect, like quicksort, is tail-recursive and eligible for tail
call optimization.

Quicksort parallelizes well. The array can be partitioned with a parallel prefix
sum algorithm that performs O(n) work in O(logn) time and O(n) space. The two
subarrays can then be sorted recursively in parallel. Parallel quicksort does
O(nlogn) work in O((logn)^2) time and O(n) space. A time complexity of O(logn)
is possible on a concurrent-read, concurrent-write (CRCW) parallel
random-access-machine (PRAM) with n processors.

A binary tree sort is a sorting algorithm that builds a binary search tree (O(n)
auxiliary space) from the elements to be sorted and then traverses the tree
in-order to produce a sorted sequence. Quicksort is like a space-optimized
version of binary tree sort. The recursive call stack acts like a tree, but no
data structure is constructed, so the algorithm is "in-place" (plus O(logn)
space in the call stack). (If allowed O(n) auxiliary space, quicksort can
produce a stable sort, similar to how tree sort does it.)

Quicksort, mergesort, and heapsort all have O(nlogn) time complexity, but
quicksort tends to be the fastest of the three when working with arrays. Unlike
mergesort, it is not stable, and it does not handle linked lists well (cannot
freely select a pivot). Unlike heapsort, which is constant w.r.t. space, it has
an O(logn) auxiliary space complexity.
'''
