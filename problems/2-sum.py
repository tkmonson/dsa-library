'''
2Sum (#1)

Given an array of integers `nums` and an integer `target`, return the indicies
of the two numbers that add up to `target`. You may assume there is exactly one
pair of numbers that add up to `target`. You may not use the same element
twice. You can return the answer in any order.
'''

def two_sum_naive(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum(nums: list[int], target: int) -> list[int]:
    hash_map = {}
    for i in range(len(nums)):
        if nums[i] in hash_map:
            return [i, hash_map[nums[i]]]
        else:
            hash_map[target - nums[i]] = i


if __name__ == '__main__':
    nums = [2, 5, 9, 8, 14, 0, 1, -4]
    target = 10
    print(two_sum(nums, target))

