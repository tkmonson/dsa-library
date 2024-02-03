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

exec(open('_parent_import.py').read())
from structures.priority_queue import PriorityQueue

def dijkstra(graph, edge_length, source):
    pq = PriorityQueue()
    distance = {source: 0}
    predecessor = {}
    for key in graph.keys():
        if key != source:
            distance[key] = float('inf')
            predecessor[key] = None
        pq.insert(key, distance[key])

    while not pq.is_empty():
        u = pq.pull()[1]
        for v in graph[u]:
            alt = distance[u] + edge_length[(u, v)]
            if alt < distance[v]:
                pq.prioritize((distance[v], v), (alt, v))
                distance[v] = alt
                predecessor[v] = u

    return distance, predecessor

if __name__ == '__main__':
  graph = {
    'a': ['b', 'c', 'e'],
    'b': ['a', 'c', 'd'],
    'c': ['a', 'b', 'd', 'e'],
    'd': ['b', 'c', 'e', 'f', 'g'],
    'e': ['a', 'c', 'd', 'g'],
    'f': ['d', 'g'],
    'g': ['d', 'e', 'f'],
  }
  edge_length = {
    ('a', 'b'): 4,
    ('a', 'c'): 3,
    ('a', 'e'): 7,
    ('b', 'a'): 4,
    ('b', 'c'): 6,
    ('b', 'd'): 5,
    ('c', 'a'): 3,
    ('c', 'b'): 6,
    ('c', 'd'): 11,
    ('c', 'e'): 8,
    ('d', 'b'): 5,
    ('d', 'c'): 11,
    ('d', 'e'): 2,
    ('d', 'f'): 2,
    ('d', 'g'): 10,
    ('e', 'a'): 7,
    ('e', 'c'): 8,
    ('e', 'd'): 2,
    ('e', 'g'): 5,
    ('f', 'd'): 2,
    ('f', 'g'): 3,
    ('g', 'd'): 10,
    ('g', 'e'): 5,
    ('g', 'f'): 3,
  }
  source = 'a'
  distance, predecessor = dijkstra(graph, edge_length, source)
  print(f'DIST: {distance}')
  print(f'PREV: {predecessor}')

