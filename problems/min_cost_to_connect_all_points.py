'''
Min Cost to Connect All Points (#1584)

You are given an array `p` of the integer coordinates of some points in a
2D-plane, where `points[i] = [x_i, y_]`.

The cost of connecting two points `[x_i, y_i]` and `[x_j, y_j]` is the
Manhattan distance between them: `|x_i - x_j| + |y_i + y_j|`.

Return the minimum cost to make all points connected. All points are connected
if there is exactly one simple path between any two points.
'''

import heapq

class DisjointSet:
    def __init__(self, n):
        self.parent = [-1] * n

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        elif self.parent[rx] < self.parent[ry]:
            self.parent[rx] += self.parent[ry]
            self.parent[ry] = rx
        else:
            self.parent[ry] += self.parent[rx]
            self.parent[rx] = ry
        return True

    def find(self, x):
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


# Time: O(|E|log|V|)
# Auxiliary space: O(|V|)
def min_cost_connect_points_kruskal(p: list[list[int]]) -> int:
    manhattan = lambda u, v: abs(u[0] - v[0]) + abs(u[1] - v[1])
    n = len(p)
    uf = DisjointSet(n)

    edges = []
    for i in range(n):
        for j in range(i, n):
            edges.append((i, j, manhattan(p[i], p[j])))
    edges.sort(key=lambda e: e[2])

    min_cost = 0
    for i, j, w in edges:
        if uf.union(i, j):
            min_cost += w

    return min_cost


# Time: O(|E|log|V|)
# Auxiliary space: O(|E|^2) (max amount of stale duplicates would be
#                            (E - 1) + (E - 2) + ... + 1)
def min_cost_connect_points_prim(p: list[list[int]]) -> int:
    manhattan = lambda u, v: abs(u[0] - v[0]) + abs(u[1] - v[1])
    n = len(p)
    tree = set()
    pq = [(0, 0)]  # (weight, index of p)

    min_cost = 0
    while len(tree) < n:
        w, i = heapq.heappop(pq)
        if i in tree:
            continue
        min_cost += w
        tree.add(i)
        for j in range(n):
            if j not in tree:
                heapq.heappush(pq, (manhattan(p[i], p[j]), j))

    return min_cost

'''
This application of Prim's algorithm does not use a cost array. A cost array
would be required if we needed to return the actual MST, but because we only
need to return its weight, it's not stricly necessary. However, this also means
that the heap will contain the maximum amount of stale duplicate entries at
some point (worst-case space complexity every time).
'''

if __name__ == '__main__':
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    print(min_cost_connect_points2(points))

'''
This problem is asking for the total cost of a minimum spanning tree of the
complete graph of the given points (every pair of points is connected by a
unique edge). Thus, Kruskal's algorithm and Prim's algorithm are appropriate
solutions. See the write-ups on those algorithms for more in-depth notes.
'''

