from priority_queue import PriorityQueue

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
inf = float('inf')
pq = PriorityQueue(
    [(0, 'a'),
     (inf, 'b'),
     (inf, 'c'),
     (inf, 'd'),
     (inf, 'e'),
     (inf, 'f'),
     (inf, 'g')]
)
print(pq)

u = pq.pull()[1]
print(graph[u])

