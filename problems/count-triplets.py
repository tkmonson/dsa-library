# Given an unsorted array of integers d and a threshold t, return the number of
#     triplets (d[i], d[j], d[k]) such that:
#         * d[i] < d[j] < d[k] and
#         * d[i] + d[j] + d[k] <= t.
# Two solutions are given below, one O(n^3), the other O(n^2).

import random

def trip_n3(d, t):
    d.sort()
    n = len(d)
    count = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if d[i] + d[j] + d[k] <= t:
                    count += 1
    return count

def trip_n2(d, t):
    d.sort()
    n = len(d)
    count = 0
    for i in range(n - 2):
        j = i + 1
        k = n - 1
        while(j < k):
            if d[i] + d[j] + d[k] > t:
                k -= 1
            else:
                count += (k - j)
                j += 1
    return count

def count_triplets(d, t, f=trip_n2):
    return f(d, t)

if __name__ == "__main__":
    d = []
    t = 77
    for _ in range(20):
        d.append(random.randint(0,100))
    print(f"d = {d}, t = {t}")
    print(f"count_triplets(d, t) => {count_triplets(d, t)}")

