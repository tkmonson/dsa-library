'''
Combination Sum II (#40)

Given an array of integers `candidates` and an integer `target`, return a list
of all unique combinations of candidates where the chosen numbers sum to
`target`. You may return the combinations in any order. Each number in
`candidates` may only be used once in the combination. Two combinations are
unique if the frequency of at least one of the chosen numbers is different.

1 <= candidates.length <= 100
2 <= candidates[i] <= 50
1 <= target <= 30
'''

def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    result = []
    curr = []
    candidates.sort()

    def dfs(n, target):
        if target == 0:
            result.append(curr[:])
            return
        if n == 0:
            return

        num = candidates[n - 1]
        if num <= target:
            curr.append(num)
            dfs(n - 1, target - num)  # take
            curr.pop()
        while n > 0 and candidates[n - 1] == num:
            n -= 1
        dfs(n, target)  # not take

    dfs(len(candidates), target)
    return result

'''
A backtracking solution similar to the 0-1 knapsack problem. The candidates are
sorted to more easily avoid duplicate combinations. When "not taking" a
candidate, skip over any upcoming candidates of the same value (once you decide
to "not take," you must not "take" any of the same item in the future).
'''

def combination_sum2(candidates: list[int], target: int) -> list[list[int]]:
    result = []
    curr = []
    candidates.sort()

    def dfs(curr_sum, idx):
        if curr_sum == target:
            result.append(curr[:])
        elif curr_sum < target:
            i = idx
            while i < len(candidates):
                candidate = candidates[i]
                curr.append(candidate)
                dfs(curr_sum + candidate, i + 1)
                curr.pop()
                while i < len(candidates) and candidates[i] == candidate:
                    i += 1

    dfs(0, 0)
    return result

if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(combination_sum(candidates, target))

