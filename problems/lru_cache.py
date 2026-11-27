'''
LRU Cache (#146)

Implement a data structure that satisfies the requirements of a Least Recently
Used (LRU) cache:

    * LRUCache(capacity: int) -> LRUCache
        Initialize the LRU cache with a positive capacity.

    * get(key: int) -> int
        Return the value associated with the key, if the key exists in the
        cache. Otherwise, return -1.

    * put(key: int, value: int) -> None
        Update the value associated with the key, if the key exists in the
        cache. Otherwise, add the key-value pair to the cache. If the number of
        keys in the cache exceeds the capacity due to this addition, remove the
        least recently used key.

The `get` and `put` operations must run in O(1) time.
'''

from collections import OrderedDict

class ListNode:
    def __init__(self, key: int = 0, val: int = 0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = {}
        self._head = ListNode()  # head.next is the least recently used
        self._tail = ListNode()  # tail.prev is the most recently used
        self._head.next, self._tail.prev = self._tail, self._head

    def _remove(self, node: ListNode) -> None:
        node.prev.next, node.next.prev = node.next, node.prev

    def _append(self, node: ListNode) -> None:
        node.prev, node.next = self._tail.prev, self._tail
        self._tail.prev.next = self._tail.prev = node

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1
        node = self._cache[key]
        self._remove(node)
        self._append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            self._remove(self._cache[key])
        node = self._cache[key] = ListNode(key, value)
        self._append(node)
        if len(self._cache) > self._capacity:
            lru = self._head.next
            self._remove(lru)
            del self._cache[lru.key]


class LRUCache2:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1
        self._cache.move_to_end(key)
        return self._cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            self._cache.move_to_end(key)
        self._cache[key] = value
        if len(self._cache) > self._capacity:
            self._cache.popitem(last=False)


if __name__ == '__main__':
    lru = LRUCache2(5)
    lru.put(3, 'dog')
    lru.put(4, 'cat')
    lru.put(5, 'bird')
    lru.put(6, 'goat')
    lru.put(3, 'dog')
    lru.put(7, 'mouse')
    print(lru._cache)
    lru.put(8, 'horse')
    print(lru._cache)

'''
The need for access via key in O(1) time implies the need for a hash map
structure. The need to keep track of a least recently used element implies the
need for a list structure that orders elements by how recently they have been
used. The need to update an element to most recently used whenever it is used
while maintaining O(1) time implies the need for a linked list structure, which
has O(1) remove and append operations. Thus, the LRU cache must make use of a
hash map and a linked list.
'''
