'''
Construct Quad Tree (#427)

Given a `n x n` matrix grid of 0s and 1s only. We want to represent grid with a
Quad-Tree.

A Quad-Tree is a tree data structure in which each internal node has exactly
four children. It is most often used to partition a 2D space by recursively
subdividing it into quadrants.

If all four quadrants consist of the same value, then the node representing
that grid is a leaf. val tells you what that value is, if the node is a leaf;
otherwise, it can be any value.

Return the root of the Quad-Tree representing grid.
'''

class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


# Time: O(n^2)
# Auxiliary space: O(logn) (stack)
def construct(grid: list[list[int]]) -> Node:
    def dfs(r, c, s):
        if s == 1:
            return Node(grid[r][c], True, None, None, None, None)

        half = s // 2
        tl = dfs(r, c, half)
        tr = dfs(r, c + half, half)
        bl = dfs(r + half, c, half)
        br = dfs(r + half, c + half, half)

        if (tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and
            tl.val == tr.val == bl.val == br.val):
            return Node(tl.val, True, None, None, None, None)
        else:
            return Node(0, False, tl, tr, bl, br)
        
    return dfs(0, 0, len(grid))
