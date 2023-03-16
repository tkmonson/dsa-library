'''
Clone Graph (#133)

Given a reference of a node in a connected, undirected graph, return a deep
copy (clone) of the graph.
'''

from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph_dfs(node: Node) -> Node:
    if node is None:
        return None

    node_map = {}
    node_map[node.val] = Node(node.val)

    def connect(node1, node2):
        node1.neighbors.append(node2)
        node2.neighbors.append(node1)

    def helper(curr):
        for nb in curr.neighbors:
            if nb.val not in node_map:
                node_map[nb.val] = Node(nb.val)
                connect(node_map[curr.val], node_map[nb.val])
                helper(nb)
            elif nb.val not in [n.val for n in node_map[curr.val].neighbors]:
                connect(node_map[curr.val], node_map[nb.val])

    helper(node)
    return node_map[1]


def clone_graph_bfs(node: Node) -> Node:
    if node is None:
        return None

    node_map = {}
    node_map[node.val] = Node(node.val)
    queue = deque([node])

    def connect(node1, node2):
        node1.neighbors.append(node2)
        node2.neighbors.append(node1)

    while queue:
        curr = queue.popleft()
        for nb in curr.neighbors:
            if nb.val not in node_map:
                node_map[nb.val] = Node(nb.val)
                connect(node_map[curr.val], node_map[nb.val])
                queue.append(nb)
            elif nb.val not in [n.val for n in node_map[curr.val].neighbors]:
                connect(node_map[curr.val], node_map[nb.val])

    return node_map[1]


if __name__ == '__main__':
    node1, node2, node3, node4 = Node(1), Node(2), Node(3), Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    print(clone_graph(node1))

'''
This problem involves traversing a graph, which can be done in a DFS or BFS
manner. One also has to make sure not to confuse nodes of the original graph
with nodes of the clone graph, but this problem is pretty straightforward
otherwise.
'''

