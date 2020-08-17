from structures import singlylinkedlist as sll
from structures import doublylinkedlist as dll

# Needs an array implementation option as well

class Deque:
    def __init__(self, data=[], structure=dll.DoublyLinkedList):
        if (structure is sll.SinglyLinkedList or
            structure is sll.CircularSinglyLinkedList or
            structure is dll.DoublyLinkedList or
            structure is dll.CircularDoublyLinkedList):

            self._structure = structure(data)
        else:
            raise ValueError(f'Deque cannot be implemented by {structure}.')

    def __str__(self):
        return self._structure.__str__()

    def is_empty(self):
        return self._structure.is_empty()

    def size(self):
        return self._structure.size

    def enqueue_left(self, data):
        self._structure.prepend(data)

    def enqueue_right(self, data):
        self._structure.append(data)

    def dequeue_left(self):
        return self._structure.pop(0)

    def dequeue_right(self):
        return self._structure.pop()

    def peek_left(self):
        return self._structure.access(0)

    def peek_right(self):
        return self._structure.access(-1)

