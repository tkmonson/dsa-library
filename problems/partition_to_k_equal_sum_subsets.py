'''
Partition to K Equal Sum Subsets (#698)

Given an integer array nums and an integer k, return true if it is possible to
divide this array into k non-empty subsets whose sums are all equal.

1 <= nums[i] <= 10^4
'''

# Time: O(k*2^n)
# Auxiliary space: O(n)
def can_partition_k_subsets(nums: list[int], k: int) -> bool:
    s = sum(nums)
    if s % k > 0:
        return False

    target = s // k
    if max(nums) > target:
        return False
    
    nums.sort(reverse=True)
    used = [False for _ in range(len(nums))]

    def backtrack(i, k, subset_sum):
        if k == 0:
            return True
        if subset_sum == target:
            return backtrack(0, k - 1, 0)
        
        for j in range(i, len(nums)):
            if used[j] or subset_sum + nums[j] > target:
                continue
            
            used[j] = True
            if backtrack(j + 1, k, subset_sum + nums[j]):
                return True
            used[j] = False

            if subset_sum == 0: # Pruning
                return False

        return False
    
    return backtrack(0, k, 0)

'''
If your target sum is 5, how would you know if you should group a 3 with a 2 or
with 2 1s? You would need to explore recursively and backtrack.

Try to fill one subset at a time. If an element has not been used yet and fits,
add it to the subset and recur. When a subset is filled, start at the beginning
of nums again to consider the remaining elements.

Sorting nums in descending order helps to fail faster.

If an element is placed into an empty subset and its recursive subtree exits
without returning True, then it will not fit anywhere, given the previous
decisions. You need to backtrack to an earlier state.
'''

# TLE
def can_partition_k_subsets2(nums: list[int], k: int) -> bool:
    s = sum(nums)
    if s % k > 0:
        return False

    target = s // k
    if max(nums) > target:
        return False
    
    subsets = [0 for _ in range(k)]
    nums.sort(reverse=True)

    def dfs(i):
        nonlocal subsets
        if i == len(nums):
            for n in subsets:
                if n != target:
                    return False
            return True

        for j in range(k):
            if nums[i] + subsets[j] <= target:
                subsets[j] += nums[i]
                if dfs(i + 1):
                    return True
                subsets[j] -= nums[i]

                if subsets[j] == 0: # Pruning
                    return False

        return False

    return dfs(0)

'''
This solution exceeds the time limit without the pruning check, so it's a bit
slower. Possibly because it doesn't try to fill one subset first, which means
the search remains high complexity the whole time.
'''

if __name__ == '__main__':
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    print(can_partition_k_subsets(nums, k))

'''
There are other solutions that memoize/tabulate the "used" state.
'''