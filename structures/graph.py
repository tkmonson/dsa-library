from collections import defaultdict

class Graph:
    def __init__(self, connections, directed=False):
        self._adj_list = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        for source, dest in connections:
            self.add(source, dest)

    def add(self, source, dest):
        self._adj_list[source].add(dest)
        if not self._directed:
            self._adj_list[dest].add(source)

