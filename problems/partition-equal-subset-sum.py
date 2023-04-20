'''
Partition Equal Subset Sum (#416)

Given an integer array, return True if you can partition the array into two
subsets such that the sums of the elements in both subsets are equal or False
otherwise.
'''

def can_partition_memo(nums: list[int]) -> bool:
    if (total := sum(nums)) % 2 == 1:
        return False
    N, W = len(nums), total // 2
    dp = set()

    def f(n, w):
        if n == 0 or w < 0 or (n, w) in dp:
            return False
        if w == 0:
            return True

        if not (f(n - 1, w - nums[n - 1]) or f(n - 1, w)):
            dp.add((n, w))
        return not ((n, w) in dp)

    return f(N, W)

'''
This is a variation of the knapsack problem. You can choose to take or not take
each num in nums. Using recursion, you can explore all combinations of taking
and not taking these numbers. Memoization is used to avoid recomputation.
Because only a boolean value needs to be stored and because the first True will
initiate a backing out of the recursion, the cache can be a set that holds
(n, w) tuples that have previously returned False.
'''

def can_partition_tab(nums: list[int]) -> bool:
    if (total := sum(nums)) % 2 == 1:
        return False
    N, W = len(nums), total // 2
    dp = set([(i, 0) for i in range(N + 1)])

    for n in range(1, N + 1):
        for w in range(1, W + 1):
            if (n - 1, w - nums[n - 1]) in dp or (n - 1, w) in dp:
                dp.add((n, w))

    return (N, W) in dp

'''
This is a knapsack-style tabulation solution. It is quite slow because it is
evaluating every (n, w) tuple, even those that would never come up in the
memoization solution, but it does pass all test cases without timing out. 
'''

def can_partition_bit(nums: list[int]) -> bool:
    if sum(nums) % 2 > 0:
        return False

    target = sum(nums) // 2
    bit = 1

    for num in nums:
        bit = bit | bit << num
        
    return bit & 1 << target

'''
This bit manipulation solution is really cool and really fast, but I don't know
why it works.
'''

if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    print(can_partition_bit(nums))

'''
After recognizing that the subsets should both sum to half of the total sum of
nums (provided the total sum is even), this problem reduces to the subset sum
problem.
'''

