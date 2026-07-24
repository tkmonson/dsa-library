'''
Evaluate Division (#399)

You are given an array of variable pairs `equations` and an array of real
numbers `values`, where `equations[i] = [A_i, B_i]` and values[i] represent the
equation `A_i / B_i = values[i]`. Each `A_i` or `B_i` is a string that
represents a single variable.

You are also given some `queries`, where `queries[j] = [C_j, D_j]` represents
the `jth` query where you must find the answer for `C_j / D_j = ?`.

Return the answers to all queries. If a single answer cannot be determined,
return -1.0.

Note: The input is always valid. You may assume that evaluating the queries
will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined,
so the answer cannot be determined for them.
'''

from collections import defaultdict, deque

# Time: O(q * e)
# Auxiliary space: O(q + e)
def calc_equation_dfs(
        equations: list[list[str]],
        values: list[float],
        queries: list[list[str]]) -> list[float]:
    
    adj = defaultdict(list)
    for i, e in enumerate(equations):
        adj[e[0]].append((e[1], values[i]))
        adj[e[1]].append((e[0], 1 / values[i]))

    def dfs(curr):
        nonlocal target, found
        if curr == target:
            found = True
            return 1

        for nb in adj[curr]:
            node, weight = nb
            if node not in visited:
                visited.add(node)
                result = weight * dfs(node)
                if found:
                    return result
                visited.remove(node)

        return 0

    ans = []
    for q in queries:
        curr, target = q
        if curr not in adj or target not in adj:
            ans.append(-1.0)
            continue

        found = False
        visited = set([curr])
        result = dfs(curr)
        ans.append(result if found else -1.0)

    return ans

'''
Because DFS explores only one path at a time, the path weight so far can be
stored within the recursive stack. Because the result can be any float value,
there isn't really a special value you can return from the DFS to signify that
the target was not found. This is why I use a nonlocal found variable.
'''

# Time: O(q * e)
# Auxiliary space: O(q + e)
def calc_equation_bfs(
        equations: list[list[str]],
        values: list[float],
        queries: list[list[str]]) -> list[float]:
    
    adj = defaultdict(list)
    for i, e in enumerate(equations):
        adj[e[0]].append((e[1], values[i]))
        adj[e[1]].append((e[0], 1 / values[i]))

    def bfs(src, target):
        if src not in adj or target not in adj:
            return -1.0
        q = deque([(src, 1)])
        visited = set([src])
        while q:
            n, w = q.popleft()
            if n == target:
                return w
            for nb, weight in adj[n]:
                if nb not in visited:
                    q.append((nb, w * weight))
                    visited.add(nb)

        return -1.0

    return [bfs(q[0], q[1]) for q in queries]

'''
Because the BFS traverses multiple paths at once, you need to store the path
weight so far for each path. You can store this along with each node in the
queue.
'''

if __name__ == '__main__':
    equations = [['a','b'], ['b','c']]
    values = [2.0,3.0]
    queries = [['a','c'], ['b','a'], ['a','e'], ['a','a'], ['x','x']]
    print(calc_equation_bfs(equations, values, queries))

'''
This is actually a graph problem. The intuition for this is that you are given
a list of pairwise relationships (relationships between exactly two entities).
These are connections between entities that form a graph.

a / b = 2.0 is a factor. We want to create a chain of factors that equals the
query. A chain is a path. So (a / b) * (b / c) = a / c is a path a -> b -> c.

1. Create a weighted directed graph with equations and values. Each equation
   [a, b] with value w creates two directed edges: a -> b with weight w (a / b)
   and b -> a with weight 1 / w (b / a).
2. DFS or BFS through the graph, starting at the query numerator, until you
   visit the query denominator. Keep track of the chain value as you traverse.
   Use a visited set to avoid loops.
3. If the query includes variables that do not exist in the graph, return -1.0
   (even if query is x / x, which is dumb, but that is what the problem says).
4. Repeat for all queries.
'''
