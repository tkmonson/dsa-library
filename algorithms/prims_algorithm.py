'''
Prim's Algorithm

Given an undirected, connected graph G = (V, E) and a set of edge weights, find
a minimum spanning tree of G.
'''

import heapq
from math import inf

# Time: O(|E|log|V|)
# Auxiliary space: O(|E|^2) (max amount of stale duplicates would be
#                            (E - 1) + (E - 2) + ... + 1)
def prim(adj_list, weight):
    cost = {v: inf for v in adj_list}
    prev = {}
    tree = set()
    pq = [(0, next(iter(adj_list)))]

    while len(tree) < len(adj_list):
        while (u := heapq.heappop(pq)[1]) in tree: pass
        tree.add(u)
        for v in adj_list[u]:
            if v not in tree and (w := weight((u, v))) < cost[v]:
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
            if v in pq and (w := weight((u, v))) < pq.get_priority(v):
                pq.decrease_key(v, priority=w)
                prev[v] = u

    return [(prev[v], v) for v in prev]


class PriorityQueue:
    def __init__(self, items=[]):
        self.pq = items
        self.index = {t: i for (i, [_, t]) in enumerate(items)}
        self._heapify()

    def __len__(self):
        return len(self.pq)

    def __contains__(self, task):
        return task in self.index

    def insert(self, task, priority=0):
        self.pq.append([priority, task])
        self._sift_up(len(self.pq) - 1)

    def pop(self):
        if len(self.pq):
            self.pq[0], self.pq[-1] = self.pq[-1], self.pq[0]
            self.index[self.pq[0][1]] = 0
            _, task = self.pq.pop()
            del self.index[task]
            self._sift_down(0)
            return task
        raise KeyError('Pop from empty priority queue')

    def decrease_key(self, task, priority=0):
        if self.get_priority(task) <= priority:
            raise ValueError('New priority is not less than old priority')
        c = self.index[task]
        self.pq[c][0] = priority
        self._sift_up(c)

    def get_priority(self, task):
        if task not in self.index:
            raise KeyError('Task not in priority queue')
        return self.pq[self.index[task]][0]

    def _heapify(self):
        for p in range(len(self.pq) // 2 - 1, -1, -1):
            self._sift_down(p)

    def _sift_up(self, c):
        p = (c - 1) // 2
        if c > 0 and self.pq[c] < self.pq[p]:
            self._swap(c, p)
            self._sift_up(p)

    def _sift_down(self, p):
        n = len(self.pq)
        cl, cr = 2 * p + 1, 2 * p + 2
        if cl >= n:
            return
        if cr >= n:
            cr = cl
        c = cl if self.pq[cl] < self.pq[cr] else cr

        if self.pq[c] < self.pq[p]:
            self._swap(c, p)
            self._sift_down(c)

    def _swap(self, i, j):
        self.index[self.pq[i][1]] = j
        self.index[self.pq[j][1]] = i
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]

'''
This solution adds all of the verticies to the heap initially. When the
priority of a vertex increases, the heap restructures itself to maintain the
heap invariant. To do this, the heap requires a decrease-key operation. The
heapq module does not provide this operation, so a custom heap implementation
is required.
'''

