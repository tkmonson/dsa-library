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
