'''
Course Schedule IV (#1462)

There are a total of `num_courses` courses you have to take, labeled from 0 to
`num_courses - 1`. You are given an array `prerequisites` where
`prerequisites[i] = [a_i, b_i]` indicates that you must take course `a_i` first
if you want to take course `b_i`.

Prerequisites can also be indirect. If course `a` is a prerequisite of course
`b`, and course `b` is a prerequisite of course `c`, then course `a` is a
prerequisite of course `c`.

You are also given an array `queries` where `queries[j] = [u_j, v_j]`. For the
jth query, you should answer whether course `u_j` is a prerequisite of course
`v_j` or not.

Return a boolean array `answer`, where `answer[j]` is the answer to the jth
query.

The prerequisites graph has no cycles.
'''

from collections import deque

def check_if_prerequisite_dfs(
        num_courses: int,
        prerequisites: list[list[int]],
        queries: list[list[int]]) -> list[int]:
    adj_list = [[] for _ in range(num_courses)]
    visited = set()
    dfs_path = set()
    successors = [set() for _ in range(num_courses)]
    for p in prerequisites:
        adj_list[p[0]].append(p[1])

    def dfs(v):
        if v in visited:  # path already explored
            return
        
        for p in dfs_path:
            successors[p].add(v)

        dfs_path.add(v)
        for n in adj_list[v]:
            successors[v].add(n)
            if n in visited:
                for s in successors[n]:
                    successors[v].add(s)
            dfs(n)

        dfs_path.remove(v)
        visited.add(v)

    for v in range(num_courses):
        dfs(v)

    answer = []
    for a, b in queries:
        answer.append(b in successors[a])
    return answer

'''
Similar to previous versions of this problem, but this time you need to pass
prerequisite information as you search. In DFS, because you are keeping track
of the DFS path, you can mark all the nodes in the path as having the current
node as a successor. (It can probably also be written in terms of prereqs.)
'''

def check_if_prerequisite_bfs(
        num_courses: int,
        prerequisites: list[list[int]],
        queries: list[list[int]]) -> list[int]:
    adj_list = [[] for _ in range(num_courses)]
    in_degrees = [0] * num_courses
    for p in prerequisites:
        adj_list[p[0]].append(p[1])
        in_degrees[p[1]] += 1

    queue = deque()
    for v, d in enumerate(in_degrees):
        if d == 0:
            queue.append(v)

    prereqs = [set() for _ in range(num_courses)]
    while queue:
        v = queue.popleft()
        for n in adj_list[v]:
            prereqs[n].add(v)
            for p in prereqs[v]:
                prereqs[n].add(p)

            in_degrees[n] -= 1
            if in_degrees[n] == 0:
                queue.append(n)

    answer = []
    for a, b in queries:
        answer.append(a in prereqs[b])
    return answer

'''
Because BFS does not keep track of courses that came before, it is easier to
pass the prerequisites of the current node as prerequisites of its neighbors.
'''

if __name__ == '__main__':
    num_courses = 3
    prerequisites = [[1,2],[1,0],[2,0]]
    queries = [[1,0],[1,2]]
    print(check_if_prerequisite_bfs(num_courses, prerequisites, queries))

'''
Note that the definition of the prerequisites array is reversed from what it
was in Course Schedule I and II.
'''