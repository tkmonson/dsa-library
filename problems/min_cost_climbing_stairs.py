'''
Min Cost Climbing Stairs (#746)

You are given an integer array `cost` where `cost[i]` is the cost of the ith
step on a staircase. Once you pay the cost, you can either climb one or two
steps. You can either start from the 0th or 1st step. Return the minimum cost
to climb the entire staircase.
'''

from contextlib import suppress
from functools import cache

def min_cost_climbing_stairs_memo(cost: list[int]) -> int:
    @cache
    def f(i):
        a = b = 0
        with suppress(IndexError):
            a = cost[i] + f(i + 1)
            b = cost[i + 1] + f(i + 2)

        return min(a, b)

    return f(0)

'''
Let f(i) be the min cost of climbing a staircase that starts at step i.
f(i) = min(cost[i] + f(i + 1), cost[i + 1] + f(i + 2)).
'''

def min_cost_climbing_stairs_tab(cost: list[int]) -> int:
    n = len(cost)
    dp = [0] * n
    dp[n - 1] = cost[n - 1]
    dp[n - 2] = cost[n - 2]

    for i in range(n - 3, -1, -1):
        dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
    return min(dp[0], dp[1])


def min_cost_climbing_stairs_tab2(cost: list[int]) -> int:
    for i in range(len(cost) - 3, -1, -1):
        cost[i] += min(cost[i + 1], cost[i + 2])
    return min(cost[0], cost[1])


def min_cost_climbing_stairs_tab3(cost: list[int]) -> int:
    dp = cost[:2]
    for i in range(2, len(cost)):
        dp.append(min(dp[i - 1], dp[i - 2]) + cost[i])
    return min(dp[-1], dp[-2])


def min_cost_climbing_stairs_tab4(cost: list[int]) -> int:
    for i in range(2, len(cost)):
        cost[i] += min(cost[i - 1], cost[i - 2])
    return min(cost[-1], cost[-2])

'''
Let dp[i] be the min cost of being able to move from step i.

When traversing left-to-right:
dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

When traversing right-to-left:
dp[i] = min(dp[i + 1], dp[i + 2]) + cost[i]
'''

if __name__ == '__main__':
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(min_cost_climbing_stairs_tab4(cost))

