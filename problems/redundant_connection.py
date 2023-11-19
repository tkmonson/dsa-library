'''
Redundant Connection (#684)

Consider a connected, acyclic, undirected graph (a tree) with vertices labeled
`1` to `n`. Now, add an edge to this graph that connects two different vertices
in the graph and that does not already exist in the graph. Given this updated
graph, represented as list of `n` edges, return the last edge in the list that
would make the graph acyclic if removed.
'''

from collections import defaultdict

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


def find_redundant_connection(edges: list[list[int]]) -> list[int]:
    uf = DisjointSet(len(edges) + 1)
    for u, v in edges:
        if not uf.union(u, v):
            return [u, v]

'''
The disjoint-set data structure can detect cycles in an undirected graph. Add
edges between vertices by performing union operations. If adding an edge would
create a cycle, the union operation will not change the structure (and will
return False). Such an edge would be the last edge in the cycle not already
added; if adding edges from left to right, such an edge would be the last edge
in the input that is a member of the cycle.
'''

def find_redundant_connection2(edges: list[list[int]]) -> list[int]:
    parent = [0] * (len(edges) + 1)
    def find(x):
        while parent[x]:
            x = parent[x]
        return x
    for x, y in edges:
        rx, ry = find(x), find(y)
        if rx == ry:
            return [x, y]
        parent[rx] = ry

'''
Another more concise union-find solution. Likely slower because it does not
utilize weighted union or collapsed find.
'''

def find_redundant_connection3(edges: list[list[int]]) -> list[int]:
    adj_list = defaultdict(lambda: [])
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    dfs_tree = []
    seen = {}
    def dfs(prev, curr):
        dfs_tree.append(curr)
        seen[curr] = len(dfs_tree) - 1

        for n in adj_list[curr]:
            if n in seen:
                if n != prev:
                    # Extract cycle from DFS tree
                    for i in range(seen[n]):
                        del seen[dfs_tree[i]]
                    return True
            else:
                if dfs(curr, n):
                    return True

        dfs_tree.pop()
        del seen[curr]

    dfs(0, 1)
    cycle = seen
    for i in range(len(edges) - 1, -1, -1):
        if edges[i][0] in cycle and edges[i][1] in cycle:
            return edges[i]

'''
A slower solution that does not use a disjoint set. Create an adjacency list,
use it to DFS the graph. Keep track of the DFS tree in an array and store a
mapping of elements in the DFS tree to their indicies in the tree. If you come
across a vertex v that exists in the DFS tree and is not the vertex you last
visited, then you have just completed a cycle. Delete all keys in the mapping
that were visited before v. The mapping now contains only the vertices
contained in the cycle. Traverse the given edge list backward. Return the first
edge whose members both exist in the mapping.
'''

if __name__ == '__main__':
    edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    print(find_redundant_connection(edges))

