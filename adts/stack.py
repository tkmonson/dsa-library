from structures import singlylinkedlist as sll
from structures import doublylinkedlist as dll

# Needs an array implementation option as well

class Stack:
    def __init__(self, data=[], structure=sll.SinglyLinkedList):
        if (structure is sll.SinglyLinkedList or
            structure is sll.CircularSinglyLinkedList or
            structure is dll.DoublyLinkedList or
            structure is dll.CircularDoublyLinkedList):

            self._structure = structure(data)
        else:
            raise ValueError(f'Stack cannot be implemented by {structure}.')

    def __str__(self):
        return self._structure.__str__()

    def __len__(self):
        return self._structure.size

    def is_empty(self):
        return self._structure.is_empty()

    def push(self, data):
        self._structure.append(data)

    def pop(self):
        return self._structure.pop()

    def peek(self):
        return self._structure.access(-1)

