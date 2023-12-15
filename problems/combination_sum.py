'''
Combination Sum (#39)

Given an array of distinct integers `candidates` and an integer `target`,
return a list of all unique combinations of candidates where the chosen numbers
sum to `target`. You may return the combinations in any order. The same number
may be chosen from `candidates` an unlimited number of times. Two combinations
are unique if the frequency of at least one of the chosen numbers is different.

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
1 <= target <= 40
'''

def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    result = []
    curr = []

    def dfs(n, target):
        if target == 0:
            result.append(curr[:])
            return
        if n == 0:
            return

        num = candidates[n - 1]
        if num <= target:
            curr.append(num)
            dfs(n, target - num)  # take
            curr.pop()
        dfs(n - 1, target)  # not take

    dfs(len(candidates), target)
    return result

'''
My initial backtracking solution. This solution shows how similar this problem
is to the unbounded knapsack problem. You can only choose to "take" a candidate
if it is less than or equal to the current target (pool of candidates stays the
same, target decreases by value of taken candidate). You can always choose to
"not take" a candidate (the size of the pool of candidates will decrement).
'''

def combination_sum2(candidates: list[int], target: int) -> list[list[int]]:
    result = []
    curr = []

    def dfs(curr_sum, idx):
        if curr_sum == target:
            result.append(curr[:])
        if curr_sum < target:
            for i in range(idx, len(candidates)):
                curr.append(candidates[i])
                dfs(curr_sum + candidates[i], i)
                curr.pop()

    dfs(0, 0)
    return result

'''
A slightly more refined backtracking solution. Here there is only one explicit
"take" call. If taking is not possible, the call will return (backtrack) and i
will increment, which represents a "not take."
'''

# Slower
def combination_sum3(candidates: list[int], target: int) -> list[list[int]]:
    idx_d = {val: idx for idx, val in enumerate(candidates)}
    n = len(candidates)
    dp = [[] for _ in range(target + 1)]
    dp[0].append([])
    for i in range(1, target + 1):
        for j in range(i):
            for comb in dp[j]:  
                start_idx = idx_d[comb[-1]] if comb else 0
                for val in candidates[start_idx:]:
                    if val + j == i:
                        dp[i].append(comb + [val])
    return dp[-1]

'''
This is a tabulation solution that seeks to find all of the combinations that
sum to 1, 2, ..., and target. Let dp[0] contain the empty list. When filling
the table row dp[i] with combinations that sum to i, consider the combinations
in each previous row that sum to lesser targets. If a candidate can be appended
to one of these lesser combinations such that the new combination sums to i,
that is a valid combination that can be added to dp[i] if that candidate does
not come before the last element of the lesser combination in the list of
candidates or if the lesser combination is empty. (This stipulation is in
accordance with "taking" and "not taking" in the unbounded knapsack problem.
You can take an item as many times as your capacity allows, but once you decide
to not take it, you move on to consider the other items.) After the table is
full, return dp[target].
'''

def combination_sum4(candidates: list[int], target: int) -> list[list[int]]:
    dp = [[] for _ in range(target + 1)]
    dp[0].append([])
    for c in candidates:
        for i in range(c, target + 1):
            for comb in dp[i - c]:
                dp[i].append(comb + [c])
    return dp[-1]

'''
Another tabulation solution. Let dp[0] contain the empty list. For all targets
i from c to target, each combination in dp[i - c], once appended with c, can be
added to dp[i].
'''

if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    print(combination_sum4(candidates, target))

