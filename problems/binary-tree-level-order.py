'''
Binary Tree Level Order Traversal (#102)

Given the root of a binary tree, return the level order traversal of its nodes'
values (a list of lists, where each list in the list represents a level).
'''

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: TreeNode | None) -> list[list[int]]:
    if root is None:
        return []

    level_list = [[root]]
    while level_list[-1]:
        next_level = []
        for i in range(len(level_list[-1])):
            node = level_list[-1][i]
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
            level_list[-1][i] = level_list[-1][i].val
        level_list.append(next_level)

    return level_list[:-1]


def level_order2(root: TreeNode | None) -> list[list[int]]:
    if root is None:
        return []

    queue = deque()
    level_list = []
    queue.append(root)
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left != None:
                queue.append(node.left)
            if node.right != None:
                queue.append(node.right)
        level_list.append(level)

    return level_list

'''
To traverse a binary tree in level order, you put the root into a queue. Then,
you dequeue a node, enqueue its non-null children, and repeat until the queue
is empty. This problem is slightly different because the nodes not only have to
be in order, but they also have to be separated into their levels. To do this,
you process all of the nodes in the queue (put them into a level) before
processing their children (putting them into the next level).

Two solutions are given. One is more traditional, where the queue and the list
of levels are separate. The other combines the two, using the current lowest
level as the queue and converting nodes to values as they are processed.
'''

