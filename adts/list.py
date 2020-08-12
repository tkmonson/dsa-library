from structures import singlylinkedlist as sll
from structures import doublylinkedlist as dll

# Needs an array implementation option as well

class List:
    def __init__(self, data=[], structure=dll.DoublyLinkedList):
        if (structure is sll.SinglyLinkedList or
            structure is sll.CircularSinglyLinkedList or
            structure is dll.DoublyLinkedList or
            structure is dll.CircularDoublyLinkedList):

            self._structure = structure(data)
        else:
            raise ValueError(f'List cannot be implemented by {structure}.')
    
    def __str__(self):
        return self._structure.__str__()

    def is_empty(self):
        return self._structure.is_empty()

    def size(self):
        return self._structure.size

    def access(self, index):
        return self._structure.access(index)

    def search(self, data):
        return self._structure.access(data)

    def insert(self, index, data):
        self._structure.insert(index, data)

    def prepend(self, data):
        self._structure.prepend(data)

    def append(self, data):
        self._structure.append(data)

    def remove(self, data):
        self._structure.remove(data)

    def pop(self, index):
        return self._structure.pop(index)

