from dsa_library.structures import singlylinkedlist as sll

class MyList:
    def __init__(self):
        self.list = sll.SinglyLinkedList()
    
    def append(self, val):
        self.list.append(val)

