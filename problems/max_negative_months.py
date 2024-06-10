import heapq
from random import randint

'''
Get Max Negative Months (Amazon OA2, 06/24)

You a given an array of integers `PnL`, where `PnL[i]` represents an amount of
money that you will either gain or lose. Each value in `PnL` is positive, and
you can multiply values by -1 an arbitrary number of times.

Find the maximum number of months where you can afford to take a loss such that
your "cumulative PnL" is strictly positive for each month.

E.g. the cumulative PnL for [3, -2, 5, -6, 1] is [3, 1, 6, 0, 1].

THIS SOLUTION IS UNTESTED, MAY NOT BE PERFECTLY CORRECT.
'''

# Time: O(nlogn)
# Auxiliary space: O(n)
def get_max_negative_months(PnL):
    s = 0
    pq = []

    for curr in PnL:
        if curr < s:
            s -= curr
            heapq.heappush(pq, -curr)
        else:
            if not pq or -pq[0] <= curr:
                s += curr
            else:
                s -= 2 * heapq.heappop(pq)
                s -= curr
                heapq.heappush(pq, -curr)

    return len(pq)


if __name__ == '__main__':
    PnL = [randint(0, 100) for _ in range(100)]
    print(PnL)
    print(get_max_negative_months(PnL))

'''
The naive approach is backtracking. However, this problem has optimal
substructure. That is:

    f(a[:i]) = f(a[:i - 1]) + (0 or 1) (depending on whether a[i - 1] can be
    made negative without making the cumulative sum negative)

Additionally, this problem does not have overlapping subproblems. Thus, a
greedy approach is best.

While traversing left-to-right, if you can make a month negative, do so. If you
cannot, then you can consider a swap: make a previous loss a gain and make the
current month a loss. If this can be done while also increasing the cumulative
sum, then it is worth doing. Otherwise, just take the current month as a gain.

An optimal swap would be made with the greatest previous loss. To have direct
access to the greatest previous loss, store losses in a heap.
'''

