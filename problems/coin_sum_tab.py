def coin_sum_tab(coins, total):
    T = [0 for i in range(11)]
    T[0] = 1

    for coin in coins:
        for i in range(coin,
