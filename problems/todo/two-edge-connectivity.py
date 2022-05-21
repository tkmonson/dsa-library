'''
Given an undirected connected graph, determine whether it is 2-edge-connected
or not. A connected graph is 2-edge-connected if it remains connected when any
one edge is removed.

Examples:
    Input:

        b       - - f
      /   \     | /
    a   |   d - e
      \   /       \
        c           g

    Output: False (bridges at (d,e) and (e,g))

    Input:

        b - c
      /       \
    a           d
      \       /
        f - e

    Output: True (no bridges)
'''

from structures.graph import Graph

def two_edge_connectivity(graph):
    
