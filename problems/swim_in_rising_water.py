'''
Swim in Rising Water (#778)

You are given an nxn integer matrix where each cell value represents the
elevation at that point. Rain starts to fall. At time t, the depth of the water
everywhere is t. You can swim from one cell to a 4-directionally adjacent cell
if and only if the elevation of both cells is at most t. You can swim infinite
distances in zero time. You must stay within the grid boundaries.

Return the minimum amount of time it takes to swim from the top left cell to
the bottom right square.
'''

import heapq

def swim_in_water_dijkstra(grid: list[list[int]]) -> int:
    n = len(grid)
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    pq = [(grid[0][0], 0, 0)]  # (max height along path, row, column)
    visited = set(); visited.add((0, 0))

    while True:
        h, r, c = heapq.heappop(pq)
        if r == n - 1 and c == n - 1:
            return h

        for (dr, dc) in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                heapq.heappush(pq, (max(h, grid[nr][nc]), nr, nc))
                visited.add((nr, nc))

    return h

'''
This is a modified Dijkstra's algorithm. Instead of finding the shortest-length
path, we want to find the shortest-height path, where height is node value. The
key insight here is that we want to store entries in the heap of the form
(h, r, c), where (r, c) is the index of a cell and h is the tallest height
encountered so far on the path taken to that cell. Thus, at each step, we
continue along the path that will minimize total height/time.

Adding neighbors to the visited set as they are pushed to the heap ensures that
there will be no duplicate cells in the heap. If cells were instead added to
the visited set when popped, then the heap could contain duplicates of a cell,
for different paths to that cell. In this case, a visited check would be
required for each popped entry.

When an entry (h, r, c) is popped, h is guaranteed to be the shortest amount of
time required to reach the cell at (r, c).
'''

# Modified for tuple entries
class DisjointSet:
    def __init__(self, n):
        self.parent = {(i, j): (i, j) for i in range(n) for j in range(n)}

    def union(self, x, y):
        self.parent[self.find(y)] = self.find(x)

    def find(self, x):
        return x if x == self.parent[x] else self.find(self.parent[x])


# Slow (not sure why)
def swim_in_water_djs(grid: list[list[int]]) -> int:
    n = len(grid)
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    pq = []
    for r in range(n):
        for c in range(n):
            pq.append((grid[r][c], r, c))
    pq.sort()

    djs = DisjointSet(n)
    for h, r, c in pq:
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] <= h:
                djs.union((r, c), (nr, nc))
                if djs.find((0, 0)) == djs.find((n - 1, n - 1)):
                    return h

    return h  # for the [[0]] case

'''
Put every cell into a disjoint-set forest. Go through the cell from shortest to
tallest. Make connections between each cell and its neighbors, if possible.
Trees will begin to form throughout the grid. When trees connect such that the
start and end are contained in the same tree, you know that the minimum
required amount of time has passed.
'''

if __name__ == '__main__':
    grid = [[0, 1, 3],
            [2, 4, 1],
            [1, 2, 1]]
    grid = [[0]]
    print(swim_in_water_djs(grid))

