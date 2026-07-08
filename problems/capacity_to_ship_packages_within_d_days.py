'''
Capacity To Ship Packages Within D Days (#1011)

A conveyor belt has packages that must be shipped from one port to another
within `days` days. The `ith` package on the conveyor belt has a weight of
`weights[i]`. Each day, we load the ship with packages on the conveyor belt (in
the order given by `weights`). We may not load more weight than the maximum
weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the
packages on the conveyor belt being shipped within `days` days.
'''

# Time: nlog(m) (where m is the sum of weights)
# Auxiliary space: O(1)
def ship_within_days(weights: list[int], days: int) -> int:
    left = max(weights)
    right = sum(weights)
    result = right

    def can_ship(cap):
        ships = 1
        curr_cap = cap
        for w in weights:
            if curr_cap - w < 0:
                ships += 1
                curr_cap = cap
            curr_cap -= w
        return ships <= days

    while left <= right:
        cap = (left + right) // 2
        if can_ship(cap):
            result = cap
            right = cap - 1
        else:
            left = cap + 1
    return result

'''
The ship has to have a capacity of at least max(weights). And the largest
capacity the ship would possibly need is sum(weights). This means that the
optimal capacity exists somewhere in the search space between the two.

Do a binary search of the capacity search space. If a capacity can ship the
items in d days, search the left half. If it cannot, search the right half.
When determining whether a capacity can ship the items, add items to a ship
until you cannot fit the next item; then move on to the next ship.
'''

# Correct, but time limit exceeded
def ship_within_days2(weights: list[int], days: int) -> int:
    dp = {}
    def dfs(i, d):
        if (i, d) in dp:
            return dp[(i, d)]

        if d == 1:
            w = 0
            for j in range(i, len(weights)):
                w += weights[j]
            dp[(i, d)] = w
            return w
        
        curr_load = 0
        max_load = 0
        min_ship = float('inf')

        for j in range(i, len(weights) - d + 1):
            curr_load += weights[j]
            if curr_load >= min_ship:
                break
            max_load = max(curr_load, dfs(j + 1, d - 1))
            min_ship = min(min_ship, max_load)

        dp[(i, d)] = min_ship
        return min_ship

    return dfs(0, days)

'''
My original idea was that you might want to intentionally reserve an item that
would fit on the current ship in order to make other items fit better in the
future. Thus, you would need to evaluate different configurations using DP. But
this is not true. If an item can fit on the ship, you should load it. If A
barely fits on ship 1, and B and C fit on ship 2 but D cannot fit with them, D
is not going to be able to fit on ship 2 because you decide to reserve A and
load it on ship 2 instead.

If you were not restricted to loading items in the order given, then you would
want to consider different configurations using DP to load the items as
space-efficiently as possible.

This solution works, but it considers a bunch of non-optimal loading
configurations where space is left on ships for no reason.
'''

if __name__ == '__main__':
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    days = 5
    print(ship_within_days(weights, days))
