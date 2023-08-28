'''
K Closest Points to Origin (#973)

Given an array of `points` where `points[i] = [x_i, y_i]` represents a point on
the x-y plane and an integer `k`, return the `k` closest points to the origin
in any order. The distance between two points on the x-y plane is the Euclidean
distance: `sqrt((x_1 - x_2)^2 + (y_1 - y_2)^2)`.
'''

import heapq

def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    return sorted(points, key=lambda x: x[0]*x[0] + x[1]*x[1])[:k]

def k_closest_heap(points: list[list[int]], k: int) -> list[list[int]]:
    values = [p[0]*p[0] + p[1]*p[1] for p in points]
    return [t[1] for t in heapq.nsmallest(k, zip(values, points))]

if __name__ == '__main__':
    points = [[3,3],[5,-1],[-2,4]]
    k = 2
    print(k_closest_heap(points, k))

'''
This problem is about sorting. This is done above using a built-in sort method
and a heap, both of which have time complexities of O(nlogn). This could also
be done by writing a quickselect algorithm from scratch, which would have a
time complexity of O(n).
'''

