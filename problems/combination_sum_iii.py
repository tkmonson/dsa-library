'''
Combination Sum III (#216)

Find all valid combinations of `k` numbers that sum to `n` such that the
following conditions are true:
    * Only numbers 1 through 9 are used
    * Each number is used at most once

Return a list of all possible valid combinations. The list must not contain the
same combination twice, and the combinations may be returned in any order.
'''

def combination_sum(k: int, n: int) -> list[list[int]]:
    curr = []
    result = []

    def dfs(curr_sum):
        if len(curr) == k:
            if curr_sum == n:
                result.append(curr[:])
            return
        if curr_sum > n:
            return

        i = curr[-1] + 1 if curr else 1
        while i < 10:
            curr.append(i)
            dfs(curr_sum + i)
            curr.pop()
            i += 1

    dfs(0)
    return result


if __name__ == '__main__':
    k = 3
    n = 9
    print(combination_sum(k, n))

