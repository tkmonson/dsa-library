from structures import binaryheap as bh

class PriorityQueue:
    def __init__(self, data=[], structure=bh.ImplicitBinaryMinHeap):
        if (structure is bh.ImplicitBinaryMinHeap or
            structure is bh.ImplicitBinaryMaxHeap):

            self._structure = structure(data)
        else:
            raise ValueError(f'Priority queue cannot be implemented by {structure}.')

    def __str__(self):
        return self._structure.__str__()

    def __len__(self):
        return self._structure.size()

    def is_empty(self):
        return self._structure.is_empty()

    def insert(self, data, priority):
        return self._structure.insert((priority, data))

    def pull(self):
        if type(self._structure) is bh.ImplicitBinaryMinHeap:
            return self._structure.extract_min()
        return self._structure.extract_max()

    def peek(self):
        if type(self._structure) is bh.ImplicitBinaryMinHeap:
            return self._structure.get_min()
        return self._structure.get_max()

    def prioritize(self, data, priority):
        if type(self._structure) is bh.ImplicitBinaryMinHeap:
            return self._structure.decrease_key(data, priority)
        return self._structure.increase_key(data, priority)

'''
The following code is fully functional and correct:

class PriorityQueue:
    def __init__(self, items=[]):
        self.pq = items
        self.index = {t: i for (i, [_, t]) in enumerate(items)}
        self._heapify()

    def __len__(self):
        return len(self.pq)

    def __contains__(self, task):
        return task in self.index

    def insert(self, task, priority=0):
        self.pq.append([priority, task])
        self._sift_up(len(self.pq) - 1)

    def pop(self):
        if len(self.pq):
            self.pq[0], self.pq[-1] = self.pq[-1], self.pq[0]
            self.index[self.pq[0][1]] = 0
            _, task = self.pq.pop()
            del self.index[task]
            self._sift_down(0)
            return task
        raise KeyError('Pop from empty priority queue')

    def decrease_key(self, task, priority=0):
        if self.get_priority(task) <= priority:
            raise ValueError('New priority is not less than old priority')
        c = self.index[task]
        self.pq[c][0] = priority
        self._sift_up(c)

    def get_priority(self, task):
        if task not in self.index:
            raise KeyError('Task not in priority queue')
        return self.pq[self.index[task]][0]

    def _heapify(self):
        for p in range(len(self.pq) // 2 - 1, -1, -1):
            self._sift_down(p)

    def _sift_up(self, c):
        p = (c - 1) // 2
        if c > 0 and self.pq[c] < self.pq[p]:
            self._swap(c, p)
            self._sift_up(p)

    def _sift_down(self, p):
        n = len(self.pq)
        cl, cr = 2 * p + 1, 2 * p + 2
        if cl >= n:
            return
        if cr >= n:
            cr = cl
        c = cl if self.pq[cl] < self.pq[cr] else cr

        if self.pq[c] < self.pq[p]:
            self._swap(c, p)
            self._sift_down(c)

    def _swap(self, i, j):
        self.index[self.pq[i][1]] = j
        self.index[self.pq[j][1]] = i
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
'''

