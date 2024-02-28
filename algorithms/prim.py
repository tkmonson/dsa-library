'''
Prim's Algorithm

Given an undirected, connected graph G = (V, E) and a set of edge weights, find
a minimum spanning tree of G.
'''

import heapq
from math import inf

exec(open('_parent_import.py').read())
from structures.priority_queue import PriorityQueue

# Time: O(|E|log|V|)
# Auxiliary space: O(|V|^2) (max amount of heap entries would be
#                            (V - 1) + (V - 2) + ... + 1)
def prim(adj_list, weight):
    cost = {v: inf for v in adj_list}
    prev = {}
    pq = [(0, next(iter(adj_list)))]
    tree = set()  # visited

    while len(tree) < len(adj_list):
        while (u := heapq.heappop(pq)[1]) in tree: pass
        tree.add(u)
        for v in adj_list[u]:
            if v not in tree and (w := weight[(u, v)]) < cost[v]:
                heapq.heappush(pq, (w, v))
                cost[v] = w
                prev[v] = u
        
    return [(prev[v], v) for v in prev]

'''
This solution adds verticies to the heap when they become adjacent to the tree.
When the priority of an adjacent vertex increases, a duplicate entry for that
vertex is added to heap, with higher priority. Thus, the heap may contain stale
duplicates, but these can be discarded when popped by checking if the vertex is
already in the tree.
'''

# Time: O(|E|log|V|)
# Auxiliary space: O(|V|)
def prim2(adj_list, weight):
    prev = {}
    pq = PriorityQueue([[inf, v] for v in adj_list])
    while pq:
        u = pq.pop()
        for v in adj_list[u]:
            if v in pq and (w := weight[(u, v)]) < pq.get_priority(v):
                pq.decrease_key(v, priority=w)
                prev[v] = u

    return [(prev[v], v) for v in prev]

'''
This solution adds all of the verticies to the heap initially. When the
priority of a vertex increases, the heap restructures itself to maintain the
heap invariant. To do this, the heap requires a decrease-key operation. The
heapq module does not provide this operation, so a custom heap implementation
is required.
'''

if __name__ == '__main__':
    adj_list = {
        1: [2, 3, 4, 5],
        2: [1, 5],
        3: [1, 4, 6],
        4: [1, 3, 5, 6, 7],
        5: [1, 2, 4, 7, 9],
        6: [3, 4, 7, 8],
        7: [4, 5, 6, 8, 9],
        8: [6, 7, 9],
        9: [5, 7, 8]
    }
    weight = {
        (1, 2): 10, (1, 3): 9, (1, 4): 6, (1, 5): 12, (2, 5): 8, (3, 4): 7,
        (3, 6): 5,  (4, 5): 8, (4, 6): 8, (4, 7): 7,  (5, 7): 4, (5, 9): 13,
        (6, 7): 14, (6, 8): 6, (7, 8): 8, (7, 9): 8,  (8, 9): 10
    }
    for edge in dict(weight):
        weight[edge[::-1]] = weight[edge]  # the graph is undirected

    print(prim2(adj_list, weight))

