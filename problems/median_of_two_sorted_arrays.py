'''
Median of Two Sorted Arrays (#4)

Given two sorted arrays of sizes `m` and `n`, return the median of the two
sorted arrays. The solution should have O(log(m + n)) time complexity.
'''

from math import inf

# Time: O(log(m + n))
# Auxiliary space: O(1)
def find_median(a: list[int], b: list[int]) -> int:
    total = len(a) + len(b)
    half = total // 2
    if len(a) > len(b):
        a, b = b, a
    
    L, R = 0, len(a) - 1
    while True:
        i = (L + R) // 2
        j = half - i - 2
        
        a_left = a[i] if i >= 0 else -inf
        a_right = a[i + 1] if (i + 1) < len(a) else inf
        b_left = b[j] if j >= 0 else -inf
        b_right = b[j + 1] if (j + 1) < len(b) else inf
        
        if a_left <= b_right and b_left <= a_right:
            if total % 2:
                return min(a_right, b_right)
            else:
                return (max(a_left, b_left) + min(a_right, b_right)) // 2
        elif a_left > b_right:
            R = i - 1
        else:
            L = i + 1

'''
Let the two sorted arrays be called A and B. Let's partition them such that
each has two parts. If:

    C1. the left partitions, when combined, contain half of the total number of
        elements, and
    C2. the rightmost element of A's left partition is less than or equal to
        the leftmost element of B's right partition, and
    C3. the rightmost element of B's left partition is less than or equal to
        the leftmost element of A's right partition,

then the median is either the smaller of the leftmost elements of the right
partitions or the average of these elements.

Let A be the smaller of the two arrays. Initially, partition A into halves (if
len(A) % 2, then left partition will contain one element more than the right).
To partition B, subtract the number of elements in A's left partition from half
of the total number of elements. B's left partition should contain the
resultant number of elements. By partitioning in this way, C1 will always be
satisfied.

Now the problem is a matter of adjusting where A is partitioned until C2 and C3
are satisfied. In other words, we are searching for the partition index i (the
left partition is A[:i + 1]) that satisfies C2 and C3. This can be done in
O(log(m + n)) time using binary search.

If C2 is not satisfied, then A's left partition must shrink and B's
left partition must grow (search continues within A's left partition, not
including i). If C3 is not satisfied, then A's left partition must grow and B's
left partition must shrink (search continues within A's right partition).
'''

if __name__ == '__main__':
    a = [1, 2, 3, 4]
    b = [1, 2, 3, 4, 5, 6, 7, 8]
    print(find_median(a, b))  

'''
The brute-force solution is to combine the arrays, sort the combined array, and
return its median. This is O((m + n)log(m + n)).

The linear solution is to start a pointer at the beginning of each array and
iterate the pointer that points to the smaller number. Do this (m + n) // 2
times and then return the median.
'''

