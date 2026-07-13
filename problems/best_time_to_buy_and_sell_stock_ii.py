'''
Best Time to Buy and Sell Stock II (#122)

You are given an integer array `prices` where `prices[i]` is the price of a
given stock on the `ith` day. On each day, you may decide to buy and/or sell
the stock. You can only hold at most one share of the stock at any time.
However, you can sell and buy the stock multiple times on the same day,
ensuring you never hold more than one share of the stock (i.e. you are allowed
to do nothing on any given day).

Find and return the maximum profit you can achieve.
'''

# Time: O(n)
# Auxiliary space: O(1)
def max_profit(prices: list[int]) -> int:
    profit = 0
    for i in range(1, len(prices)):
        if prices[i - 1] < prices[i]:
            profit += prices[i] - prices[i - 1]
    return profit


# Time: O(n)
# Auxiliary space: O(1)
def max_profit2(prices: list[int]) -> int:
    profit = 0
    has_stock = False
    for i in range(len(prices) - 1):
        if has_stock:
            if prices[i + 1] < prices[i]:
                profit += prices[i]
                has_stock = False
        else:
            if prices[i + 1] > prices[i]:
                profit -= prices[i]
                has_stock = True

    if has_stock:
        profit += prices[-1]

    return profit

'''
In the previous problem, you can only buy once and sell once. That means, to
maximize profit, you need to buy at the global minimum and sell at the global
maximum.

In this problem, you can buy and sell multiple times, so you can buy at local
minima and sell at local maxima. You can either buy and sell each time the line
goes up between two consecutive days or you can buy at the bottom and sell at
the top of a sequence of days with consistently upward growth. Both strategies
yield maximum profit. This is a greedy solution.
'''

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(max_profit(prices))
