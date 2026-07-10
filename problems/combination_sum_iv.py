'''
Combination Sum IV (#377)

Given an array of distinct integers `nums` and a target integer `target`,
return the number of possible *permutations* that add up to `target`.
'''

def combination_sum(nums: list[int], target: int) -> int:
    dp = {}
    def dfs(remainder):
        if remainder == 0:
            return 1
        if remainder in dp:
            return dp[remainder]

        count = 0
        for num in nums:
            if num <= remainder:
                count += dfs(remainder - num)

        dp[remainder] = count
        return count

    return dfs(target)

'''
Because different orderings count separately, there are overlapping subproblems.

For example, for nums = [1, 2, 3], target = 4, f(2) appears multiple times, and
the work is identical each time:

4 - 1 = 3
          - 1 = 2                  <-- !
                  - 1 = 1
                          - 1 = 0
                  - 2 = 0
          - 2 = 1
                  - 1 = 0
          - 3 = 0
  - 2 = 2                          <-- !
          - 1 = 1
                  - 1 = 0
          - 2 = 0
  - 3 = 1
          - 1 = 0

This differs from the combination problems because there it also mattered where
the pointer was in the candidates list. The remainder might be the same for two
subproblems, but the candidates available would differ, which means the work
would not be same:

4 - 1 = 3
          - 1 = 2                  <-- !
                  - 1 = 1
                          - 1 = 0
                  - 2 = 0
          - 3 = 0
  - 2 = 2                          <-- !
          - 2 = 0

The loop starts at the beginning of nums for each recursive step. Cache results
to subproblems.
'''

if __name__ == '__main__':
    nums = [1,2,3]
    target = 4
    print(combination_sum(nums, target))
