'''
Network Delay Time (#743)

You are given a network of `n` nodes, labeled from 1 to `n`. You are also given
`times`, a list of travel times as directed edges `times[i] = (u_i, v_i, w_i)`,
where `u_i` is the source node, `v_i` is the target node, and `w_i` is the time
it takes for a signal to travel from source to target.

We will send a signal from a given node `k`. Return the minimum time it takes
for all `n` nodes to receive the signal. If it is impossible for all `n` nodes
to receive the signal, return -1.
'''

from collections import defaultdict
import heapq
from math import inf

exec(open('_parent_import.py').read())
from algorithms.dijkstra import dijkstra, dijkstra2

def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    adj_list = defaultdict(list)
    for u, v, w in times:
        adj_list[u].append((w, v))
    heap = [(0, k)]
    visited = set()

    while len(visited) < n:
        try:
            time_k_to_u, u = heapq.heappop(heap)
        except IndexError:
            return -1
        visited.add(u)

        for time_u_to_v, v in adj_list[u]:
            if v not in visited:
                heapq.heappush(heap, (time_k_to_u + time_u_to_v, v))

    return time_k_to_u

'''
This solution uses Dijkstra's algorithm, but it does not keep track of the
information (distance and predecessor for all verticies) that would normally be
returned by Dijkstra's algorithm. This is acceptable because the minimum time
to reach all verticies is equal to the time to reach the vertex farthest from
the source. Dijkstra's algorithm will visit this vertex last, so only the last
distance value is needed.
'''

def network_delay_time2(times: list[list[int]], n: int, k: int) -> int:
    adj_list = {i: [] for i in range(1, n + 1)}
    edge_length = {}
    for u, v, w in times:
        adj_list[u].append(v)
        edge_length[(u, v)] = w

    distance = dijkstra(adj_list, edge_length, k)[0]
    ans = max(distance.values())
    return ans if ans != inf else -1

'''
This solution makes use of an implementation of Dijkstra's algorithm that
returns a full list of distances from the source to each vertex. This is more
information than is required for this problem, but it is convenient to make use
of a standard, pre-written algorithm.
'''

if __name__ == '__main__':
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    print(network_delay_time(times, n, k))

