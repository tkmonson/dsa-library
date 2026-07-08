'''
Graph Valid Tree (#261)


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

    return len(visited) == n

if __name__ == '__main__':
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    print(valid_tree(n, edges))
