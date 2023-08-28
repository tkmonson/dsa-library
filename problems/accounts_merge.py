'''
Accounts Merge (#721)

Given a list `accounts` where each element `accounts[i]` is a list of strings,
each element `accounts[i][0]` is a name, and the rest of the elements in
`accounts[i]` are email addresses of the account, merge any accounts that share
an email address and return the list of accounts such that each name is
followed by all of the email addresses associated with the account in sorted
order.

Two accounts can have the same name but belong to different people (because
two different people could have the same name). If two accounts share an email
address, they belong to the same person (thus, any accounts that have the same
email address necessarily have the same name).
'''

from collections import defaultdict

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

class DisjointSet:
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
        if self.find(x) == self.find(y):
            return
        elif self.parent[self.find(x)] < self.parent[self.find(y)]:
            self.parent[self.find(x)] += self.parent[self.find(y)]
            self.parent[self.find(y)] = self.find(x)
        else:
            self.parent[self.find(y)] += self.parent[self.find(x)]
            self.parent[self.find(x)] = self.find(y)
    def find(self, x):
        if self.parent[x] < 0:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

'''
This implementation makes two modifications known as weighted union and
collapsing find. Initially, the root of each tree points to the value -1 (a
weight/rank/height of 1). When sets are unioned, the tree with the smaller
weight becomes the subtree of the tree with the larger weight, and the weight
of the smaller tree is added to the weight of the larger tree. This makes the
resulting tree more balanced, which reduces the time complexity of both
operations from O(n) to O(logn), worst-case. When find(x) is called for the
first time, the full path from x to the root is traversed, and then the path is
collapsed so that x points directly to the root, resulting in an O(1) time
complexity for both operations on subsequent calls.
'''

def accounts_merge(accounts: list[list[str]]) -> list[list[str]]:
    uf = DisjointSet(len(accounts))

    # Creat unions between indexes
    ownership = {}
    for i, (_, *emails) in enumerate(accounts):
        for email in emails:
            if email in ownership:
                uf.union(i, ownership[email])
            ownership[email] = i

    # Append emails to correct index
    ans = defaultdict(list)
    for email, owner in ownership.items():
        ans[uf.find(owner)].append(email)

    return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]

'''
As this problem involves merging (or unioning) accounts, the disjoint-set data
structure is a natural choice. The elements of the disjoint sets are the
indicies of the accounts. Each email address in the input is read and if one
has been read previously, its account is unioned with the account where it was
read previously. Every distinct email address is now associated with the
account where it was last read. This is where the disjoint-set data structure
has a great advantage: find (O(logn) first call, O(1) subsequent call) is
called on each of these accounts to find the unioned account that each email
will be added to.
'''

def accounts_merge2(accounts: list[list[str]]) -> list[list[str]]:
    n = len(accounts)
    email_sets = [set(account[1:]) for account in accounts]
    i = 0
    while i < n:
        if not email_sets[i]:
            i += 1
            continue
        merge_occurred = False
        j = i + 1
        while j < n:
            if email_sets[i].intersection(email_sets[j]):
                email_sets[i] = email_sets[i].union(email_sets[j])
                email_sets[j] = {}
                merge_occurred = True
            j += 1
        if not merge_occurred:
            i += 1

    result = []
    for i in range(n):
        if email_sets[i]:
            result.append([accounts[i][0]] + sorted(list(email_sets[i])))

    return result

'''
This is my initial solution that does not use a disjoint-set data structure.
It passes all test cases but is slow. Given a = [['John', 'email1', 'email2'],
['John', 'email3', 'email4'], ['John', 'email2', 'email3']], if you compare the
set of emails in a[0] to those in the other accounts in a linear fashion, you
will know that a[2] should be unioned with a[0], but you won't know that a[1]
should, too. You would have to union a[0] and a[2] and then consider a[1] with
regard to that union. I thought of this concept in terms of distance: a[2] is a
distance of 1 from a[0], a[1] is a distance of 2 from a[0]. So, in order to
find all of the email addresses to be unioned under account a[0], you could
union a[0] with all of the 1-distance accounts, then loop through all of the
accounts again to consider all remaining 2-distance accounts, then again with
the remaining 3-distance accounts, and so on, until a merge does not occur
during a loop.
'''

if __name__ == '__main__':
    accounts = [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["John", "johnsmith@mail.com", "john00@mail.com"],
                ["Mary", "mary@mail.com"],
                ["John", "johnnybravo@mail.com"]]
    print(accounts_merge(accounts))

'''
The disjoint-set data structure can be used to detect cycles in an undirected
graph. If graph A contains vertex x and graph B contains vertex y, the
connection of A and B by the edge (x, y) can be represented by the union of a
set containing A's verticies with a set containing B's verticies, both of which
are represented as trees. If A and B are already connected (x and y exist
within the same connected graph), the addition of edge (x, y) would produce a
cycle. Attempting to add (x, y) would be analogous to unioning a set containing
x and y with itself, which would produce no change. This cycle detection is
used in Kruskal's algorithm and Prim's algorithm.
'''

