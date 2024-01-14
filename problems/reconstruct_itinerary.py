'''
Reconstruct Itinerary (#332)

Given a list of airline `tickets` where `tickets[i] = [from_i, to_i]`
represents the departure and arrival airports of one flight, reconstruct the
full itinerary in order and return it.

All of the tickets belong to a man who depart from 'JFK'. Thus, the itinerary
must begin with 'JFK'. If multiple valid itineraries exist, return the
itinerary that comes first in lexical order.

    e.g. ['JFK', 'LGA'] comes before ['JFK', 'LGB'] in lexical order.

You may assume all tickets form at least one valid itinerary. You must use each
ticket exactly once.
'''

from collections import defaultdict, deque

# Time: O(E)
# Auxiliary space: O(E) (adjacency list and call stack)
def find_itinerary(tickets: list[list[str]]) -> list[str]:
    tickets.sort(reverse=True)
    adj_list = defaultdict(list)
    for src, dst in tickets:
        adj_list[src].append(dst)

    cycle = deque()
    def dfs(v):
        while adj_list[v]:
            dfs(adj_list[v].pop())
        cycle.appendleft(v)

    dfs('JFK')
    return cycle

'''
This is an application of Hierholzer's algorithm. Because you have to both
arrive and depart from each airport (every vertex has equal in-degree and
out-degree), the graph is guaranteed to have an Eulerian cycle.

There is a primary cycle that starts and ends at the starting vertex, and there
may be any number of secondary cycles that start and end at other verticies.

The reason the above implementation is so elegant is that it only adds a vertex
to the result when the trail is backing out of recursion and the vertex has no
unexplored adjacent edges. The trail will expand toward the adjacent vertex
that appears first in lexical order, and this may or may not be along the
primary cycle. Eventually, the trail (which may contain secondary cycles) will
return to the starting vertex, and then it will back out of the recursion. If
the trail backs out to a vertex v with no unexplored adjacent edges, v will be
added to the result. Otherwise, if v does have unexplored adjacent edges, the
trail will expand again to explore those edges, moving through secondary cycles
that return to v. And once all cycles that start and end at v are explored, the
trail will back out of those cycles, adding verticies to the result.

The effect is that it does not matter if you explore secondary cycles before or
after exploring the primary cycle. The verticies will be added to the result in
the correct order regardless.
'''

# Time: O(E^d) where d is the max degree of a vertex
# Auxiliary space: O(E) (adjacency list and call stack)
# Works, but not fast enough to pass all test cases
def find_itinerary2(tickets: list[list[str]]) -> list[str]:
    tickets.sort()
    adj_list = {src: [] for src, dst in tickets}
    for src, dst in tickets:
        adj_list[src].append(dst)

    cycle = ['JFK']
    def dfs(src):
        if len(cycle) == len(tickets) + 1:
            return True
        if src not in adj_list:
            return False

        for i, v in enumerate(adj_list[src]):
            if not v:
                continue
            adj_list[src][i] = ''
            cycle.append(v)
            if dfs(v):
                return True
            adj_list[src][i] = v
            cycle.pop()

        return False

    dfs('JFK')
    return cycle


if __name__ == '__main__':
    tickets = [
        ['JFK', 'SFO'],
        ['JFK', 'ATL'],
        ['SFO', 'ATL'],
        ['ATL', 'JFK'],
        ['ATL', 'SFO']
    ]
    print(find_itinerary(tickets))

