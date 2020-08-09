class DLLNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    # A range of negative indicies is valid (-1 for the tail, -self.size for
    #     the head), but these indicies are converted to their corresponding
    #     non-negative indicies before traversal.
    # When given an index that is out-of-bounds, insert will prepend or append
    #     the element accordingly; access and pop raise an exception instead.
    # Insert can use either a "predecessor" or a "successor" pointer for
    #     traversal because a "temp" node can be inserted from an antecedent or
    #     subsequent position in a doubly-linked list. A predecessor is used in
    #     this implementation for consistency, and it points to head initially,
    #     which means that only [1:] can be explored within the loop; head must
    #     be explored separately.
    # Remove and pop use a "current" pointer for traversal because links can be
    #     accessed on either side of the node to be removed or popped. It
    #     points to head initially and explores the whole list in order.

    # Time: O(n) (but, practically, O(1) when data is not given)
    # Auxiliary Space: O(1) 
    def __init__(self, data=[]):
        self.head = None
        self.tail = None
        self.size = 0
        for el in data:
            self.append(el)

    # Time: O(n)
    # Auxiliary Space: O(n)
    def __str__(self):
        if self.is_empty():
            return ""

        node_strings = ["<-- "]
        current = self.head
        for _ in range(self.size - 1):
            node_strings.append(str(current.data) + " <--> ")
            current = current.next

        node_strings.append(str(current.data) + " -->")
        return ''.join(node_strings)
 
    # Time: O(1)
    # Auxiliary Space: O(1)
    def is_empty(self):
        return self.size == 0

    # Time: O(n)
    # Auxiliary Space: O(1)
    def access(self, index):
        if index < 0:
            index += self.size

        if index >= 0 and index < self.size:
            current = self.head
            for _ in range(index):
                current = current.next
            return current.data
        raise IndexError("Index not in range.")

    # Time: O(n)
    # Auxiliary Space: O(1)
    def search(self, data):
        current = self.head
        for i in range(self.size):
            if current.data == data:
                return i
            current = current.next
        raise ValueError("Data not in list.")

    # Time: O(n) in general, O(1) for head and tail
    # Auxiliary Space: O(1)
    def insert(self, index, data):
        if index < 0:
            index += self.size

        if index <= 0:
            self.prepend(data)
        elif index >= self.size:
            self.append(data)
        else:
            predecessor = self.head
            for _ in range(index - 1):
                predecessor = predecessor.next 
            temp = DLLNode(data)
            temp.next = predecessor.next
            predecessor.next.prev = temp
            temp.prev = predecessor
            predecessor.next = temp
            self.size += 1

    # Time: O(1)
    # Auxiliary Space: O(1)
    def prepend(self, data):
        temp = DLLNode(data)
        if self.is_empty():
            self.head = temp
            self.tail = temp
        else:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
        self.size += 1

    # Time: O(1)
    # Auxiliary Space: O(1)
    def append(self, data):
        temp = DLLNode(data)
        if self.is_empty():
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            temp.prev = self.tail
            self.tail = temp
        self.size += 1

    # Time: O(n)
    # Auxiliary Space: O(1)
    def remove(self, data):
        if self.is_empty():
            raise ValueError("Cannot remove from empty list.")

        current = self.head
        for _ in range(self.size):
            if current.data == data:
                if self.size == 1:
                    self.head = None
                    self.tail = None
                elif current is self.head:
                    self.head = self.head.next
                    self.head.prev = None
                elif current is self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None
                else:
                    current.next.prev = current.prev
                    current.prev.next = current.next
                self.size -= 1
                return
            current = current.next
        raise ValueError("Data not in list.")

    # Time: O(n)
    # Auxiliary Space: O(1)
    def pop(self, index=0):
        if self.is_empty():
            raise IndexError("Cannot pop empty list.")

        if index < 0:
            index += self.size
        if index < 0 or index >= self.size:
            raise IndexError("Index not in range.")

        current = self.head
        for _ in range(index):
            current = current.next
        if self.size == 1:
            self.head = None
            self.tail = None
        elif current is self.head:
            self.head = self.head.next
            self.head.prev = None
        elif current is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current.next.prev = current.prev
            current.prev.next = current.next
        self.size -= 1
        return current.data

