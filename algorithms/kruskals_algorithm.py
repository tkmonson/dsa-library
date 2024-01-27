'''
Kruskal's Algorithm

Given an undirected, connected graph G = (V, E) and a set of edge weights, find
a minimum spanning tree of G.
'''

# Time: O(|E|log|V|)
# Auxiliary space: O(|V|)
def kruskal(edges, weight):
    verticies = set()
    for u, v in edges:
        verticies.add(u)
        verticies.add(v)
    verticies = list(verticies)
    n = len(verticies)

    vertex_to_index = {}
    for i in range(n):
        vertex_to_index[verticies[i]] = i

    uf = DisjointSet(n)
    edges.sort(key=weight)

    mst = []
    for u, v in edges:
        i, j = vertex_to_index[u], vertex_to_index[v]
        if uf.union(i, j):
            mst.append((u, v))

    return mst


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

