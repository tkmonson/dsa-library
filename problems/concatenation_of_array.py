'''
Concatenation of Array (#1929)

Given an integer array `nums`, return an array that is the concatenation of two
`nums` arrays.
'''

def get_concatenation(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        nums.append(nums[i])
    return nums

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(get_concatenation(nums))
