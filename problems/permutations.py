'''
Permutations (#46)

Given an array `nums` of distinct integers, return all possible permutations in
any order.
'''

from math import factorial
from itertools import permutations

# Time: O(n! * n) = O(n!) (n! perms; for each, there is a copy operation)
# Auxiliary space: O(n) (O(n!) including output)
def permute(nums: list[int]) -> list[list[int]]:
    result = []
    candidate = []
    
    def dfs():
        if len(candidate) == len(nums):
            result.append(candidate.copy())
            return

        for num in nums:
            if num in candidate:
                continue

            candidate.append(num)
            dfs()
            candidate.pop()

    dfs()
    return result

# Time: O(n! * n^2) = O(n!) (n! perms; for each, there are n insert operations)
# Auxiliary space: O(n! * n) = O(n!) (recursion depth of n; each recursive
#                                     state holds O(n!) perms)
def permute_topdown(nums: list[int]) -> list[list[int]]:
    if len(nums) == 0:
        return [[]]
    
    perms = permute(nums[1:])
    res = []
    for p in perms:
        for i in range(len(p) + 1):
            p_copy = p.copy()
            p_copy.insert(i, nums[0])
            res.append(p_copy)

    return res

'''
Finding all the permutations of [1, 2, 3] can be solved in terms of the
subproblem of finding all the permutations of [2, 3] (i.e. [2, 3], [3, 2]). By
inserting 1 in every possible location for all permutations of [2, 3], you get
all the permutations of [1, 2, 3]:
    * [1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]
'''

# Time: O(n!)
# Auxiliary space: O(n!)
def permute2_bottomup(nums: list[int]) -> list[list[int]]:
    perms = [[]]
    for n in nums:
        new_perms = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, n)
                new_perms.append(p_copy)
        perms = new_perms

    return perms

'''
Inserting nums[i] in all locations of all permutations of nums[:i] gets you all
the permutations of nums[:i + 1].

    * [[]], i = 0: [[1]]
    * [[1]], i = 1: [[2, 1], [1, 2]]
    * [[2, 1], [1, 2]], i = 2:
          [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]
'''

# Time: O(n!)
# Auxiliary space: O(n^2) (recursion depth of n; each holds a copy)
def permute_slow(nums: list[int]) -> list[list[int]]:
    result = []
    visited = set()

    def dfs(candidate):
        if len(candidate) == len(nums):
            result.append(candidate)
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                dfs(candidate + [nums[i]])
                visited.remove(i)

    dfs([])
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
def permute_cheat(nums: list[int]) -> list[list[int]]:
    return permutations(nums)


if __name__ == '__main__':
    nums = [1, 2, 3]
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

