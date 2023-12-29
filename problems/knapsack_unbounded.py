'''
Unbounded Knapsack

Given a set of N kinds of items, each with a weight and a value and an infinite
number of copies, determine which items to include in a knapsack such that the
total weight is less than or equal to the knapsack's capacity W and the total
value is as large as possible. Return the total value.

Recurrance relation: K(n, w) = max(val[n - 1] + K(n, w - wt[n - 1]),
                                   K(n - 1, w)
                               )
'''

def unbounded_knapsack_naive(wt: list[int], val: list[int], W: int) -> int:
    N = len(wt)
    def knapsack(n, w):
        if n == 0 or w == 0:
            return 0

        if (wt[n - 1] > w):
            return knapsack(n - 1, w)
        else:
            return max(
                val[n - 1] + knapsack(n, w - wt[n - 1]),
                knapsack(n - 1, w)
            )

    return knapsack(N, W)


def unbounded_knapsack_memo(wt: list[int], val: list[int], W: int) -> int:
    N = len(wt)
    dp = [[-1 for _ in range(W + 1)] for _ in range(N + 1)]

    def knapsack(n, w):
        if n == 0 or w == 0:
            return 0

        if dp[n][w] == -1:
            if (wt[n - 1] > w):
                dp[n][w] = knapsack(n - 1, w)
            else:
                dp[n][w] = max(
                    val[n - 1] + knapsack(n, w - wt[n - 1]),
                    knapsack(n - 1, w)
                )

        return dp[n][w]

    return knapsack(N, W)


def unbounded_knapsack_tab_2d(wt: list[int], val: list[int], W: int) -> int:
    N = len(wt)
    dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]

    for n in range(1, N + 1):
        for w in range(1, W + 1):
            if wt[n - 1] > w:
                dp[n][w] = dp[n - 1][w]
            else:
                dp[n][w] = max(
                    val[n - 1] + dp[n][w - wt[n - 1]],
                    dp[n - 1][w]
                )

    return dp[N][W]

'''
These three solutions are very similar to the corresponding 0-1 solutions; in
fact, there is only one change. In a 0-1 solution, the "take" value is
val[n - 1] + K(n - 1, w - wt[n - 1]); the first argument of K expresses that
because you have taken the nth item, there are only n - 1 items left to
consider. In an unbounded solution, the "take" value is
val[n - 1] + K(n, w - wt[n - 1]); the first argument of K expresses that even
though you have taken an instance of the nth item, you can continue to take
additional instances of the nth item. The set of items under consideration only
shrinks when you decide not to take an item (K(n - 1, w)).
'''

def unbounded_knapsack_tab_1d(wt: list[int], val: list[int], W: int) -> int:
    N = len(wt)
    dp = [0] * (W + 1)
 
    for n in range(1, N + 1):
        for w in range(wt[n - 1], W + 1):
            dp[w] = max(val[n - 1] + dp[w - wt[n - 1]], dp[w])
 
    return dp[W]

'''
This solution is very similar to the corresponding 0-1 solution; in fact, there
is only one change. In the 0-1 solution, the row is traversed right-to-left so
that subproblems K(n, w) can be expressed in terms of subproblems
K(n - 1, w - wt), the values stored to the left of the current pointer. In the
unbounded solution, the row is traversed left-to-right so that subproblems
K(n, w) can be expressed in terms of subproblems K(n, w - wt), the values
stored to the left of the current pointer. These K expressions having the same
first argument implies that the nth item can be added to the knapsack multiple
times as w increases.
'''

if __name__ == '__main__':
    wt = [4, 2, 1, 10, 2]
    val = [12, 2, 1, 4, 1]
    W = 15
    print(unbounded_knapsack_tab_1d(wt, val, W))

