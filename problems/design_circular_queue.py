'''
Design Circular Queue (#622)

Design your implementation of the circular queue. The circular queue is a
linear data structure in which the operations are performed based on the FIFO
principle, and the last position is connected back to the first position to
make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces
in front of the queue. In a normal queue, once the queue becomes full, we
cannot insert the next element even if there is a space in front of the queue.
But using the circular queue, we can use the space to store new values.

Implement the MyCircularQueue class:

    - MyCircularQueue(k): Initializes the object with the size of the queue to
                          be k.
    - int Front(): Gets the front item from the queue. If the queue is empty,
                   return -1.
    - int Rear(): Gets the last item from the queue. If the queue is empty,
                  return -1.
    - boolean enQueue(int value): Inserts an element into the circular queue.
                                  Return true if the operation is successful.
    - boolean deQueue(): Deletes an element from the circular queue. Return
                         true if the operation is successful.
    - boolean isEmpty(): Checks whether the circular queue is empty or not.
    - boolean isFull(): Checks whether the circular queue is full or not.
'''

class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [0 for _ in range(k)]
        self.capacity = k
        self.front = -1
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        elif self.isEmpty():
            self.front = 0
            self.rear = 0
            self.q[self.rear] = value
        else:
            self.rear += 1
            self.rear %= self.capacity
            self.q[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        elif self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1
            self.front %= self.capacity
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.q[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.q[self.rear]

    def isEmpty(self) -> bool:
        return self.front == self.rear == -1

    def isFull(self) -> bool:
        return (self.rear + 1) % self.capacity == self.front

'''
Unless you are keeping track of the queue's size, you need to have a sentinel
value (such as -1) for front and rear that denotes an empty array, because
front == rear denotes a queue with one element.
'''

if __name__ == '__main__':
    q = MyCircularQueue(3)
    print(q.enQueue(1))
    print(q.enQueue(2))
    print(q.enQueue(3))
    print(q.enQueue(4))
    print(q.Rear())
    print(q.isFull())
    print(q.deQueue())
    print(q.enQueue(4))
    print(q.Rear())
    print(q.q)

'''
When implementing a queue with a linear array, dequeuing elements leaves empty
space at the front of the array that can only be used by performing an O(n)
operation where all elements are shifted forward. With a circular queue, just
wrap the pointers around to the front of the array.
'''
