'''
Last Stone Weight II (#1049)

You are given an array of integers `stones` where `stones[i]` is the weight of
the ith stone. We are playing a game with the stones. On each turn, we choose
any two stones and smash them together. Suppose the stones have weights `x` and
`y` with `x <= y`. The result of this smash is:

    * If `x == y`, both stones are destroyed, and
    * If `x != y`, the stone of weight `x` is destroyed, and the stone of
      weight `y` has new weight `y - x`.

At the end of the game, there is at most one stone left. Return the smallest
possible weight of the left stone. If there are no stones left, return 0.
'''

# Time: O(n * t)
# Auxiliary space: O(n * t)
def last_stone_weight_ii(stones: list[int]) -> int:
    n, t = len(stones), sum(stones)
    dp = [[-1 for _ in range(t)] for _ in range(n)]

    def dfs(i, w):
        if i == n or w == 0:
            return 0

        if dp[i][w] == -1:
            if stones[i] > w:
                dp[i][w] = dfs(i + 1, w)
            else:
                dp[i][w] = max(stones[i] + dfs(i + 1, w - stones[i]), dfs(i + 1, w))

        return dp[i][w]

    subset_sum = dfs(0, t // 2)
    return (t - subset_sum) - subset_sum

'''
The naive solution is to simulate every combination of stones being smashed
together. This would be O(n^2) states just for the first decision and it would
explode in complexity as you move down the decision tree. This is not viable.

You want to split this set of stones into two subsets, which will smash into
each other. The final result is equal to the absolute difference of the two
groups of stones, so it will be minimized if the subsets are as close as
possible to each other in weight.

By changing the decision from "which two stones to smash together" to "which
group does this stone belong to", the solution reduces to a binary decision
tree with O(2^n) complexity. But there are overlapping subproblems, so the
solution can be further improved.

If you select a subset of the stones that sums to x, then the subset of
remaining stones will sum to t - x, where t is the total sum. So you want to
minimize t - 2x, which you can do by selecting the subset with x as close as
possible to t // 2 (the target). That means this is now a 0-1 knapsack problem.

Value and weight of each item can be equal in this case. We don't want the
weight to exceed the target, but we also want the value to be as close to the
target as possible.
'''

# Time: O(n * t)
# Auxiliary space: O(n * t)
def last_stone_weight_ii_tab(stones: list[int]) -> int:
    total = sum(stones)
    target = total // 2
    dp = [0] * (target + 1)

    for i in range(1, len(stones) + 1):
        for w in range(target, stones[i - 1] - 1, -1):
            dp[w] = max(stones[i - 1] + dp[w - stones[i - 1]], dp[w])

    return (total - dp[target]) - dp[target]


# Time: O(n * t)
# Auxiliary space: O(n * t)
def last_stone_weight_ii_tab2(stones: list[int]) -> int:
    total = sum(stones)
    target = total // 2

    dp = [False] * (target + 1)
    dp[0] = True

    for stone in stones:
        for w in range(target, stone - 1, -1):
            dp[w] = dp[w] or dp[w - stone]
    
    for s in range(target, -1, -1):
        if dp[s]:
            return total - 2 * s
        
'''
A cool variant of the 1D tabulation solution. dp[s] tells you if you can make
a subset that sums to s. The set you can choose from expands by one stone each
loop. If you could sum to s before having access to the current stone, you can
still sum to s. Or if you can add the current stone to some previous subset
that summed to s - stone, you can sum to s. Find the sum closest to the target
that can be formed. That is the sum of your smaller subset.
'''

# Time: O(n * t) (beats 99%)
# Auxiliary space: O(n * t)
def last_stone_weight_ii_sign(stones: list[int]) -> int:
    dp = {0}
    for weight in stones:
        new_dp = set()
        for s in dp:
            new_dp.add(s + weight)
            new_dp.add(abs(s - weight))
        dp = new_dp
    return min(dp)

'''
We are adding or subtracting each stone from a running sum. Consider both
possibilities and keep track of all possible running sums for the previous
turn. If a sum goes negative, you can just interpret it as if the stones
so far actually belonged to the opposite subset, by taking the absolute value
instead (this cuts down on sums stored in dp). Return the sum closest to zero.
'''

if __name__ == '__main__':
    stones = [31, 26, 33, 21, 40]
    print(last_stone_weight_ii_tab(stones))
