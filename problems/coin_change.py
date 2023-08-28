'''
Coin Change (#322)

You are given a list of integers representing coins of different denominations
and an integer representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that
amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
'''

import math

def coin_change(coins: list[int], amount: int) -> int:
    dp = [math.inf] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for w in range(coin, amount + 1):
            dp[w] = min(1 + dp[w - coin], dp[w])

    return -1 if dp[-1] == math.inf else dp[-1]

'''
This is a variation of the unbounded knapsack problem where the denominations
represent weight, each coin has a value of 1, we are trying to minimize value
instead of maximize it, and we must fill the knapsack to its full capacity.
'''

if __name__ == '__main__':
    coins = [1, 2, 5, 13]
    amount = 68
    print(coin_change(coins, amount))

