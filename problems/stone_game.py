'''
Stone Game (#877)

Alice and Bob play a game with piles of stones. There are an even number of
piles arranged in a row, and each pile has a positive integer number of stones
piles[i]. The objective of the game is to end with the most stones. The total
number of stones across all the piles is odd, so there are no ties. Alice and
Bob take turns, with Alice starting first. Each turn, a player takes the entire
pile of stones either from the beginning or from the end of the row. This
continues until there are no more piles left, at which point the person with
the most stones wins.

Assuming Alice and Bob play optimally, return true if Alice wins the game, or
false if Bob wins.
'''

# Time: O(1)
# Auxiliary space: O(1)
def stone_game(piles: list[int]) -> bool:
    return True

'''
With 2 piles, Alice can always choose the larger pile. With 4 piles, Alice can
always choose piles 1 and 3 or piles 2 and 4. One of these must have the
majority of the stones because there is an odd number of stones in total. With
N piles, Alice can always choose all of the odd-indexed piles or all of the
even-indexed piles. One must have the majority. Alice always wins (when playing
optimally).
'''

# Time: O(n^2)
# Auxiliary space: O(n^2) (call stack)
def stone_game2(piles: list[int]) -> bool:
    dp = {}
    def max_alice_score(i, j):
        if (i, j) in dp:
            return dp[(i, j)]

        if j - i == 1:
            dp[(i, j)] = max(piles[i], piles[j])
            return dp[(i, j)]

        dp[(i, j)] = max(
            piles[i] + max_alice_score(i + 2, j),
            piles[i] + max_alice_score(i + 1, j - 1),
            piles[j] + max_alice_score(i + 1, j - 1),
            piles[j] + max_alice_score(i, j - 2),
        )

        return dp[(i, j)]

    return max_alice_score(0, len(piles) - 1) > sum(piles) / 2

'''
"Play optimally" implies that players make moves as if they can see into the
future to the end of the game. This suggests recursion / DP.

If Alice has the majority of the stones at the end of the game, she wins. We
can calculate the max score she can get, given some set of piles p(i, j)
(inclusive). It will be derived from subproblems p(i + 2, j), p(i + 1, j - 1),
and p(i, j - 2), the possible states on her second turn.
'''

if __name__ == '__main__':
    piles = [5,3,4,5]
    print(stone_game(piles))
