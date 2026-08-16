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
