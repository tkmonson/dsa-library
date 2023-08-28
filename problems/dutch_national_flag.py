'''
Sort Colors (#75)

Given balls of three colors, red, white, and blue, arrange them such that balls
of the same color are adjacent, with the colors in the order red, white, and
blue. Let 0, 1, and 2 represent the colors red, white, and blue respectively.

This problem is also known as the Dutch national flag problem because it is
about grouping colors together, similar to how they are grouped on the Dutch
national flag.
'''

def sort_colors(nums: list[int]) -> None:
    red, white, blue = 0, 0, 0
    for num in nums:
        if num == 0:
            red += 1
        elif num == 1:
            white += 1
        else:
            blue += 1
    nums[:red] = [0] * red
    nums[red : red + white] = [1] * white
    nums[red + white:] = [2] * blue

'''
Count occurrences, overwrite entire array based on those counts.
'''

def sort_colors2(nums: list[int]) -> None:
    red, white, blue = 0, 0, len(nums) - 1

    while white <= blue:
        if nums[white] == 0:
            nums[red], nums[white] = nums[white], nums[red]
            red += 1
            white += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1

'''
There are three pointers: R, W, and B. At all times, elements to the left of
R are red, elements to the right of B are blue, elements to the left of W but
not to the left of R are white, and everything else (elements to the left of B
but not to the left of W) is uncategorized. Initially, all elements are
uncategorized; at the end, they are all categorized.

This solution is also known as the 3-Way Partition Quicksort. Whereas the
standard 2-way partition quicksort partitions an array into two subarrays of
elements, those less than or equal to the pivot and those greater than the
pivot, this algorithm partitions an array into a three subarrays of elements,
those less than the pivot, those equal to the pivot, and those greater than the
pivot. This algorithm is O(n) when sorting an array with few (O(1)) unique
keys.
'''

if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    sort_colors(nums)
    print(nums)

