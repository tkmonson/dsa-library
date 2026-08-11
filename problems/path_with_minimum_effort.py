'''
Path with Minimum Effort (#1631)

You are a hiker preparing for an upcoming hike. You are given `heights`, a 2D
array of size `rows x columns`, where `heights[row][col]` represents the height
of cell `(row, col)`. You are situated in the top-left cell, `(0, 0)`, and you
hope to travel to the bottom-right cell, `(rows-1, columns-1)`. You can move
up, down, left, or right, and you wish to find a route that requires the
minimum effort. A route's effort is the maximum absolute difference in heights
between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the
bottom-right cell.

1 <= heights[i][j] <= 10^6
'''

import heapq
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(script_dir, '_parent_import.py')).read())

from structures.disjoint_set import DisjointSet

# Time: O(|E|log|V|) = O((r * c)log(r * c))
# Auxiliary space: O(|V|^2) = (r * c)^2
def minimum_effort_path(heights: list[list[int]]) -> int:
    R, C = len(heights), len(heights[0])
    min_heap = [[0, 0, 0]]
    visited = set()

    while min_heap:
        diff, r, c = heapq.heappop(min_heap)

        if (r, c) in visited:
            continue
        visited.add((r, c))

        if (r, c) == (R - 1, C - 1):
            return diff
        
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_r, new_c = r + dr, c + dc

            if (new_r < 0 or new_r == R or
                new_c < 0 or new_c == C or
                (new_r, new_c) in visited):
                continue

            new_diff = max(diff, abs(heights[r][c] - heights[new_r][new_c]))
            heapq.heappush(min_heap, [new_diff, new_r, new_c])

'''
The problem statement should make you think about the shortest path problem.
While we are not trying to minimize the total path weight in this problem, we
*are* trying to minimize the maximum weight of an edge in the path (i.e. the
largest difference encountered along the path). So we can use Dijkstra's
algorithm.

We want to travel along edges with low weight before those with higher weight.
Dijkstra's algorithm is a "best-first search"; it prioritizes searching the
lowest-cost edges first by using a heap. For this problem, we keep track of the
greatest difference seen so far along a path instead of the total path weight.
'''

# Time: O(|E|log|E|) = O((r * c)log(r * c))
# Auxiliary space: O(|E|) = O(r * c)
def minimum_effort_path_kruskal(heights: list[list[int]]) -> int:
    R, C = len(heights), len(heights[0])
    uf = DisjointSet(R * C)
    edges = []
    result = 0

    for r in range(R):
        for c in range(C):
            i = r * C + c
            if c < C - 1:
                edges.append((i, i + 1, abs(heights[r][c] - heights[r][c + 1])))
            if r < R - 1:
                edges.append((i, i + C, abs(heights[r][c] - heights[r + 1][c])))
    edges = sorted(edges, key = lambda x: x[2])

    for u, v, diff in edges:
        if uf.union(u, v):
            result = max(result, diff)
        if uf.find(0) == uf.find(R * C - 1):
            break

    return result

'''
Edges in the grid can be added to a tree (forest) in ascending order of weight.
This is Kruskal's algorithm, and it is done with a union-find data structure.
If adding an edge to the tree would form a cycle, the edge is skipped. Continue
adding edges until the start and end belong to the same set. When this is true,
a path has been found between them, and it is the path with minimum effort
because the edges were processed from low to high difference.

Prim's algorithm could also be used to solve this problem. The difference is
only that, at each step of adding a new edge to the tree, Prim's algorithm
considers only edges between a node in the tree and a node outside of the tree.
'''

# Time: O(r * c * log(10 ** 6))
# Auxiliary space: O(r * c)
def minimum_effort_path_binary_search(heights: list[list[int]]) -> int:
    R, C = len(heights), len(heights[0])
    DIRS = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def dfs(r, c, visited, threshold):
        if r == R - 1 and c == C - 1:
            return True
        visited[r][c] = True

        for (dr, dc) in DIRS:
            new_r, new_c = r + dr, c + dc

            if (new_r < 0 or new_r == R or
                new_c < 0 or new_c == C or visited[new_r][new_c]):
                continue

            if (abs(heights[new_r][new_c] - heights[r][c]) <= threshold and
                dfs(new_r, new_c, visited, threshold)):
                return True

        return False

    def can_reach_destination(threshold):
        visited = [[False] * C for _ in range(R)]
        return dfs(0, 0, visited, threshold)

    left = 0
    right = ans = 10 ** 6
    while left <= right:
        mid = left + (right - left) // 2
        if can_reach_destination(mid):
            right = mid - 1
            ans = mid
        else:
            left = mid + 1
    return ans

'''
We are trying to minimize maximum difference between cells along a path. There
are lower and upper bounds for this value: 0 and 10^6 (given constraint).

Instead of using Dijkstra's algorithm to find the best path from start to end,
you can just DFS or BFS to see if there is any path from start to end, given a
threshold for maximum difference. Then you just binary search for the lowest
possible threshold where a path from start to end still exists.
'''

if __name__ == '__main__':
    heights = [[1,2,2],[3,8,2],[5,3,5]]
    print(minimum_effort_path_binary_search(heights))

'''
This problem cannot be solved with dynamic programming because when computing
dp(r, c) you can come from all 4 directions. So dp(r, c) depends on
dp(r - 1, c), for example, but dp(r - 1, c) also depends on dp(r, c). This is
a circular dependency, which means there is no valid order in which DP states
can be computed. In similar problems (like Unique Paths), where you can only
move down and right, DP is possible because there are no cycles in the state
graph (DAG).
'''
