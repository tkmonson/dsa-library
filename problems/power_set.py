'''
Subsets (#78)

Given an integer array of unique elements, return all possible subsets (the
power set). The solution must not contain duplicate subsets. Return the
solution in any order.
'''

from itertools import combinations

# Time: O(n*2^n)
# Auxiliary space: O(n*2^n)
def subsets_recur(nums: list[int]) -> list[list[int]]:
    power_set = []
    def f(subset, i):
        if i == len(nums):
            power_set.append(subset)
            return
        f(subset.copy(), i + 1)
        subset.append(nums[i])
        f(subset.copy(), i + 1)
    
    f([], 0)
    return power_set

'''
    {1, 2, 3}  =>
                             {}
                 ___________/  \___________
    1:         {}                          {1}
            __/  \___                 ____/   \____
    2:    {}         {2}           {1}             {1,2}
         /  \       /   \         /   \           /     \
    3: {}    {3} {2}     {2,3} {1}     {1,3} {1,2}       {1,2,3}
'''

def subsets_iter(nums: list[int]) -> list[list[int]]:
    power_set = [[]]
    for n in nums:
        power_set += [s + [n] for s in power_set]        
    return power_set


def subsets_lib(nums: list[int]) -> list[list[int]]:
    power_set = []
    for i in range(len(nums) + 1):
        power_set += combinations(nums, i)
    return [list(s) for s in power_set]


# Fastest
def subsets_bit(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    power_set = [[]]

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

        power_set.append(subset)
        mask -= 1

    return power_set

'''
Power sets have a close relationship with binary representation. For a set of n
elements, each member of its power set can be represented by a number from 0
to 2^n - 1, where each bit in the binary representation expresses whether or
not a particular element of the set is present.
'''

if __name__ == '__main__':
    nums = [1, 2, 3]
    print(subsets2(nums))

