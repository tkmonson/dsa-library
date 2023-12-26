'''
Last Stone Weight (#1046)

You are given an array of integers `stones` where `stones[i]` is the weight of
the ith stone. We are playing a game with the stones. On each turn, we choose
the heaviest two stones and smash them together. Suppose the heaviest two
stones have weights `x` and `y` where `x <= y`. If `x == y`, both stones are
destroyed. Otherwise, the stone of weight `x` is destroyed and the stone of
weight `y` has a new weight `y - x`. At the end of the game, there is at most
one stone left. Return the weight of the last remaining stone or 0 if no stones
are left.
'''

import heapq

# Time: O(nlogn)
# Auxiliary space: O(1)
def last_stone_weight(stones: list[int]) -> int:
    for i in range(len(stones)):
        stones[i] = -stones[i]
    heapq.heapify(stones)
    while True:
        try:
            y = heapq.heappop(stones)
        except IndexError:
            return 0
        try:
            x = heapq.heappop(stones)
        except IndexError:
            return -y
        heapq.heappush(stones, y - x)

'''
Two heaviest stones => we need to know the maximum element in the collection
                    => max-heap
'''

# Time: O(n^2)
# Auxiliary space: O(1)
def last_stone_weight2(stones: list[int]) -> int:
    f = lambda s: s.pop(s.index(max(s)))
    while len(stones) > 1:
        stones.append(f(stones) - f(stones))
    return stones[0]


if __name__ == '__main__':
    stones = [2, 7, 4, 1, 8, 1]
    print(last_stone_weight(stones))

'''
Apparently bucket sort is also a possible solution to this problem?
'''

