'''
Minimum Degree of a Connected Trio in a Graph

A connected trio is a set of three nodes where there is an edge between every
pair of them. The degree of a connected trio is the number of edges where one
endpoint is in the trio and the other is not. Given the number of nodes in the
graph and a list of undirected edges, return the minimum degree of a connected
trio in the graph or -1 if the graph has no connected trios.

-------------------------------------------------------------------------------

There are three solutions given below; the third is the most efficient.
General lessons:
    * When given an edge list, consider creating an adjacency list/matrix.
    * To find the minimum degree of a connected trio, all connected trios must
      be explored.
    * If the solution requires that three for loops be nested and it still is
      not fast enough, consider reducing the bounds of the loops.
    * When given 1-indexed elements, consider looping over range(1, n + 1) and
      leaving the 0th element untouched to avoid off-by-one errors.
'''


'''
Solution 1 (Adjacency List of Sets + Intersection)

* Create adjacency list.
* For the first node, consider all n nodes.
* For the second node, consider neighbors of the first node whose values are
  greater than that of the first node (this prevents double-counting of the
  undirected edges, e.g. [2, 7] is considered, [7, 2] is not).
* Intersect the set of the first node and its neighbors with the set of the
  second node and its neighbors. If the first and second nodes are part of the
  same trio, the intersection will contain the first node, the second node, and
  at least one other node.
* For the third node, consider all nodes in the intersection, excluding the
  first and second node.
* Calculate the degree of each trio (sum of (len(neighbors) - 2) for all three
  nodes), save it if it is the smallest degree so far.
* When finished exploring, return minimum degree.
'''
def min_trio_degree(n: int, edges: list[list[int]]) -> int:
    adj_list = [set() for _ in range(n)]
    for edge in edges:
        adj_list[edge[0] - 1].add(edge[1])
        adj_list[edge[1] - 1].add(edge[0])

    min_degree = float('inf')
    for i in range(n):
        s1 = adj_list[i].union({i + 1})
        for j in filter(lambda x: x > i, adj_list[i]):
            s2 = adj_list[j - 1].union({j})
            intersection = s1.intersection(s2)
            if (i + 1) in intersection and j in intersection:
                intersection.remove(i + 1); intersection.remove(j)
                for k in intersection:
                    degree = 0
                    for node in [i + 1, j, k]:
                        degree += len(adj_list[node - 1]) - 2
                    min_degree = min(min_degree, degree)

    return min_degree if min_degree != float('inf') else -1


'''
Solution 2 (Adjacency Matrix of Binary Numbers + Bitmasking Intersection)

* Create adjacency matrix (implemented as a list of ints, where the MSB
  represents node 1 and the LSB represents node n) with 1s on the diagonal.
* For the first node, consider all n nodes.
* For the second node, consider nodes with values greater than that of the
  first node.
* If there is no edge between the first and second nodes, consider the next
  second node.
* For the third node, consider nodes with values greater than that of the
  second node.
* Intersect the rows corresponding to the first, second, and third nodes. If
  the intersection has 1s in positions corresponding to the first, second, and
  third nodes, the nodes form a trio.
* For each of these three rows, set the bits that correspond to the first,
  second, and third nodes to 0 and calculate the Hamming weight (the number of
  1s in a binary number) of the result. This is the degree of the trio, save it
  if it is the smallest degree so far.
* When finished exploring, return minimum degree.
'''
def min_trio_degree2(n: int, edges: list[list[int]]) -> int:
    powers = [2 ** x for x in range(n)[::-1]]
    adj_mat = powers[:]
    for pair in edges:
        adj_mat[pair[0] - 1] += 2 ** (n - pair[1])
        adj_mat[pair[1] - 1] += 2 ** (n - pair[0])

    min_degree = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if adj_mat[i] & powers[j] != powers[j]:
                continue
            for k in range(j + 1, n):
                intersection = adj_mat[i] & adj_mat[j] & adj_mat[k]
                trio_mask = powers[i] + powers[j] + powers[k]
                if intersection & trio_mask == trio_mask:
                    degree = 0
                    for row in (adj_mat[i], adj_mat[j], adj_mat[k]):
                        row -= trio_mask
                        while row:
                            row &= row - 1
                            degree += 1
                    min_degree = min(min_degree, degree)

    return min_degree if min_degree != float('inf') else -1


'''
Solution 3 (Adjacency List of Sets + Visited Set + DFS)

* Create adjacency list and empty visited set.
* For the first node, consider all n nodes.
* For the second node, consider the neighbors of the first node.
* If the edge sorted(first, second) has been visited, consider the next second
  node. Else, add sorted(first, second) to the visited set. This will prevent
  exploring trios twice, once CW, once CCW. For example:

  3 - 1      When 1 is first, (1, 2) is visited, and (1, 2, 3) is explored CW.
   \ / \     When 2 is first, (1, 2) is already visited, so (2, 4) is visited
    2 - 4    instead, and (2, 4, 1) is explored CCW.

* For the third node, consider the neighbors of the second node (excluding the
  first node).
* If the first node is a neighbor of the third node, the nodes form a triple.
  Add sorted(third, first) to the visited set. This will also prevent exploring
  trios twice. For example, in the above diagram, when 1 is first, while
  exploring (1, 2, 3), (1, 3) is visited. Thus, (1, 3, 2) cannot be explored.
* Calculate the degree of each trio (sum of (len(neighbors) - 2) for all three
  nodes), save it if it is the smallest degree so far.
* When finished exploring, return minimum degree.

This is the most efficient solution because the j and k loops only loop over
lists of neighbors instead of over range(n) and because each trio is only
explored in one direction, either CW or CCW.
'''
def min_trio_degree3(n: int, edges: list[list[int]]) -> int:
    adj_list = [set() for _ in range(n + 1)]
    for edge in edges:
        adj_list[edge[0]].add(edge[1])
        adj_list[edge[1]].add(edge[0])

    min_degree = float('inf')
    visited = set()
    for i in range(1, n + 1):
        for j in adj_list[i]:
            e1 = tuple(sorted((i, j)))
            if e1 in visited:
                continue
            visited.add(e1)
            for k in adj_list[j]:
                if k == i:
                    continue
                e2 = tuple(sorted((k, i)))
                if i in adj_list[k]:
                    visited.add(e2)
                    degree = (len(adj_list[i]) - 2 +
                              len(adj_list[j]) - 2 +
                              len(adj_list[k]) - 2)
                    min_degree = min(min_degree, degree)

    return min_degree if min_degree != float('inf') else -1


if __name__ == '__main__':
    print(min_trio_degree3(
        17,
        [[12,10],[12,16],[4,9],[4,6],[14,1],[9,2],[17,6],[17,12],[8,9],[11,14],
         [13,5],[8,15],[13,11],[15,11],[15,14],[6,8],[12,15],[14,12],[9,1],
         [9,10],[10,5],[1,11],[2,10],[15,1],[7,9],[14,2],[4,1],[17,7],[3,17],
         [8,1],[17,13],[10,13],[8,13],[1,7],[2,6],[13,6],[7,2],[1,16],[6,3],
         [6,9],[16,17],[7,14]]
    ))

