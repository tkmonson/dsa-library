'''
Alien Dictionary (#269)

There is a new alien language that uses the English alphabet, but the order of
the letters is unknown. You are given a list of strings words from the alien
language's dictionary. It is claimed that the strings in words are sorted
lexicographically by the rules of this new language.

If this claim is incorrect, and the given arrangement of strings in words
cannot correspond to any order of letters, return "". Otherwise, return a
string of the unique letters in the new alien language sorted in
lexicographically increasing order by the new language's rules. If there are
multiple solutions, return any of them.

A string `a` is lexicographically smaller than a string `b` if either of the
following is true:

    * The first letter where they differ is smaller in `a` than in `b`.
    * `a` is a prefix of `b` and `a.length < b.length`.

1 <= words.length <= 100
'''

from collections import defaultdict, deque

def alien_dictionary(words: list[str]) -> str:
    adj = defaultdict(set)
    indegree = {ch: 0 for word in words for ch in word}

    # Compare adjacent words, populate graph with edges
    for i in range(len(words) - 1):
        a, b = words[i], words[i + 1]
        for j in range(min(len(a), len(b))):
            if a[j] != b[j]:
                if b[j] not in adj[a[j]]:
                    indegree[b[j]] += 1
                adj[a[j]].add(b[j])
                break
        else:
            if len(a) > len(b):  # b is prefix of a; not allowed
                return ""

    # Kahn's algorithm
    result = []
    q = deque([ch for ch, d in indegree.items() if d == 0])
    while q:
        n = q.popleft()
        result.append(n)
        for m in adj[n]:
            indegree[m] -= 1
            if indegree[m] == 0:
                q.append(m)

    return ''.join(result) if len(result) == len(indegree) else ""

'''
You are given a list of words that is (potentially) sorted according to an
unknown order. You need to recover the order from the input.

Sorted means each word is less than the next. Adjacent words contain
information about the order. Non-adjacent words do not provide new information.
If w1 < w2 and w2 < w3, then it is implied that w1 < w3.

* ['hrn', 'hrf'] means 'n' comes before 'f'. 
* ['hr', 'hrf'] does not provide any order information.
* ['hrf', 'hr'] is invalid. For a prefix pair in ascending lexicographic order,
  the shorter word must come before the longer word.

Each adjacent pair contains at most one "comes before" fact. This sounds like a
"course scheduling" problem where some courses are prerequisites of others.
Recovering a total order from a set of pairwise precedence facts calls for
topological sort.

Topological sort can be done with BFS (Kahn's) or DFS. Kahn's algorithm needs
to keep track of indegrees.

1. Compare adjacent words, find letter where they differ
2. Put edge in adj list, update indegree dict
3. Kahn's algorithm
    * Put nodes of indegree 0 in queue
    * Dequeue, append letter to result
    * Remove adj edges, put nodes of indegree 0 in queue
    * Repeat until adj list is empty
4. If result does not contain all nodes, there is a cycle (no total order)
'''

if __name__ == '__main__':
    words = ['hrn', 'hrf', 'er', 'enn', 'rfnn']
    print(alien_dictionary(words))

'''
This solution is the first time I've ever used a for-else construct. Neat.
'''
