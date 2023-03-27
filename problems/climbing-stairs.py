'''
Climbing Stairs (#70)

It takes n steps to reach the top of a staircase. You can climb either 1 or 2
steps each time. How many distinct ways are there to climb to the top?
'''

from functools import lru_cache

def climb_stairs_iterative(n: int) -> int:
    if n == 1 or n == 2: return n

    a, b = 1, 2
    for _ in range(2, n):
        c = a + b
        a = b
        b = c
    return c


def climb_stairs_recursive(n: int) -> int:
    dp = [1, 1, 2]
    def f(n):
        if n < len(dp):
            return dp[n]
        dp.append(f(n - 1) + f(n - 2))
        return dp[n]
    return f(n)


@lru_cache
def climb_stairs_recursive2(n: int) -> int:
    if n == 1 or n == 2: return n
    return climb_stairs_recursive2(n - 1) + climb_stairs_recursive2(n - 2)


if __name__ == '__main__':
    n = 66
    print(climb_stairs_iterative(n))
    print(climb_stairs_recursive(n))
    print(climb_stairs_recursive2(n))

