'''
Minimum Height Trees (#310)

A tree is an undirected graph in which any two vertices are connected by
exactly one path (an acyclic, connected graph).

Given a tree of n nodes labeled from 0 to n - 1 and an array of n - 1 edges
where edges[i] = [a_i, b_i] indicates that there is an undirected edge between
the two nodes a_i and b_i in the tree, choose any node of the tree as the root.
Among all possible rooted trees, those with minimum height are called minimum
height trees (MHTs). Return, in any order, a list of the values of the roots of
all of the MHTs.
'''

from collections import deque

def find_minimum_height_trees_naive(n: int,
                                    edges: list[list[int]]) -> list[int]:
    adj_list = [[] for _ in range(n)]
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    def height(i):
        seen.add(i)
        unseen_children = [c for c in adj_list[i] if c not in seen]
        if not unseen_children:
            return 1
        return 1 + max([height(c) for c in unseen_children])

    min_height = float('inf')
    roots = []
    for i in range(n):
        seen = set()
        if (h := height(i)) < min_height:
            min_height = h
            roots = []
        if h == min_height:
            roots.append(i)

    return roots

'''
This solution simply finds the height of each possible tree using recursion and
keeps track of the minimum height trees and their roots.
'''

def find_minimum_height_trees(n: int, edges: list[list[int]]) -> list[int]:
    adj_list = [[] for _ in range(n)]
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    leaves = deque([i for i in range(n) if len(adj_list[i]) == 1])

    while n > 2:
        n -= len(leaves)
        for _ in range(len(leaves)):
            neighbor = adj_list[leaves[0]].pop()
            adj_list[neighbor].remove(leaves[0])

            leaves.popleft()
            if len(adj_list[neighbor]) == 1:
                leaves.append(neighbor)

    return leaves

'''
Consider a path graph (which is a tree). The MHT of this graph is rooted at the
middle vertex (or at one of the two middle vertices if the graph contains an
even number of vertices). We can isolate these vertices by sequentially
removing the leaves of the graph until only one or two vertices remain.

Similarly, in general, MHTs are those trees that are rooted at the most central
vertices of their graphs. These vertices can be found by removing the leaves of
a graph, updating the edges / adjacency list / degrees of neighbors, and
repeating until the graph contains only one or two vertices.

This is similar to Kahn's algorithm, a BFS variant of topological sort.
'''

if __name__ == '__main__':
    n = 6
    edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    print(find_minimum_height_trees(n, edges))

