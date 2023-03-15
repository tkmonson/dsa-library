'''
Best Time to Buy and Sell Stock (#121)

Given an array `prices` where `prices[i]` is the price of a given stock on the
`ith` day, return the maximum profit that can be made by buying a stock on one
day and selling it on a different day in the future.
'''

def max_profit(prices: list[int]) -> int:
    ans = 0
    max_price = 0
    for i in reversed(range(len(prices))):
        max_price = max(max_price, prices[i])
        ans = max(ans, max_price - prices[i])
    return ans


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(max_profit(prices))

