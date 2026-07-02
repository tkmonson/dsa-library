'''
Stone Game II (#1140)

Alice and Bob continue their games with piles of stones. There are a number of
piles arranged in a row, and each pile has a positive integer number of stones
piles[i]. The objective of the game is to end with the most stones.

Alice and Bob take turns, with Alice starting first. On each player's turn,
that player can take all the stones in the first X remaining piles, where
1 <= X <= 2M. Then, we set M = max(M, X). Initially, M = 1. The game continues
until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones
Alice can get.
'''

# Time: O(n^2)
# Auxiliary space: O(n^2)
def stone_game(piles: list[int]) -> int:
    dp = {}
    def dfs(i, m, alice):
        if i == len(piles):
            return 0
        
        if (i, m, alice) in dp:
            return dp[(i, m, alice)]

        curr_sum = 0
        best_curr = 0 if alice else float('inf')
        for x in range(1, 2 * m + 1):
            try:
                curr_sum += piles[i + x - 1]
            except IndexError:
                break
            if alice:
                curr = curr_sum + dfs(i + x, max(x, m), False)
                best_curr = max(best_curr, curr)
            else:
                curr = dfs(i + x, max(x, m), True)
                best_curr = min(best_curr, curr)

        dp[(i, m, alice)] = best_curr
        return best_curr

    return dfs(0, 1, True)

'''
"Play optimally" implies recursion/DP. You need to pass i and M as arguments.
As the recursion progresses, i will increase; piles will be taken turn after
turn until the game is over. Each call is a turn, and the behavior will differ
depending on whose turn it is (need turn argument too). The recursive function
only needs to return Alice's points, but it does need to simulate Bob's turn.

For each call, you need to test all x values (how many piles to take for an
optimal move). On Alice's turn, she is trying to maximize her points on the
current turn plus her points for the rest of the game. Since the function only
returns Alice's points, on Bob's turn, he is trying to choose a pile set such
that he minimizes Alice's points for the rest of the game.
'''

# Time: O(n^3)
# Auxiliary space: O(n^2)
def stone_game_tab(piles: list[int]) -> int:
    n = len(piles)
    # 3D array (alice, i, m); dp[0] is Alice, dp[1] is Bob
    dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(2)]

    for i in range(n - 1, -1, -1):
        for m in range(1, n + 1):
            dp[1][i][m] = float('inf')
            curr_sum = 0
            for x in range(1, 2 * m + 1):
                try:
                    curr_sum += piles[i + x - 1]
                except IndexError:
                    break
                dp[0][i][m] = max(dp[0][i][m], curr_sum + dp[1][i + x][max(x, m)])
                dp[1][i][m] = min(dp[1][i][m], dp[0][i + x][max(x, m)])

    return dp[0][0][1]

'''
Alternative way of implementing the solution with tabulation. Start all the way
at the right (end of the game), consider all m values for that i, and consider
all x values for that m.
'''

if __name__ == '__main__':
    piles = [2,7,9,4,4]
    print(stone_game(piles))
