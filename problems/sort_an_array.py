'''
Sort An Array (#912)

Given an array of integers nums, sort the array in ascending order and return
it. You must solve the problem without using any built-in functions, in
O(nlogn) time complexity and with the smallest space complexity possible.
'''

'''
To solve this problem with the given constraints of O(nlogn) time and O(1)
space, iterative heapsort is really the only appropriate choice. Technically,
there are other options that can do this, but they are exotic.

While they do not satisfy the given constraints, Mergesort, Quicksort, and
Insertion Sort implementations are given below, for review.
'''

# Time: O(nlogn)
# Auxiliary space: O(1)
def heapsort(nums: list[int]) -> list[int]:
    def sift_down(i, heap_size):
        while (left_i := 2 * i + 1) <= heap_size - 1:
            right_i = 2 * i + 2

            left_value = nums[left_i]
            right_value = left_value if right_i > heap_size - 1 else nums[right_i]
            max_child_i = left_i if left_value >= right_value else right_i

            if nums[i] >= nums[max_child_i]:
                break

            nums[i], nums[max_child_i] = nums[max_child_i], nums[i]
            i = max_child_i

    def heapify(nums):
        last_parent_i = (len(nums) - 1) // 2
        for i in range(last_parent_i, -1, -1):
            sift_down(i, len(nums))

    heapify(nums)
    for i in range(len(nums) - 1, -1, -1):
        nums[0], nums[i] = nums[i], nums[0]
        sift_down(0, i)

    return nums

'''
Left child of i =   2i + 1
Right child of i =  2i + 2
Parent of i =       (i - 1) // 2
Last parent =       (len(a) - 1) // 2

1. Heapify the array (sift down on all non-leafs, in decreasing order of index)
2. Pop each element in-place
       * Swap root with last element
       * Sift down on root (decrement right heap boundary)

Sift down (max heap):
    * If i is a leaf (left child is out-of-bounds), return
    * If i >= its children, return
    * Swap values between i and c_i, the max child of i
    * Sift down on c_i

To sort in-place using heapsort, the sift down function needs to know how large
the heap is, because it decreases in size as sorted elements are stored at the
end. It also needs to be implemented iteratively, to avoid using stack space.
'''

# Time: O(nlogn)
# Auxiliary space: O(n)
def mergesort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left_half = nums[:mid]
    right_half = nums[mid:]

    sorted_left = mergesort(left_half)
    sorted_right = mergesort(right_half)

    return merge(sorted_left, sorted_right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

'''
1. Split the array into halves, recursively
2. When the array has one element, it is sorted
3. Merge the sorted halves together

Merge:
    * Keep separate pointers for left and right
    * Add smaller element to result, increment for that half
    * When one half is exhausted, add the rest of the other half to result
'''

# Time: O(n^2) (O(nlogn) average)
# Auxiliary space: O(logn) (stack space)
def quicksort(nums: list[int]) -> list[int]:
    def partition(lo, hi):
        pivot = nums[hi]

        follower = lo - 1
        for leader in range(lo, hi):
            if nums[leader] < pivot:
                follower += 1
                nums[follower], nums[leader] = nums[leader], nums[follower]

        nums[follower + 1], nums[hi] = nums[hi], nums[follower + 1]
        return follower + 1

    def _quicksort(lo, hi):
        if lo < hi:
            pivot_index = partition(lo, hi)
            _quicksort(lo, pivot_index - 1)
            _quicksort(pivot_index + 1, hi)

    _quicksort(0, len(nums) - 1)
    return nums

'''
Simplest version of Quicksort, using Lomuto's partition scheme:

1. Choose the last element as the pivot
2. Follower always points to last element less than pivot,
   Leader looks for next element less than pivot
   When leader finds one, follower increments, leader swaps with follower
   (follower is pointing momentarily to an element leader already checked)
3. Continue until leader traverses whole array except pivot
4. Swap pivot with follower + 1 (the first element greater than pivot)
5. Pivot is now sorted; recur on left and right subarrays
'''

# Time: O(n^2)
# Auxiliary space: O(1)
def insertion_sort(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
    return nums

'''
Insertion sort is how one would naturally sort a new card into a sorted hand.
Draw a card. Compare it to the sorted cards in your hand, from right to left.
Shift larger cards to the right until you find the correct empty slot, then
insert the card.

1. Consider the first element sorted
2. Traverse through the rest of the cards left to right
3. Sift each one down until it is in its proper place
'''

if __name__ == '__main__':
    nums = [17, 3, 2, 1, 100, 7, 19, 36, 25]
    print(heapsort(nums))
