'''
Jump Game VII (#1871)

You are given a 0-indexed binary string `s` and two integers `min_jump` and
`max_jump`. In the beginning, you are standing at index 0, which is equal to
'0'. You can move from index i to index j if the following conditions are
fulfilled:

    * i + minJump <= j <= min(i + maxJump, s.length - 1), and
    * s[j] == '0'.

Return true if you can reach index s.length - 1 in s, or false otherwise.
'''

from collections import deque

def can_reach_bfs(s: str, min_jump: int, max_jump: int) -> bool:
    if s[-1] == '1':
        return False

    n = len(s)
    q = deque([0])
    farthest = 0
    while q:
        i = q.popleft()
        L = max(i + min_jump, farthest + 1)
        R = min(i + max_jump, n - 1)

        for j in range(L, R + 1):
            if s[j] == '0':
                if j == n - 1:
                    return True
                q.append(j)

        farthest = R

    return False

'''
You can do a 1D BFS, which will explore the space in layers. From the start
(layer 0), consider the range you are able to jump into. This is layer 1. In
this range, you can jump from each 0 to a new range. Those ranges are layer 2.

The ranges may overlap. In this case, you don't want to reexplore the
overlapping space. To avoid this, keep track of the farthest index you have
explored so far. If the next range has left boundary less than the farthest
index, start the range at the farthest index instead.

Because shallower layers are explored before deeper layers and layers are
explored left to right and the range is fixed in size and relative position,
the next range is guaranteed to explore farther than the farthest index
explored so far.

    *       *       * *     *
    0 1 1 1 0 1 0 1 0 0 0 1 0
    i    [ L1  ]
                 [ L2  ]
                         [ L3  ]
                           [ L3  ]
'''

# Time: O(n)
# Auxiliary space: O(n)
def can_reach_dfs(s: str, min_jump: int, max_jump: int) -> bool:
    if s[-1] == '1':
        return False

    n = len(s)
    visited = set()
    def dfs(i):
        if i == n - 1:
            return True
        L = i + min_jump
        R = min(i + max_jump, n - 1)
        for j in range(L, R + 1):
            if j in visited:
                break
            visited.add(j)
            if s[j] == '1':
                continue
            if dfs(j):
                return True
        return False  # all deadends from this point

    return dfs(0)

'''
DFS is not the fastest solution, but it does pass.

From the start, consider the range you are able to jump into.
From the first 0 in that range, jump to the next range.
Go as deep as you can, backtrack when you cannot proceed.
Mark all visited indicies to prevent repeated work.
'''

# Time: O(n)
# Auxiliary space: O(n)
def can_reach_dp(s: str, min_jump: int, max_jump: int) -> bool:
    if s[-1] == '1':
        return False
    
    n = len(s)
    dp = [False] * n
    dp[0] = True

    reachable = 0
    for i in range(min_jump, n):
        added_index = i - min_jump
        removed_index = i - max_jump - 1
        if dp[added_index]:
            reachable += 1
        if removed_index >= 0 and dp[removed_index]:
            reachable -= 1
        dp[i] = (reachable > 0 and s[i] == '0')

    return dp[-1]

'''
This is a sliding window solution. For each i you are jumping to, there is a
range behind it, from which you can jump to i.

    0 1 1 1 0 1 0 1 0 0 0 1 0        0 1 1 1 0 1 0 1 0 0 0 1 0
     ]    i                         [     ]    i

You want to know if the end is reachable from the start. You can do this by
answering if i is reachable from the start, for all i. You find answers for
larger i from previous answers for smaller i, so this is a DP approach.

i is reachable if the range includes at least one reachable index and i is a 0.
As you increment i, update the count of reachable indicies in the range.
'''

if __name__ == '__main__':
    s = "0111010100010"
    min_jump = 3
    max_jump = 5
    print(can_reach_bfs(s, min_jump, max_jump))

'''
The player is allowed to jump within a range that is fixed in size and relative
position, but they must land on a 0.

It's not optimal to choose the 0 in the range that will get you the farthest to
the right, like in Jump Game II, so there is no greedy solution. You need to
explore all the 0s or do DP.
'''
