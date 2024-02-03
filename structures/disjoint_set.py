'''
In mathematics, a collection of sets is disjoint if the intersection of any two
distinct sets in the collection is the empty set. If the union operation is
defined over these sets, such a collection of mutually disjoint sets can be
considered a partition of a set X if their union is X.

In computer science, a disjoint-set (or union-find) data structure stores a
partition of a set as a collection of mutually disjoint subsets. There are two
operations:
    1. Union, which merges two disjoint sets, and
    2. Find, which returns the "representative member" of a set.

A disjoint-set data structure is usually implemented as a disjoint-set forest;
that is, each set is represented by a tree, the root of which is the
"representative member" of the set, a kind of "name" for the set. Initially,
each element belongs to its own set (tree). When two sets are unioned, the root
of one tree becomes the child of the root of the other tree. Because both sets
are now represented by a single tree, they are considered to be one set whose
representative member is the root of the tree. The union of a set with itself
is itself (i.e. the union operation should do nothing in this case).
'''

class DisjointSetSimple:
    def __init__(self, n):
        self.parent = list(range(n))

    def union(self, x, y):
        self.parent[self.find(y)] = self.find(x)

    def find(self, x):
        return x if x == self.parent[x] else self.find(self.parent[x])

'''
In this implementation, each set is represented by a parent-pointer tree, and
the root of each tree points to itself. To find the representative member of
the set that some element x belongs to, you simply traverse up the tree from x
until you arrive at a node whose parent is itself (i.e. the root). When
unioning the set that some element x belongs to with the set that some element
y belongs to, if you find that x and y belong to the same set, the root of the
tree representing that set will become the child of itself (i.e. no change will
occur).
'''

class DisjointSet:
    def __init__(self, n):
        self.parent = [-1] * n

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        elif self.parent[rx] < self.parent[ry]:
            self.parent[rx] += self.parent[ry]
            self.parent[ry] = rx
        else:
            self.parent[ry] += self.parent[rx]
            self.parent[rx] = ry
        return True

    def find(self, x):
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

'''
This implementation makes two modifications known as weighted union and
collapsing find:

Initially, the root of each tree points to the value -1 (a weight/rank of 1).
When sets are unioned, the tree with the smaller weight becomes the subtree of
the tree with the larger weight, and the weight of the smaller tree is added to
the weight of the larger tree. This makes the resulting tree more balanced,
which reduces the time complexity of both operations from O(n) to O(logn),
worst-case.

When find(x) is called for the first time, the full path from x to the root is
traversed, and then the path is collapsed so that x points directly to the
root, resulting in an O(1) time complexity for both operations on subsequent
calls.
'''

'''
The disjoint-set data structure can be used to detect cycles in an undirected
graph. If graph A contains vertex x and graph B contains vertex y, the
connection of A and B by the edge (x, y) can be represented by the union of a
set containing A's verticies with a set containing B's verticies, both of which
are represented as trees. If A and B are already connected (x and y exist
within the same connected graph), the addition of edge (x, y) would produce a
cycle. Attempting to add (x, y) would be analogous to unioning a set containing
x and y with itself, which would produce no change. This cycle detection is
used in Kruskal's algorithm.
'''

