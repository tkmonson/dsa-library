'''
Kruskal's Algorithm

Given an undirected, connected graph G = (V, E) and a set of edge weights, find
a minimum spanning tree of G.
'''

exec(open('_parent_import.py').read())
from structures.disjoint_set import DisjointSet

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

