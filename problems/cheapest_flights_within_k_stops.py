'''
Cheapest Flights Within K Stops (#787)

There are `n` cities connected by some number of flights. You are given an
array `flights` where `flights[i] = [from_i, to_i, price_i]` indicates that
there is a flight from city `from_i` to city `to_i` with cost `price_i`.

You are also given three integers `src`, `dst`, and `k`, return the cheapest
price from `src` to `dst` with at most `k` stops. If there is no such route,
return -1.
'''

from collections import deque
from math import inf

# Time: O(k|E|)
# Auxiliary space: O(n)
def find_cheapest_price_bellman_ford(n: int, flights: list[list[int]],
                                     src: int, dst: int, k: int) -> int:
    dist = [inf] * n; dist[src] = 0
    for _ in range(k + 1):
        temp = dist.copy()
        for u, v, p in flights:
            if (alt := dist[u] + p) < temp[v]:
                temp[v] = alt
        dist = temp

    return -1 if dist[dst] == inf else dist[dst]

'''
Let s be the source vertex.
Let V' be the set of all verticies in a graph except s.

The Bellman-Ford algorithm is especially well-suited to solving this problem.
Generally, single-source shortest path problems are solved by initially
approximating the shortest distances between s and each v in V' to be infinite
and then gradually "relaxing" the graph's edges to better approximate these
distances until the correct (minimum) distance is found. Bellman-Ford does this
by relaxing every edge in the graph, and it does this |V| - 1 times because the
longest possible path contains |V - 1| edges.

More generally, after Bellman-Ford relaxes all edges x times, all paths with x
or fewer edges will have been explored and the shortest distances between s and
each v in V' along these paths will have been found. When x = |V| - 1, all
possible paths are explored.

In this problem, we are looking for the shortest distance between a source and
a destination, with the constraint that we can only travel along paths with at
most k intermediate vertices (or, in order words, with at most k + 1 edges).
Run the relaxation loop k + 1 times, look up the shortest distance to the
destination.
'''

# Time: O(|E| + |V|^k) ?
# Auxiliary space: O(n)
def find_cheapest_price_dijkstra(n: int, flights: list[list[int]],
                                 src: int, dst: int, k: int) -> int:
    adj = [[] for _ in range(n)]
    for u, v, p in flights:
        adj[u].append((v, p))
    dist = [inf] * n; dist[src] = 0
    q = deque([(-1, 0, src)])

    while q:
        stops, d, u = q.popleft()
        if stops < k:
            for v, p in adj[u]:
                alt = d + p
                if alt < dist[v]:
                    dist[v] = alt
                    q.append((stops + 1, alt, v))

    return -1 if dist[dst] == inf else dist[dst]

'''
We want to find the shortest path from src to dst that contains at most k + 2
verticies => modified Dijkstra's algorithm.

Normally, Dijkstra's algorithm explores verticies in the order of shortest
known distance to longest known distance. In this case, we want to explore in
the order of fewer stops from src to more stops from src (essentially a BFS)
and then terminate after exploring all verticies of k stops from src. To do
this with a priority queue, we would compare elements in a min-heap by number
of stops in the path from src. However, because verticies will be added in a
monotonically increasing order in terms of steps (BFS explores all verticies of
x steps before exploring verticies of x + 1 steps), elements in the heap will
never need to be shifted around to maintain the heap invariant. Thus, we can
just use a queue instead of a priority queue.
'''

if __name__ == '__main__':
    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    src = 0
    dst = 3
    k = 1
    print(find_cheapest_price(n, flights, src, dst, k))

