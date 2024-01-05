'''
Best Time to Buy and Sell Stock with Cooldown (#309)

You are given an array `prices` where `prices[i]` is the price of a given stock
on the ith day. On each day, you can buy a share if you do not have one, sell a
share if you do, or do nothing (cooldown). After you sell a share, you must
cooldown for one day before buying again. Find the maximum profit that you can
achieve.
'''

def max_profit(prices: list[int]) -> int:
    dp = {}

    def dfs(curr, i, have_share, cooldown):
        if i == len(prices):
            return curr

        if (i, have_share) in dp:
            left, right = dp[i, have_share]
            return curr + (right if cooldown else max(left, right))

        if have_share:
            left = dfs(curr + prices[i], i + 1, False, True)  # sell
        else:
            left = dfs(curr - prices[i], i + 1, True, False)  # buy
        right = dfs(curr, i + 1, have_share, False)  # do nothing

        dp[i, have_share] = [left - curr, right - curr]
        return right if cooldown else max(left, right)

    return dfs(0, 0, False, False)
    

if __name__ == '__main__':
    prices = [1, 2, 3, 0, 2]
    print(max_profit(prices))

'''
This is a problem about making decisions. For each day, you can either buy (if
you do not hold a share and did not sell the previous day), sell (if you do
hold a share), or cooldown (do nothing). In other words:

    If you sold the previous day:
        you must cooldown
    Else:
        you can buy/sell (depending on your share state) or cooldown

Thus, we can draw a binary decision tree. Let each left branch represent a
buy/sell and each right branch represent a cooldown.

For prices = [1, 2, 3, 0, 2]:

                  0
           B ____/ \____
           -1           0
       S __/ \__   B __/ \__
        1      -1  -2       0
         \_    ... ...   ... \_
           1                   0    <--
      B __/ \__           B __/ \__
       1       1           0       0
    S / \   B / \       S / \   B / \
     3   1  -1   1       2   0  -2   0

Each leaf node is a profit that can be made, and we want to return the greatest
one. Tracing every path to visit every leaf node would be O(2^n), but we can
lower this complexity with caching.

Note the subtrees at level 3 (<--). While the node values differ, the structure
and the change between the nodes is identical. This is because, regardless of
current profit, if you arrive at the same day twice with the same share state,
the decision paths before you will be the same (ignoring the cooldown
requirement for the moment). Thus, we can cache [lp, rp], the max profits that
can be earned from the left and right paths respectively, when starting from
state (i, s), where i is the day and s is a boolean that represents share
state. This complexity would be O(n * 2) = O(n).

Note that you could arrive at day i without a share, but in one case you would
have to cooldown because you sold on the previous day and in another case you
would be ready to buy because you have already cooled down. When accessing
cached values, we can return max(lp, rp) or rp based on whether a cooldown is
required.
'''

