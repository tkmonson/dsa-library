# DP state caching: current value and current coin index
# For cache, make a map with string keys (current_val + "_" + coin_index) and integer values (sum (result of recursive call))

def coin_sum(coins, n):
    combos = set()
    def helper(denom_map, current_val):
        if current_val < 0:
            return
        if current_val == 0:
            combos.add(tuple(denom_map.values()))
        for coin in coins:
            denom_map[coin] += 1
            helper(denom_map, current_val - coin)
            denom_map[coin] -= 1
    helper({coin:0 for coin in coins}, n)
    return len(combos)

print(coin_sum([2,3,5,6,], 10))

# Consider a tabulation solution...
