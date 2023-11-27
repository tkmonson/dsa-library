'''
Jump Game (#55)

Given an array where each element represents the maximum forward jump length
(in indicies) from that position, return True if you can reach the last index
from the first index, False otherwise.
'''

# Time: O(n)
# Auxiliary space: O(1)
def can_jump(nums: list[int]) -> bool:
    curr = nums[0]
    for i in range(1, len(nums)):
        if curr == 0:
            return False
        curr = max(curr - 1, nums[i])

    return True


# Time: O(n^2)
# Auxiliary space: O(1)
def can_jump_tabu(nums: list[int]) -> bool:
    n = len(nums)
    nums[-1] = -1
    for i in range(n - 2, -1, -1):
        max_jump_i = min(i + nums[i], n - 1)
        for j in range(max_jump_i, i, -1):
            if nums[j] < 0:
                nums[i] = -1
                break

    return nums[0] < 0


# Time: O(n^2)
# Auxiliary space: O(n)
def can_jump_memo(nums: list[int]) -> bool:
    n = len(nums)

    @cache
    def can_finish(i):
        if i == n - 1:
            return True

        max_jump_i = min(i + nums[i], n - 1)
        for j in range(max_jump_i, i, -1):
            if can_finish(j):
                return True

        return False

    return can_finish(0)


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    print(can_jump(nums))

