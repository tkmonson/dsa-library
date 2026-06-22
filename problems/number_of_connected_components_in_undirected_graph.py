'''
Number of Connected Components in Undirected Graph (#323)

Given `n` nodes labeled from `0` to `n - 1` and a list of undirected edges
(each edge is a pair of nodes), write a function to find the number of
connected components in an undirected graph.
'''

# Time: O(V + E)
# Auxiliary space: O(V)
def num_components(n: int, edges: list[list[int]]) -> int:
    count = 0
    visited = set()

    adj = [[] for _ in range(n)]
    for e in edges:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])

    def dfs(i):
        visited.add(i)
        for nb in adj[i]:
            if nb not in visited:
                dfs(nb)

    for i in range(n):
        if i in visited:
            continue
        dfs(i)
        count += 1

    return count

'''
Convert edge list to adjacency list
For each key in adj list:
    Skip key if visited
    Do a DFS starting at key, add nodes to visited set
    Increment component count when the DFS completes
'''

if __name__ == '__main__':
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    print(num_components(n, edges))

