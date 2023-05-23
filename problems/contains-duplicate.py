'''
Contains Duplicate (#217)

Given an integer array, return True if any value appears in the array more
than once, False otherwise.
'''

def contains_duplicate(nums: list[int]) -> bool:
    n = len(nums)
    nums = set(nums)
    return n != len(nums)

