'''
Sort Colors (#75)

Given an array `nums` with `n` objects colored red, white, or blue, sort them
in-place so that objects of the same color are adjacent, with the colors in the
order red, white, and blue. We will use the integers 0, 1, and 2 to represent
the color red, white, and blue, respectively.
'''

# Time: O(n)
# Auxiliary space: O(1)
def sort_colors(nums: list[int]) -> None:
    lo = mid = 0
    hi = len(nums) - 1

    while mid <= hi:
        print(nums)
        if nums[mid] == 0:
            nums[lo], nums[mid] = nums[mid], nums[lo]
            lo += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[hi] = nums[hi], nums[mid]
            hi -= 1

'''
This is the Dutch National Flag algorithm. 0s are moved to the left, 2s are
moved to the right, and 1s stay in the middle. lo always points to the
non-inclusive end of the red section. mid always points to the non-inclusive
end of the white section. hi always points to the non-inclusive start of the
blue section.
'''
        
# Time: O(n)
# Auxiliary space: O(1)
def sort_colors2(nums: list[int]) -> None:
    R = W = B = 0
    while B < len(nums):
        if nums[B] == 1:
            nums[W] = 1
            W += 1
            if B >= W:
                nums[B] = 2
        elif nums[B] == 0:
            nums[R] = 0
            R += 1
            if W >= R:
                nums[W] = 1
            W += 1
            if B >= W:
                nums[B] = 2
        B += 1

'''
To do this in one pass, the colors that we come across have to be placed in
the section they belong. Use pointers to mark the end of each section
(non-inclusive).

    0 0 1 1 2 2
        R   W   B

If a red is placed, a sorted white will be overwritten on the left end of the
section, assuming one exists. The white can be replaced at W, the right end of
the section, but this will overwrite a sorted blue on the left end of the blue
section, if one exists. It can be replaced at B, the right side of the section.
If a section is modified, the pointer should increment.
'''

if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    sort_colors(nums)
    print(nums)
