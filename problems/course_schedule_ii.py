'''
Course Schedule II (#210)

Given a total of `num_courses` courses that you have to take and an array
`prerequisites` where `prerequisites[i] = [a_i, b_i]` indicates that you must
take course `b_i` first if you want to take course `a_i`, return any valid
ordering of courses if such an ordering exists or an empty array otherwise.
'''

def find_order_dfs(
        num_courses: int,
        prerequisites: list[list[int]]) -> list[int]:
    adj_list = [[] for _ in range(num_courses)]
    visited = set()
    dfs_tree = set()
    topo_order = []
    for p in prerequisites:
        adj_list[p[1]].append(p[0])

    def has_cycle(v):
        if v in visited:  # path already explored
            return False
        if v in dfs_tree:  # cycle detected
            return True

        dfs_tree.add(v)
        for n in adj_list[v]:
            if has_cycle(n):
                return True

        dfs_tree.remove(v)
        visited.add(v)
        topo_order.append(v)
        return False

    for v in range(num_courses):
        if has_cycle(v):
            return []
    return topo_order


def find_order_bfs(
        num_courses: int,
        prerequisites: list[list[int]]) -> list[int]:
    adj_list = [[] for _ in range(num_courses)]
    in_degrees = [0] * num_courses
    for p in prerequisites:
        adj_list[p[1]].append(p[0])
        in_degrees[p[0]] += 1

    queue = deque()
    for v, d in enumerate(in_degrees):
        if d == 0:
            queue.append(v)

    topo_order = []
    while queue:
        v = queue.popleft()
        topo_order.append(v)

        for n in adj_list[v]:
            in_degrees[n] -= 1
            if in_degrees[n] == 0:
                queue.append(n)

    return topo_order if len(topo_order) == num_courses else []


if __name__ == '__main__':
    num_courses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(find_order(num_courses, prerequisites))

