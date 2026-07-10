'''
Graph Valid Tree (#261)

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge
is a pair of nodes), write a function to check whether these edges make up a
valid tree.
'''

from collections import deque

def valid_tree(n: int, edges: list[list[int]]) -> bool:
    visited = set()
    adj = {i: [] for i in range(n)}
    for e in edges:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])

    q = deque([(0, None)])
    while q:
        v, pv = q.popleft()
        if v in visited:
            return False  # cycle detected
        visited.add(v)
        for nb in adj[v]:
            if nb != pv:
                q.append((nb, v))

    return len(visited) == n  # checks if graph is connected

'''
A graph is a tree if it is acyclic and connected. Do a DFS or BFS with a
visited set to determine if the graph is acyclic (do not traverse back to the
vertex you just came from, that does not count as a cycle). If the search ends
with every vertex visited, the graph is connected.
'''

if __name__ == '__main__':
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    print(valid_tree(n, edges))

'''
You could also solve this problem with a union-find forest.
'''
