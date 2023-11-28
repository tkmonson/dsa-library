'''
Single Number (#136)

Given a non-empty array of integers where every element appears twice except
for one, return that single element.
'''

from functools import reduce

def single_number(nums: list[int]) -> int:
    return reduce(lambda x, y: x ^ y, nums)  # if x == y, x ^ y == 0

if __name__ == '__main__':
    nums = [4, 1, 2, 1, 2]
    print(single_number(nums))

