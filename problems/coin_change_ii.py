'''
Coin Change II (#518)

Given an integer array `coins` representing coins of different denominations
and an integer `amount` representing a total amount of money, return the number
of combinations that make up that amount. There is an infinite number of each
kind of coin. The coin denominations are unique.
'''

from functools import cache

def coin_change_memo(amount: int, coins: list[int]) -> int:
    @cache
    def f(i, w):
        if i < 0 or w < 0:
            return 0
        if w == 0:
            return 1
        return f(i, w - coins[i]) + f(i - 1, w)

    return f(len(coins) - 1, amount)
 
 
def coin_change_tab_2d(amount: int, coins: list[int]) -> int:
    n = len(coins)
    dp = [[0] * (amount + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        coin = coins[i - 1]
        for w in range(1, amount + 1):
            if coin > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = dp[i][w - coin] + dp[i - 1][w]

    return dp[-1][-1]


def coin_change_tab_1d(amount: int, coins: list[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1
 
    for coin in coins:
        for w in range(coin, amount + 1):
            dp[w] += dp[w - coin]
 
    return dp[-1]

'''
The 1D array holds values from the (i - 1)th and ith rows of the 2D solution.
The (i - 1)th row values are updated to ith row values from left to right.
Thus, dp[w] corresponds to dp[i - 1][w] above and dp[w - coin] corresponds to
dp[i][w - coin] above.
'''

if __name__ == '__main__':
    amount = 5
    coins = [1, 2, 5]
    print(coin_change_tab(amount, coins))

'''
This is an unbounded knapsack problem, but instead of finding an optimal
combination of coins, we are counting the number of valid combinations.
'''

