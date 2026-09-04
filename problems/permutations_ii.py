'''
Permutations II (#47)

Given a collection of numbers, `nums`, that might contain duplicates, return
all possible unique permutations in any order.
'''

from collections import Counter

# Time: O(n! * n) = O(n!) (n! perms; for each, there is a copy operation)
# Auxiliary space: O(n) (O(n!) including output)
def permute(nums: list[int]) -> list[list[int]]:
    result = []
    candidate = []

    count = Counter(nums)
    
    def dfs():
        if len(candidate) == len(nums):
            result.append(candidate.copy())
            return

        for num in count.keys():
            if count[num] == 0:
                continue

            candidate.append(num)
            count[num] -= 1
            dfs()
            candidate.pop()
            count[num] += 1

    dfs()
    return result

'''
This is the same as the solution to Permutations I, but this time we keep a
count for the elements of nums. Then, the check is not if the current num is
already in the candidate; the check is whether you have any of the current num
remaining.
'''

if __name__ == '__main__':
    nums = [1,1,2]
    print(permute(nums))
