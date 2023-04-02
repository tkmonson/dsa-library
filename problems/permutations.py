'''
Permutations (#46)

Given an array `nums` of distinct integers, return all possible permutations in
any order.
'''

from math import factorial
from itertools import permutations

def permute(nums: list[int]) -> list[list[int]]:
    result = []
    visited = set()

    def backtracking(candidate):
        nonlocal result, visited
        if len(candidate) == len(nums):
            result.append(candidate)
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                backtracking(candidate + [nums[i]])
                visited.remove(i)

    backtracking([])
    return result

'''
This is a backtracking solution. Given [1, 2, 3], permutations will be added,
according to the following table, top-to-bottom and left-to-right ([], [1],
[1, 2], ...):

L0:  []
L1:  [1]                   [2]                   [3]
L2:  [1, 2]     [1, 3]     [2, 1]     [2, 3]     [3, 1]     [3, 2]
L3:  [1, 2, 3]  [1, 3, 2]  [2, 1, 3]  [2, 3, 1]  [3, 1, 2]  [3, 2, 1]

This is the preorder traversal of an n-ary tree, where each node
is a "partial candidate" and each child differs from its parent by only a
single "extension step." In a general backtracking scheme, each leaf is a
partial candidate that cannot be extended any further. Sometimes, this is the
case because the algorithm determines that the candidate cannot be extended to
a valid solution, so the potential subtree rooted at said candidate is skipped.
However, in this particular application of backtracking, each leaf is actually
a solution (which cannot be extended because, in this problem, each path
contains at most one solution).

The "take" or "not take" strategy of the knapsack problem is a form of
backtracking. When extending a partial permutation candidate, you can take or
not take the next element in nums, provided that it is not already in the
candidate. This solution prefers to take the next element (thus, [1, 2, 3] is
the first permutation generated). For example, consider the candidate [1]. Only
after choosing to "take" the next element (2) and to explore the subtree rooted
at the resulting candidate ([1, 2]) will it choose to "not take" said element,
to take the next next element (3) instead, and to explore the subtree rooted at
the resulting candidate ([1, 3]).
'''

# Cheating solution
def permute2(nums: list[int]) -> list[list[int]]:
    return permutations(nums)


if __name__ == '__main__':
    nums = [6, 3, 2, 7, 4, -1]
    nums = [1, 2, 3, 4]
    print(permute(nums))


# DOES NOT WORK
def permute3(nums: list[int]) -> list[list[int]]:
    result = []
    i, n = 0, len(nums)
    if n == 1:
        return [nums]

    for _ in range(factorial(n) // 2):
        result.append(list(nums))
        result.append(nums[::-1])
        j = i + 1 if i + 1 < n else 0
        nums[i], nums[j] = nums[j], nums[i]
        i = j

    return result

'''
The first strategy I thought of while approaching this problem was
DFS/backtracking, as utilized above in the working solution, but I assumed it
would be too memory-intensive (current candidate + remaining elements stored in
every recursive call), so I decided to try a different strategy. I thought that
there might be some way to swap elements in nums to create different
permutations.

Starting at i = 0, I swapped nums[i] and nums[i + 1], and I
considered nums to be a circular array (so nums[n - 1] and nums[0] would swap).
I swapped until enough permutations were generated. Surprisingly, this worked
for n <= 3.

I modified the algorithm to swap half as many times as the number of required
permutations, but each time I saved the result and its reverse. Surprisingly,
this worked for n <= 5. There seems to be some kind of pattern here, but I
couldn't find a solution for arbitrary n.
'''

