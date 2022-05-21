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

