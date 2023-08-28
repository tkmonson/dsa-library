'''
Next Permutation (#31)

A permutation of an array of integers is a sequential arrangement of its
elements. For example, the permutations of [1, 2, 3] are [1, 2, 3], [1, 3, 2],
[2, 1, 3], [2, 3, 1], [3, 1, 2], and [3, 2, 1].

The next permutation of an array of integers is the permutation that follows
the given array in the lexicographic ordering of the array's permutations. If
the given array is the last permutation in the order, its next permutation is
the first permutation in the order. For example, next([1, 2, 3]) = [1, 3, 2],
next([2, 1, 3]) = [2, 3, 1], and next([3, 2, 1]) = [1, 2, 3].

Given an array of integers, transform the array into its next permutation by
modifying it in-place, using only constant space.
'''

# Time: O(n)
# Auxiliary space: O(1)
def next_permutation(nums: list[int]) -> None:
    n = len(nums)
    def reverse_suffix(i):
        j = n - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    # Find suffix and pivot
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i == -1:
        reverse_suffix(0)
        return
    pivot = nums[i]

    # Find element in suffix to swap with pivot; swap; reverse suffix
    j = i + 1
    while j < n and pivot < nums[j]:
        j += 1
    nums[i], nums[j - 1] = nums[j - 1], nums[i]
    reverse_suffix(i + 1)

'''
Similar to binary numbers, the leftmost element is most significant and the
rightmost element is least significant. To get to the next permutation, we need
to "increase" the given array as little as possible. To do this, we should
consider modifying less significant elements before more significant elements.

Find the longest non-increasing suffix (subarray that includes the last element
of the array). The elements of this suffix cannot be rearranged to increase the
value of the array; they are already arranged in their highest permutation.
Thus, we need to modify some element outside of the suffix, and the least
significant element outside of it is the one immediately to the left of it, and
this element is guaranteed to be smaller than the head of the suffix. Let this
element be the pivot.

To increase the value of the array, the pivot needs to be swapped with an
element to the right of it that is larger. To increase the value of the array
as little as possible, the pivot needs to be swapped with the smallest and
least significant element in the suffix that is larger than the pivot.

After the swap is performed, the suffix needs to be sorted into its lowest
permutation (non-decreasing). But the suffix is guaranteed to still be
non-increasing after the swap, so we can simply reverse the suffix to put it
into its lowest permutation.
'''

if __name__ == '__main__':
    nums = [0, 1, 2, 5, 3, 3, 0]
    next_permutation(nums)

