'''
4Sum (#18)

Given an array `nums` of `n` integers, return an array of all the unique
quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:

    * `0 <= a, b, c, d < n`
    * `a`, `b`, `c`, and `d` are distinct.
    * `nums[a] + nums[b] + nums[c] + nums[d] == target`

You may return the answer in any order.
'''

# Time: O(n^3)
# Auxiliary space: O(n)
def four_sum(nums: list[int], target: int) -> list[list[int]]:
    res = []
    nums.sort()
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:  # no duplicates for 1st element
            continue
        for j in range(i + 1, len(nums)):
            b = nums[j]
            if j > i + 1 and b == nums[j - 1]:  # no duplicates for 2nd element
                continue

            L, R = j + 1, len(nums) - 1
            while L < R:
                four_sum = a + b + nums[L] + nums[R]
                if four_sum > target:
                    R -= 1
                elif four_sum < target:
                    L += 1
                else:
                    res.append([a, b, nums[L], nums[R]])
                    L += 1
                    while nums[L] == nums[L - 1] and L < R:  # no duplicates
                        L += 1                               # for 3rd element

    return res

'''
This is just 3Sum with an additional for-loop.
'''

# Time: O(n^3)
# Auxiliary space: O(n)
def four_sum_recur(nums: list[int], target: int) -> list[list[int]]:
    res, quad = [], []
    nums.sort()

    def k_sum(k, start, target):
        if k != 2:
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                quad.append(nums[i])
                k_sum(k - 1, i + 1, target - nums[i])
                quad.pop()
            return
        
        # base case (two sum II)
        L, R = start, len(nums) - 1
        while L < R:
            if nums[L] + nums[R] > target:
                R -= 1
            elif nums[L] + nums[R] < target:
                L += 1
            else:
                res.append(quad + [nums[L], nums[R]])
                L += 1
                while L < R and nums[L] == nums[L - 1]:
                    L += 1

    k_sum(4, 0, target)
    return res

'''
A general kSum implementation, written recursively.
'''

# Time: O(n^3) (15x faster)
# Auxiliary space: O(n)
def four_sum_fast(nums: list[int], target: int) -> list[list[int]]:
    n = len(nums)
    if n < 4:
        return []
    nums.sort()
    res = []

    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
            break
        if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
            continue
        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                break
            if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                continue
                
            L, R = j + 1, len(nums) - 1
            while L < R:
                four_sum = nums[i] + nums[j] + nums[L] + nums[R]
                if four_sum > target:
                    R -= 1
                elif four_sum < target:
                    L += 1
                else:
                    res.append([nums[i], nums[j], nums[L], nums[R]])
                    L += 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                
    return res

'''
This one is so fast because it quits early on combinations where there is no
chance of success.

If n = 10 and you selected your first element at i = 2, then a[2] + a[7] + a[8]
+ a[9] is the largest sum you can make. If it is smaller than the target, there
is no need to check (a[2] + ...); you need to move on and select a[3] as the
first element. This is the only action that may produce a larger sum.

Similarly, a[2] + a[3] + a[4] + a[5] is the smallest sum you can make. If it is
larger than the target, there is no need to check (a[2] + anything else) or
(a[3] + anything else); every upcoming combination is too large, so you can
terminate the search.
'''

if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(four_sum(nums, target))
