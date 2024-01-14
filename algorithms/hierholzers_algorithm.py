'''
Hierholzer's Algorithm (Eulerian Cycle Detection)

Given a directed graph G = (V, E), find the Eulerian cycle of G (an ordering of
E that represents a full traversal of G, starting and ending at the same
vertex).

Assume that G is represented as an adjacency list and that G has an Eulerian
cycle.

Time: O(E)
Auxiliary space: O(E) (call stack)
'''

from collections import deque

# Returns the vertex sequence of the Eulerian cycle
def hierholzer_vertices(graph: dict[str, list[str]], s: str) -> list[str]:
    cycle = deque()
    def dfs(v):
        while graph[v]:
            dfs(graph[v].pop())
        cycle.appendleft(v)

    dfs(s)
    return cycle


# Returns the Eulerian cycle
def hierholzer_edges(graph: dict[str, set[str]], s: str) -> list[str]:
    cycle = deque()
    def dfs(src, dst):
        while graph[dst]:
            dfs(dst, graph[dst].pop())
        cycle.appendleft([src, dst])
        while graph[src]:
            dfs(src, graph[src].pop())

    dfs(s, graph[s].pop())
    return cycle


if __name__ == '__main__':
    dg = {
      'A': {'E', 'B'},
      'B': {'D', 'C'},
      'C': {'Y', 'D'},
      'D': {'B', 'A'},
      'E': {'F'},
      'F': {'G'},
      'G': {'H'},
      'H': {'A'},
      'Y': {'Z'},
      'Z': {'C'}
    }
    print(hierholzer_edges(dg, 'Y'))

'''
These functions can also be used to find an Eulerian trail, provided that s is
set to the vertex with out-degree - in-degree = 1, if such a vertex exists.
'''

