# Possible expansions include:
    # Prepend/Insert/Append All (complement to prune/graft)
    # Traverse (complement to preorder/inorder/postorder)

class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    # A tail pointer is not required for the canonical singly-linked list, but
    #     it is included in this implementation because, for a mere 4 bytes of
    #     overhead, it lowers the time complexity of the append method from
    #     O(n) to O(1).
    # A range of negative indicies is valid (-1 for the tail, -self.size for
    #     the head), but these indicies are converted to their corresponding
    #     non-negative indicies before traversal.
    # When given an index that is out-of-bounds, insert will prepend or append
    #     the element accordingly; access and pop raise an exception instead.
    # Insert, remove, and pop use a "predecessor" pointer for traversal because
    #     links cannot be accessed from behind in a singly-linked list. It
    #     points to head initially, which means that only [1:] can be explored
    #     within the loop; head must be explored seperately.

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
        node_strings = []
        current = self.head
        for _ in range(self.size):
            node_strings.append(str(current.data) + " --> ")
            current = current.next
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
        raise ValueError('Data not in list.')

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
            temp = SLLNode(data)
            temp.next = predecessor.next
            predecessor.next = temp
            self.size += 1

    # Time: O(1)
    # Auxiliary Space: O(1)
    def prepend(self, data):
        temp = SLLNode(data)
        if self.is_empty():
            self.head = temp
            self.tail = temp
        else:
            temp.next = self.head
            self.head = temp
        self.size += 1
    
    # Time: O(1) (would be O(n) without tail pointer)
    # Auxiliary Space: O(1)
    def append(self, data):
        temp = SLLNode(data)
        if self.is_empty():
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
        self.size += 1
   
    # Time: O(n)
    # Auxiliary Space: O(1)
    def remove(self, data):
        if self.is_empty():
            raise ValueError("Cannot remove from empty list.")

        if self.head.data == data:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            self.size -= 1
            return

        predecessor = self.head
        for _ in range(self.size - 1):
            if predecessor.next.data == data:
                if predecessor.next is self.tail:
                    self.tail = predecessor
                predecessor.next = predecessor.next.next
                self.size -= 1
                return
            predecessor = predecessor.next
        raise ValueError("Data not in list.")

    # Time: O(n)
    # Auxiliary Space: O(1)
    def pop(self, index=-1):
        if self.is_empty():
            raise IndexError("Cannot pop empty list.")

        if index < 0:
            index += self.size
        if index < 0 or index >= self.size:
            raise IndexError("Index not in range.")

        if index == 0:
            data = self.head.data
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            self.size -= 1
            return data
        
        predecessor = self.head
        for _ in range(index - 1):
            predecessor = predecessor.next
        if predecessor.next is self.tail:
            self.tail = predecessor
        data = predecessor.next.data
        predecessor.next = predecessor.next.next
        self.size -= 1
        return data

class CircularSinglyLinkedList:
    # This implementation needs only a tail pointer because tail.next always
    #     points to the head of the list (and append remains O(1)).
    # Every signed index is valid because circular lists are closed loops that
    #     never end; to prevent unnecessary looping, indicies are reduced
    #     before traversal.
    # Prepend and append produce circular lists of the same relative order;
    #     the only difference is the position of the tail pointer.
    # Nodes cannot be appended to a circular list using insert; any index
    #     that is a multiple of self.size will be reduced to 0, resulting
    #     in a prepend operation.
    # Insert, remove, and pop use a "predecessor" pointer for traversal because
    #     links cannot be accessed from behind in a singly-linked list. It
    #     points to tail initially, which means that the whole list can be
    #     explored within the loop, from head to tail, in order.
    # In a circular list, every element is technically a middle element.

    # Time: O(n) (but, practically, O(1) when data is not given)
    # Auxiliary Space: O(1)
    def __init__(self, data=[]):
        self.tail = None
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
        current = self.tail.next
        for _ in range(self.size - 1):
            data_string = str(current.data)
            node_strings.append(data_string + " --> ")
            character_total += (len(data_string) + 5)
            current = current.next

        data_string = str(current.data)
        node_strings.append(data_string + " --\n")
        character_total += (len(data_string) + 3)

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
        current = self.tail.next
        for _ in range(index):
            current = current.next
        return current.data

    # Time: O(n)
    # Auxiliary Space: O(1)
    def search(self, data):
        if not self.is_empty():
            current = self.tail.next
            for i in range(self.size):
                if current.data == data:
                    return i
                current = current.next
        raise ValueError('Data not in list.')

    # Time: O(n)
    # Auxiliary Space: O(1)
    def insert(self, index, data):
        if self.is_empty():
            temp = SLLNode(data)
            self.tail = temp
            temp.next = temp
            self.size += 1
            return

        index %= self.size

        predecessor = self.tail
        for _ in range(index):
            predecessor = predecessor.next 
        temp = SLLNode(data)
        temp.next = predecessor.next
        predecessor.next = temp
        self.size += 1

    # Time: O(1)
    # Auxiliary Space: O(1)
    def prepend(self, data):
        self.insert(0, data)
    
    # Time: O(1)
    # Auxiliary Space: O(1)
    def append(self, data):
        temp = SLLNode(data)
        if self.is_empty():
            self.tail = temp
            temp.next = temp
        else:
            temp.next = self.tail.next
            self.tail.next = temp
            self.tail = temp
        self.size += 1

    # Time: O(n)
    # Auxiliary Space: O(1)
    def remove(self, data):
        if self.is_empty():
            raise ValueError("Cannot remove from empty list.")

        predecessor = self.tail
        for _ in range(self.size):
            if predecessor.next.data == data:
                if self.size == 1:
                    self.tail = None
                elif predecessor.next is self.tail:
                    self.tail = predecessor
                predecessor.next = predecessor.next.next
                self.size -= 1
                return
            predecessor = predecessor.next
        raise ValueError("Data not in list.")

    # Time: O(n)
    # Auxiliary Space: O(1)
    def pop(self, index=-1):
        if self.is_empty():
            raise IndexError("Cannot pop empty list.")

        index %= self.size

        predecessor = self.tail
        for _ in range(index):
            predecessor = predecessor.next
        if self.size == 1:
            self.tail = None
        elif predecessor.next is self.tail:
            self.tail = predecessor
        data = predecessor.next.data
        predecessor.next = predecessor.next.next
        self.size -= 1
        return data

