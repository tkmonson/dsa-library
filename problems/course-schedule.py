'''
Course Schedule (#207)

Given a total of `num_courses` courses that you have to take and an array
`prerequisites` where `prerequisites[i] = [a_i, b_i]` indicates that you must
take course `b_i` first if you want to take course `a_i`, return True if you
can finish all the courses or False otherwise.
'''

from collections import deque

def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    visited = set()
    dfs_tree = set()
    adj_list = [[] for _ in range(num_courses)]
    for p in prerequisites:
        adj_list[p[1]].append(p[0])

    def has_cycle(v):
        if v in dfs_tree:
            return True
        if v in visited:
            return False

        visited.add(v)
        dfs_tree.add(v)

        for n in adj_list[v]:
            if has_cycle(n):
                return True

        dfs_tree.remove(v)
        return False

    for v in range(num_courses):
        if has_cycle(v):
            return False
    return True

'''
This problem reduces to "check if a directed graph is acyclic." DFS is a
natural way of detecting cycles. An adjacency list is needed for DFS.

You have to start at a vertex with no prerequisites (in-degree = 0), but you
may not be able to reach all vertices in the graph from that vertex. In that
case, for a DAG, there will be multiple "start vertices."

Each vertex in the graph is in one of three states:
    1. Being visited. The vertex is contained in the current DFS tree, which
       means that the DFS has wrapped back on itself and there is a cycle.
    2. Previously visited. No need to move the search to this vertex because it
       has already been explored.
    3. Unvisited.
This implies that two collections need to be maintained, one for visited
vertices and one for the DFS tree, which adds elements as the search goes
deeper and removes elements as it backs out.
'''

def can_finish2(num_courses: int, prerequisites: list[list[int]]) -> bool:
    def topo_bfs(num_courses, prerequisites):
        adj_list = [[] for _ in range(num_courses)]
        in_degrees = [0] * num_courses
        for p in prerequisites:
            adj_list[p[1]].append(p[0])
            in_degrees[p[0]] += 1
    
        queue = deque()
        for v in range(num_courses):
            if in_degrees[v] == 0:
                queue.append(v)
    
        topo_order = []
        while queue:
            v = queue.popleft()
            topo_order.append(v)
    
            for n in adj_list[v]:
                in_degrees[n] -= 1
                if in_degrees[n] == 0:
                    queue.append(n)

        return topo_order if len(topo_order) == num_courses else None

    return True if topo_bfs(num_courses, prerequisites) else False

'''
This is an implementation of Kahn's algorithm, which generates a topological
ordering of a directed graph, a linear ordering of vertices such that, for every
edge uv from vertex u to vertex v, u comes before v. In the context of this
problem, a topological ordering is a valid scheduling of tasks.

Create an adjacency list and a list of in-degrees for every vertex. Fill a
queue with vertices of in-degree 0 ("start vertices"). Dequeue a vertex, add it
to a topological ordering list, process it by subtracting 1 from the in-degrees
of all of its neighbors and enqueuing any neighbors that now have in-degree 0,
and repeat until the queue is empty. This represents completing a task and thus
satisfying this prerequisite for neighboring tasks. If the final topological
ordering does not contain all vertices in the graph, no valid topological
ordering exists.
'''

if __name__ == '__main__':
    num_courses = 5
    prerequisites = [[1, 0], [1, 2], [3, 1], [3, 2], [4, 2], [2, 4]]
    print(can_finish2(num_courses, prerequisites))

