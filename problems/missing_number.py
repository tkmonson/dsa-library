'''
Missing Number (#268)

Given an array `nums` containing `n` distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.
'''

def missing_number(nums: list[int]) -> int:
    n = len(nums)
    return ((n * (n + 1)) >> 1) - sum(nums)

# Sum of arithmetic progression 1, 2, 3, ..., n = n(n + 1) // 2.

def missing_number2(nums: list[int]) -> int:
    return sum([i for i in range(len(nums) + 1)]) - sum(nums)

if __name__ == '__main__':
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print(missing_number(nums))

