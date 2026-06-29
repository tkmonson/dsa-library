'''
Open the Lock (#752)

You have a lock in front of you with 4 circular wheels. Each wheel has 10
slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate
freely and wrap around: for example we can turn '9' to be '0', or '0' to be
'9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4
wheels.

You are given a list of dead ends, meaning if the lock displays any of these
codes, the wheels of the lock will stop turning and you will be unable to open
it.

Given a target representing the value of the wheels that will unlock the lock,
return the minimum total number of turns required to open the lock, or -1 if it
is impossible.
'''

from collections import deque

# Time: O(1) (not dependent on input)
# Auxiliary space: O(d) (set with deadends)
def open_lock(deadends: list[str], target: str):
    rot = {
        '0': ('9', '1'),
        '1': ('0', '2'),
        '2': ('1', '3'),
        '3': ('2', '4'),
        '4': ('3', '5'),
        '5': ('4', '6'),
        '6': ('5', '7'),
        '7': ('6', '8'),
        '8': ('7', '9'),
        '9': ('8', '0')
    }

    visited = set(deadends)
    queue = deque([('0000', 0)])

    while queue:
        combo, dist = queue.popleft()

        if combo in visited:
            continue
        visited.add(combo)

        if combo == target:
            return dist

        wheels = list(combo)
        for i in range(4):
            temp = wheels[i]
            for d in rot[wheels[i]]:
                wheels[i] = d
                queue.append((''.join(wheels), dist + 1))
            wheels[i] = temp

    return -1

'''
At each step, you can make one of eight moves. This can be modeled as a graph,
where the verticies are lock states that are connected if they differ by one
wheel rotation. Because we are looking for the minimum number of turns, do a
BFS of the lock space, starting from 0000. Visited nodes are "deadends" during
the search, so deadends can start in the visited set.
'''

if __name__ == '__main__':
    deadends = ["0201","0101","0102","1212","2002"]
    target = "0202"
    print(open_lock(deadends, target))
