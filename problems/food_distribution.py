'''
Food Distribution (Coderbyte)

You are given an array, the first element of which is the number of sandwiches
you have and the rest which represent the hunger levels of an arbitrary number
of people (0-5, where 0 is not hungry and 5 is very hungry). Giving a sandwich
to a person will decrease their hunger by 1. Distribute sandwiches in such a
way that you minimize the hunger differences between adjacent people. Return
the sum of these minimized differences.

E.g. [4, 5, 2, 3, 1, 0] => minimized hunger array is [2, 2, 2, 1, 0] with
     difference sum of 2.

NOT 100% CERTAIN THIS SOLUTION IS CORRECT
'''

from collections import deque

def food_distribution(arr):
    N, h = arr[0], arr[1:]
    score = sum(abs(h[i] - h[i + 1]) for i in range(len(h) - 1))

    local_maxes = deque()
    for i in range(1, len(h) - 1):
        if h[i - 1] < h[i] > h[i + 1]:
            local_maxes.append(i)

    while local_maxes and N > 0:
        i = local_maxes.popleft()
        while h[i - 1] < h[i] > h[i + 1] and N > 0:
            score -= 2
            h[i] -= 1
            N -= 1

    while h[0] > h[1] and N > 0:
        score -= 1
        h[0] -= 1
        N -= 1

    while h[-1] > h[-2] and N > 0:
        score -= 1
        h[-1] -= 1
        N -= 1

    return score

if __name__ == '__main__':
    arr = [4, 5, 2, 3, 1, 0]
    print(food_distribution(arr))

'''
The insight here is that you want to give sandwiches to local maximums and
giving a sandwich to a local maximum in the middle will reduce the difference
sum by 2, whereas giving one to a local maximum on either end of the array will
only reduce the sum by 1.

* Traverse hunger array, collect all local maxes in the middle.
* Give sandwiches to each until they are no longer local maxes. Reduce sum by 2
  for each sandwich given. Continue until you run out of sandwiches or maxes.
* Do the same for local maxes on either end, if you have sandwiches left.
'''
