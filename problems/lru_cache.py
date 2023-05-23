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
    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self._cache = {}
        self._capacity = capacity
        self._lru = None
        self._mru = None

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1
        self._update_to_most_recent(key)
        return self._cache[key][0]

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            self._update_to_most_recent(key)
            self._cache[key][0] = value
        else:
            node = ListNode(key)
            if not len(self._cache):
                self._lru = node
            else:
                self._mru.next = node
                node.prev = self._mru
            self._mru = node

            if len(self._cache) == self._capacity:
                del self._cache[self._lru.val]
                self._lru = self._lru.next
                self._lru.prev = None
            self._cache[key] = [value, node]

    def _update_to_most_recent(self, key):
        node = self._cache[key][1]
        if node is self._mru:
            return
        if node is self._lru:
            self._lru = self._lru.next

        if node.prev:
            node.prev.next = node.next
        node.next.prev = node.prev

        self._mru.next = node
        node.prev = self._mru
        node.next = None
        self._mru = self._mru.next


class LRUCache2:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1
        self._cache[key] = self._cache.pop(key)
        return self._cache[key]

    def put(self, key: int, value: int) -> None:
        if key not in self._cache and len(self._cache) >= self._capacity:
            self._cache.popitem(last=False)
        if key in self._cache:
            self._cache.pop(key)
        self._cache[key] = value

'''
The need for access via key in O(1) time implies the need for a hash map
structure. The need to keep track of a least recently used element implies the
need for a list structure that orders elements by how recently they have been
used. The need to update an element to most recently used whenever it is used
while maintaining O(1) time implies the need for a linked list structure, which
has O(1) remove and append operations. Thus, the LRU cache must make use of a
hash map and a linked list.
'''

