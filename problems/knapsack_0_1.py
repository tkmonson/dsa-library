'''
0-1 Knapsack

Given a set of N items, each with a weight and a value, determine which items
to include in a knapsack such that the total weight is less than or equal to
the knapsack's capacity W and the total value is as large as possible. Return
the total value.

Recurrance relation: K(n, w) = max(val[n - 1] + K(n - 1, w - wt[n - 1]),
                                   K(n - 1, w)
                               )
'''

# Time: O(2^N)
# Auxiliary Space: O(N) (call stack)
def knapsack_naive(wt: list[int], val: list[int], W: int) -> int:
    N = len(wt)
    def knapsack(n, w):
        if n == 0 or w == 0:
            return 0

        if wt[n - 1] > w:
            return knapsack(n - 1, w)
        else:
            return max(
                val[n - 1] + knapsack(n - 1, w - wt[n - 1]),
                knapsack(n - 1, w)
            )

    return knapsack(N, W)

'''
Consider all subsets of items whose total weight is less than or equal to W and
select the maximum value subset.

You can either include an item or not. If the item's weight is greater than
the given capacity, it cannot be included. If you include the item, the total
value increases by the item's value but the capacity of the knapsack decreases
by the item's weight. If you exclude the item, the total value and knapsack
capacity remain unchanged. In either case, the item is removed from the set of
items being considered.

This solution recomputes subproblems, which adds unnecessary complexity.
'''

# Time: O(N * W)
# Auxiliary Space: O(N * W) + O(N) (2D array + call stack)
def knapsack_memo(wt: list[int], val: list[int], W: int) -> int:
    N = len(wt)
    dp = [[-1 for _ in range(W + 1)] for _ in range(N + 1)]

    def knapsack(n, w):
        if n == 0 or w == 0:
            return 0

        if dp[n][w] == -1:
            if wt[n - 1] > w:
                dp[n][w] = knapsack(n - 1, w)
            else:
                dp[n][w] = max(
                    val[n - 1] + knapsack(n - 1, w - wt[n - 1]),
                    knapsack(n - 1, w)
                )

        return dp[n][w]

    return knapsack(N, W)

'''
This is a memoization, or top-down, solution. We create an array with N + 1
rows and W + 1 columns, where each cell holds the computed value of a
subproblem K(n, w), where n is some number of items in [0, N] and w is some
capacity in [0, W]. We start out looking for a solution to the overall problem,
K(N, W), by expressing it in terms of a slightly smaller subproblem, and we
express that subproblem in terms of an even smaller subproblem, and so on,
until we arrive at a base subproblem whose solution is trivial. Results of
previously solved subproblems are stored in the array and used whenever we come
across the same subproblem.
'''

# Time: O(N * W)
# Auxiliary Space: O(N * W) (2D array)
def knapsack_tab_2d(wt: list[int], val: list[int], W: int) -> int:
    N = len(wt)
    dp = [[0 for _ in range(W + 1)] for _ in range(N + 1)]

    for n in range(1, N + 1):
        for w in range(1, W + 1):
            if wt[n - 1] > w:
                dp[n][w] = dp[n - 1][w]
            else:
                dp[n][w] = max(
                    val[n - 1] + dp[n - 1][w - wt[n - 1]],
                    dp[n - 1][w]
                )

    return dp[N][W]

'''
This is a tabulation, or bottom-up, solution. We create an array with N + 1
rows and W + 1 columns, where each cell holds the computed value of a
subproblem K(n, w), where n is some number of items in [0, N] and w is some
capacity in [0, W]. We already know the solution to any subproblem where n = 0
or w = 0 is 0. We then consider subproblems where n = 1, for all w in [1, W],
saving the results in the array. Then we do the same for n = 2, using the
results in the previous row, and so on, until we reach n = N, which will yield
the solution to K(N, W).

Each subproblem in the nth row can be expressed in terms of a subproblem in the
(n - 1)th row. Why is this? Let's assume an item set (A, B) and a capacity w.
If we include B, we "set aside" space for it by reducing the capacity by its
weight. The maximum total value would be val(B) plus the maximum value that can
be contained in a smaller knapsack with capacity w - wt(B), given an item set
of (A). If we exclude B, we don't need to "set aside" space, so the maximum
total value is equal to the maximum value that can be contained in the original
knapsack with capacity w, given an item set of (A).
'''

# Time: O(N * W)
# Auxiliary Space: O(W) (1D array)
def knapsack_tab_1d(wt: list[int], val: list[int], W: int) -> int:
    N = len(wt)
    dp = [0] * (W + 1)

    for n in range(1, N + 1):
        for w in range(W, wt[n - 1] - 1, -1):
            dp[w] = max(val[n - 1] + dp[w - wt[n - 1]], dp[w])

    return dp[W]

'''
This is a tabulation solution that is space-optimized. In the previous
solution, results to all subproblems are stored in a 2D array even though
subproblems in the nth row could be solved using only the results of
subproblems in the (n - 1)th row. In fact, only one row is necessary.

Assume that we have the results of subproblems where n = 1 stored in a single
row. Starting from the right (w = W), we know that K(2, W) will either be
expressed in terms of K(1, W) or K(1, w) where w < W. As we overwrite the row
with n = 2 results from right to left, we will still have access to the
required n = 1 results.
'''

if __name__ == '__main__':
    wt = [95, 4, 60, 32, 23, 72, 80, 62, 65, 46]
    val = [55, 10, 47, 5, 4, 50, 8, 61, 85, 87]
    W = 269
    print(knapsack_tab_1d(wt, val, W))

