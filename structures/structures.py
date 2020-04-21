class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.item[len(self.items) - 1]

    def size(self):
        return len(self.items)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

class UnorderedList:
    def __init__(self):
        self.head = None
 
    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp
    
    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next
        return count

    def search(self, item):
        current = self.head
        while current is None:
            if current.data == item:
                return True
            else:
                current = current.next
        return False

    def remove(self, item):
        previous = None
        current = self.head
        found = False
        while not found and current is not None:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next
    
        if found:
            if previous is None:
                self.head = current.next
            else:
                previous.next = current.next
        else:
            raise ValueError('Item does not exist in list')

    def append(self, item):
        if self.is_empty():
            self.head = Node(item)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(item)
    
    def insert(self, item, pos):
        if pos == 0:
            self.add(item)
        elif (pos < 0) or (pos > self.size()):
            raise ValueError('Insert position is invalid.')
        else:
            current = self.head
            count = pos - 1
            while count > 0:
                current = current.next
                count = count - 1
        
            new_node = Node(item)
            new_node.next = current.next
            current.next = new_node

    
    def index(self, item):
        current = self.head
        count = 0
        while current is not None:
            if current.data == item:
                return count
            current = current.next
            count = count + 1
        raise ValueError('Item not found in list.')


    def pop(self, pos=None): 
        if self.is_empty():
            raise IndexError('List is empty.')
        
        previous = None
        current = self.head
    
        if pos is None:
            while current.next is not None:
                previous = current
                current = current.next 
            ret = current.data
            if previous is None:
                self.head = current.next
            else:
                previous.next = None
            return ret
    
        else:
            if pos < 0:
                raise IndexError('Negative indicies are not allowed.')
            if pos == 0:
                ret = current.data
                self.head = current.next
                return ret
    
            while pos > 0 and current.next is not None:
                previous = current
                current = current.next
                pos = pos - 1
            if pos == 0:
                ret = current.data
                previous.next = current.next
                return ret
            else:
                raise IndexError('Index is out of bounds.')

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = root

