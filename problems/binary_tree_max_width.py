'''
Maximum Width of Binary Tree (#662)

Given the root of a binary tree, return the maximum width of the given tree.
The maximum width of a tree is the maximum width among all levels. The width of
one level is defined as the length between the end-nodes (the leftmost and
rightmost non-null nodes), where the null nodes between the end-nodes that
would be present in a complete binary tree extending down to that level are
also counted into the length calculation.
'''

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time: O(n)
# Auxiliary space: O(n)
def width_of_binary_tree(root: TreeNode) -> int:
    if not root:
        return 0

    q = deque([(root, 1)])
    max_width = 1

    while q:
        max_width = max(max_width, q[-1][1] - q[0][1] + 1)
        for _ in range(len(q)):
            root, index = q.popleft()
            if root.left:
                q.append((root.left, 2 * index))
            if root.right:
                q.append((root.right, 2 * index + 1))

    return max_width

'''
Since widths are to be evaluated level by level, a BFS approach makes sense.
But the width cannot be calculated if only non-null nodes are added to the
queue, and adding null nodes to the queue would have a worst-case space
complexity of O(2^n) (in the case of a path). So some information must be
stored in addition to the non-null nodes without storing all of the null nodes.

My first attempt was to store a tuple of each node and the "gap" to its left,
but this proved to be complicated. Instead, one can store a tuple of each node
and its "heap index" (for a node of index i, its left child has index 2i and
its right child has index 2i + 1). With this information, calculating the width
at each level is simple.
'''

if __name__ == '__main__':
    TN = TreeNode
    root = TN(1,
              TN(1,
                 TN(1),
                 TN(1,
                    None,
                    TN(1,
                       TN(2,
                          TN(2,
                             TN(2),
                             None),
                          TN(2,
                             TN(2),
                             None)),
                       TN(2,
                          TN(2,
                             None,
                             TN(2)),
                          TN(2,
                             None,
                             TN(2)))))),
              TN(1,
                 TN(1),
                 TN(1)))
                                      
    print(width_of_binary_tree(root))

