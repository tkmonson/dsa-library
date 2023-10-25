'''
3Sum (#15)

Given an integer array `nums`, return all the triplets `[nums[i], nums[j],
nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] +
nums[k] == 0`. The triplets in the solution set must be distinct sets.
'''

from itertools import combinations

def three_sum_naive(nums: list[int]) -> list[list[int]]:
    triplets = set()
    nums.sort()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplets.add((nums[i], nums[j], nums[k]))
    return triplets


def three_sum(nums: list[int]) -> list[list[int]]:
    triplets = set()
    nums.sort()
    for i in range(len(nums) - 2):
        hash_map = {}
        target = -nums[i]
        for j in range(i + 1, len(nums)):
            if nums[j] in hash_map:
                triplets.add((nums[i], hash_map[nums[j]], nums[j]))
            else:
                hash_map[target - nums[j]] = nums[j]
    return [list(triplet) for triplet in triplets]


def three_sum2(nums: list[int]) -> list[list[int]]:
    triplets = set()

    # 1. Split nums into three sets: negatives, positives, and zeros
    n, p, z = [], [], []
    for num in nums:
        if num < 0:
            n.append(num)
        elif num > 0:
            p.append(num)
        else:
            z.append(num)

    # 2. Create separate sets for negatives and positives for O(1) lookup times
    N, P = set(n), set(p)

    # 3. Add all triplets that contain 1 or 3 zeros
    if z:
        for num in P:
            if -num in N:
                triplets.add((-num, 0, num))
        if len(z) >= 3:
            triplets.add((0, 0, 0))

    # 4. For all pairs of negative numbers, check if their complement exists in P
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            target = -(n[i] + n[j])
            if target in P:
                triplets.add(tuple(sorted([n[i], n[j], target])))

    # 5. For all pairs of positive numbers, check if their complement exists in N
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            target = -(p[i] + p[j])
            if target in N:
                triplets.add(tuple(sorted([p[i], p[j], target])))

    return [list(triplet) for triplet in triplets]


def three_sum3(nums: list[int]) -> list[list[int]]:
    triplets = set()

    n, p, z = [], [], []
    for num in nums:
        if num < 0:
            n.append(num)
        elif num > 0:
            p.append(num)
        else:
            z.append(num)

    S = set(nums)

    if z:
        for num in p:
            if -num in S:
                triplets.add((-num, 0, num))
        if len(z) >= 3:
            triplets.add((0, 0, 0))

    for s in [n, p]:
        for x, y in combinations(s, 2):
            target = -(x + y)
            if target in S:
                triplets.add(tuple(sorted([x, y, target])))

    return [list(triplet) for triplet in triplets]


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(three_sum3(nums))

