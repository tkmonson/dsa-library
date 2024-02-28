'''
Dijkstra's Algorithm (Shortest Path Algorithm)

Given a graph G = (V, E), directed or undirected, a set of positive edge
lengths {l_e : e in E}, and a source vertex s in V, find the shortest distance
between s and u and the predecessor of u on this shortest path, for all u in V
that are reachable from s.

In this implementation, the graph is represented by an adjacency list.

Time complexity: O((|V|+|E|) * log(|V|))
Space complexity: O(|V|) (using a binary heap)
'''

import heapq
from math import inf

exec(open('_parent_import.py').read())
from structures.priority_queue import PriorityQueue

# Time: O(|E|log|V|)
# Auxiliary space: O(|V|^2) (max amount of heap entries would be
#                            (V - 1) + (V - 2) + ... + 1)
def dijkstra(adj_list, weight, source):
    distance = {v: inf for v in adj_list}; distance[source] = 0
    predecessor = {}
    pq = [(0, source)]
    visited = set()

    while len(visited) < len(adj_list):
        try:
            while (u := heapq.heappop(pq)[1]) in visited: pass
        except IndexError:
            break  # graph is not strongly connected
        visited.add(u)
        for v in adj_list[u]:
            alt = distance[u] + weight[(u, v)]
            if v not in visited and alt < distance[v]:
                heapq.heappush(pq, (alt, v))
                distance[v] = alt
                predecessor[v] = u

    return distance, predecessor

'''
This solution adds unvisited verticies to the heap when they become adjacent to
the vertex currently being visited. When the priority of a vertex in the heap
increases, a duplicate entry for that vertex is added to heap, with higher
priority. Thus, the heap may contain stale duplicates, but these can be
discarded when popped by checking if the vertex has already been visited.
'''

# Time: O(|E|log|V|)
# Auxiliary space: O(|V|)
def dijkstra2(adj_list, weight, source):
    distance = {source: 0}
    predecessor = {}
    pq = PriorityQueue()
    for v in adj_list:
        if v != source:
            distance[v] = inf
            predecessor[v] = None
        pq.insert(v, priority=distance[v])

    while pq:
        u = pq.pop()
        for v in adj_list[u]:
            alt = distance[u] + weight[(u, v)]
            if v in pq and alt < distance[v]:
                pq.decrease_key(v, priority=alt)
                distance[v] = alt
                predecessor[v] = u

    return distance, predecessor

'''
This solution adds all of the verticies to the heap initially. When the
priority of a vertex increases, the heap restructures itself to maintain the
heap invariant. To do this, the heap requires a decrease-key operation. The
heapq module does not provide this operation, so a custom heap implementation
is required.
'''

if __name__ == '__main__':
  adj_list = {
    'a': ['b', 'c', 'e'],
    'b': ['a', 'c', 'd'],
    'c': ['a', 'b', 'd', 'e'],
    'd': ['b', 'c', 'e', 'f', 'g'],
    'e': ['a', 'c', 'd', 'g'],
    'f': ['d', 'g'],
    'g': ['d', 'e', 'f'],
  }
  weight = {
    ('a', 'b'): 4,  ('b', 'a'): 4,
    ('a', 'c'): 3,  ('c', 'a'): 3,
    ('a', 'e'): 7,  ('e', 'a'): 7,
    ('b', 'c'): 6,  ('c', 'b'): 6,
    ('b', 'd'): 5,  ('d', 'b'): 5,
    ('c', 'd'): 11, ('d', 'c'): 11,
    ('c', 'e'): 8,  ('e', 'c'): 8,
    ('d', 'e'): 2,  ('e', 'd'): 2,
    ('d', 'f'): 2,  ('f', 'd'): 2,
    ('d', 'g'): 10, ('g', 'd'): 10,
    ('e', 'g'): 5,  ('g', 'e'): 5,
    ('f', 'g'): 3,  ('g', 'f'): 3,
  }
  source = 'a'
  distance, predecessor = dijkstra(adj_list, weight, source)
  print(f'DIST: {distance}')
  print(f'PRED: {predecessor}')

