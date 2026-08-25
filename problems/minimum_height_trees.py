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

# Time: O(n)
# Auxiliary space: O(n)
def find_minimum_height_trees(n: int, edges: list[list[int]]) -> list[int]:
    adj_list = [set() for _ in range(n)]
    for edge in edges:
        adj_list[edge[0]].add(edge[1])
        adj_list[edge[1]].add(edge[0])

    leaves = deque([i for i in range(n) if len(adj_list[i]) <= 1])

    while n > 2:
        n -= len(leaves)
        for _ in range(len(leaves)):
            neighbor = adj_list[leaves[0]].pop()
            adj_list[neighbor].remove(leaves[0])

            leaves.popleft()
            if len(adj_list[neighbor]) == 1:
                leaves.append(neighbor)

    return list(leaves)

'''
This solution repeatedly prunes the tree, from the outside nodes to the inside
nodes, until only the innermost nodes remain. It is like peeling the layers of
an onion until you get to its core or eating the grapes on the outside of the
bunch before eating the grapes closer to the center.

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

'''
The naive solution is to do a DFS or BFS on each possible tree rooted at each
node. This would be O(n^2).

There is another possible O(n) solution:

1. Choose a node at random (A)
2. Do a DFS (or BFS) to find the longest path starting at A
3. The node at the end of this path (B) must be on the longest path globally
   (Longest path from R will go through center and then out to a leaf)
4. Do a DFS (or BFS) to find the longest path starting at B (ends at C)
   (It will also go through center and then out to a leaf)
5. The path from B to C is the longest path globally. Its innermost node(s) is
   the root of the MHT.
6. Prune the ends of this path until only 1 or 2 nodes remain.
'''