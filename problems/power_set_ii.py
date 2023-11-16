'''
Subsets II (#90)

Given an integer array that may contain duplicates, return all possible subsets
(the power set). The solution must not contain duplicate subsets. Return the
solution in any order. Note that a "subset of an array" can contain duplicates.

E.g. [1, 2, 2] => [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
'''

# Slow
def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    if len(nums) == 0:
        return [[]]
    else:
        ps_n1 = [tuple(s) for s in subsets_with_dup(nums[:-1])]
        ps_n = [tuple(sorted(s + (nums[-1],))) for s in ps_n1]
    return [list(s) for s in set(ps_n1 + ps_n)]


# Preferred
def subsets_with_dup_backtrack(nums: list[int]) -> list[list[int]]:
    power_set = []
    curr = []
    def backtrack(i):
        if i == len(nums):
            power_set.append(curr[:])
            return

        # Take
        curr.append(nums[i])
        backtrack(i + 1)

        # Not take
        curr.pop()
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        backtrack(i + 1)

    nums.sort()
    backtrack(0)
    return power_set

'''
To avoid the problem of duplicate subsets, as soon as you decide to "not take"
some value, you must not "take" a duplicate of that value going forward. To
easily avoid duplicate values, sort the array and skip over the whole
contiguous block of duplicates.

[1, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9]

Valid:          x  x  x
                ^  x  x
                ^  ^  x
                ^  ^  ^

Not valid:      x  ^  x
                x  x  ^
                ^  x  ^
                x  ^  ^
'''

def subsets_with_dup_bit(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    nums.sort()
    power_set = {()}

    mask = 2 ** n - 1
    while mask:
        copy = mask
        i = n - 1
        subset = []
        while copy:
            if copy & 1:
                subset.append(nums[i])
            i -= 1
            copy >>= 1

        power_set.add(tuple(subset))
        mask -= 1

    return [list(s) for s in power_set]


if __name__ == '__main__':
    nums = [4, 4, 4, 1, 4]
    print(subsets_with_dup_backtrack(nums))

