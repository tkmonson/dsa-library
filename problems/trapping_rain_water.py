'''
Trapping Rain Water (#42)

Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water the terrain can trap after rain.

E.g. height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]  =>  6

|
|               #
|       # ~ ~ ~ # # ~ #
|   # ~ # # ~ # # # # # #
'''

from contextlib import suppress

# Time: O(n)
# Auxiliary space: O(1)
def trap(self, height: List[int]) -> int:
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    trapped_water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] > left_max:
                left_max = height[left]
            else:
                trapped_water += left_max - height[left]
            left += 1
        else:
            if height[right] > right_max:
                right_max = height[right]
            else:
                trapped_water += right_max - height[right]
            right -= 1
    return trapped_water


# Time: O(n)
# Auxiliary space: O(1)
def trap2(height: list[int]) -> int:
    left, end = 0, len(height) - 1
    with suppress(IndexError):
        while height[left] == 0:
            left += 1
    with suppress(IndexError):
        while height[end] == 0:
            end -= 1

    total, subtotal = 0, 0
    right = left
    while right <= end:
        if (diff := height[left] - height[right]) > 0:
            subtotal += diff
        else:
            total += subtotal
            subtotal = 0
            left = right
        right += 1
    right -= 1

    subtotal = 0
    end = left
    for left in range(right, end - 1, -1):
        if (diff := height[right] - height[left]) > 0:
            subtotal += diff
        else:
            total += subtotal
            subtotal = 0
            right = left
    
    return total

'''
Ignore leading and trailing zeros. Starting at the first non-zero column,
expand a window to the right, one column at a time, adding the difference
between the leftmost and rightmost column to a subtotal. When the difference is
non-positive, the window is "complete": add the subtotal to a total, reset the
subtotal, and reset the window, beginning at the previous rightmost column.
This will capture all water blocks, except for any that may exist in the final
window, in the case where the window does not "complete" before the end of the
map (the last non-zero column). To capture these missing blocks, perform the
same sliding window operation, this time moving from right to left, within the
range of this final window. Return the total.

The key here is that you don't know how many water blocks exist within an
incomplete window. But you do know that if you traverse an incomplete window in
reverse, the final column is guaranteed to be greater than all of the other
columns, which means that the final window in this reverse traversal is
guaranteed to be complete.
'''

if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap(height))