class CircularDoublyLinkedList:
    # This implementation needs only a head pointer because head.prev always
    #     points to the tail of the list (and append remains O(1)).
    # Every signed index is valid because circular lists are closed loops that
    #     never end; to prevent unnecessary looping, indicies are reduced
    #     before traversal.
    # Prepend and append produce circular lists of the same relative order;
    #     the only difference is the position of the head pointer.
    # Nodes cannot be appended to a circular list using insert; any index
    #     that is a multiple of self.size will be reduced to 0, resulting
    #     in a prepend operation.
    # Insert can use either a "predecessor" or a "successor" pointer for
    #     traversal because a "temp" node can be inserted from an antecedent or
    #     subsequent position in a doubly-linked list. A predecessor is used in
    #     this implementation for consistency, and it points to head initially,
    #     which means that only [1:] can be explored within the loop; head must
    #     be explored separately.
    # Remove and pop use a "current" pointer for traversal because links can be
    #     accessed on either side of the node to be removed or popped. It
    #     points to head initially and explores the whole list in order.
    # In a circular list, every element is technically a middle element.

    def __init__(self, data=[]):
        self.head = None
        self.size = 0
        for el in data:
            self.append(el)

    # Time: O(n)
    # Auxiliary Space: O(n)
    def __str__(self):
        if self.is_empty():
            return ""

        node_strings = ["--> "]
        character_total = 4
        current = self.head
        for _ in range(self.size - 1):
            data_string = str(current.data)
            node_strings.append(data_string + " <--> ")
            character_total += (len(data_string) + 6)
            current = current.next 

        data_string = str(current.data)
        node_strings.append(data_string + " <--\n")
        character_total += (len(data_string) + 4)

        circular_link = "\\" + ''.join(["_" * (character_total - 2)]) + "/"
        node_strings.append(circular_link)
        return ''.join(node_strings)

    # Time: O(1)
    # Auxiliary Space: O(1)
    def is_empty(self):
        return self.size == 0

    # Time: O(n)
    # Auxiliary Space: O(1)
    def access(self, index):
        if self.is_empty():
            raise IndexError("Cannot access an empty list.")
        index %= self.size
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    # Time: O(n)
    # Auxiliary Space: O(1)
    def search(self, data):
        if not self.is_empty():
            current = self.head
            for i in range(self.size):
                if current.data == data:
                    return i
                current = current.next
        raise ValueError('Data not in list.')

    # Time: O(n) in general, O(1) for head and tail
    # Auxiliary Space: O(1)
    def insert(self, index, data):
        if self.is_empty():
            temp = DLLNode(data)
            self.head = temp
            temp.next = temp
            temp.prev = temp
            self.size += 1
            return

        index %= self.size

        if index == 0:
            self.prepend(data)
        else:
            predecessor = self.head
            for _ in range(index - 1):
                predecessor = predecessor.next 
            temp = DLLNode(data)
            temp.next = predecessor.next
            predecessor.next.prev = temp
            temp.prev = predecessor
            predecessor.next = temp
            self.size += 1

    # Time: O(1)
    # Auxiliary Space: O(1)
    def prepend(self, data):
        temp = DLLNode(data)
        if self.is_empty():
            self.head = temp
            temp.next = temp
            temp.prev = temp
        else:
            temp.prev = self.head.prev
            self.head.prev.next = temp
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
        self.size += 1
    
    # Time: O(1)
    # Auxiliary Space: O(1)
    def append(self, data):
        self.prepend(data)
        self.head = self.head.next

    # Time: O(n)
    # Auxiliary Space: O(1)
    def remove(self, data):
        if self.is_empty():
            raise ValueError("Cannot remove from empty list.")

        current = self.head
        for _ in range(self.size):
            if current.data == data:
                if self.size == 1:
                    self.head = None
                elif current is self.head:
                    self.head = self.head.next
                current.next.prev = current.prev
                current.prev.next = current.next
                self.size -= 1
                return
            current = current.next
        raise ValueError("Data not in list.")

    # Time: O(n)
    # Auxiliary Space: O(1)
    def pop(self, index=0):
        if self.is_empty():
            raise IndexError("Cannot pop empty list.")

        index %= self.size

        current = self.head
        for _ in range(index):
            current = current.next
        if self.size == 1:
            self.head = None
        elif current is self.head:
            self.head = self.head.next
        current.next.prev = current.prev
        current.prev.next = current.next
        self.size -= 1
        return current.data

