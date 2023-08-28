'''
Time Based Key-Value Store (#981)

Design a time-based key-value data structure that can store multiple values for
the same key at different timestamps and retrieve the key's value at a certain
timestamp. Implement the `TimeMap` class:
    * TimeMap: Initializes the data structure
    * set: Stores the key `key` with the value `value` at the given time
           `timestamp`
    * get: Returns the value associated with `key` at a given `timestamp`. If
           no value is associated with `key` at `timestamp`, return the value
           associated with `key` at the largest timestamp less than
           `timestamp`. If no such timestamp exists, return ''.

All timestamps passed to `set` are strictly increasing.
'''

from collections import defaultdict
from bisect import bisect

class TimeMap:
    def __init__(self):
        self.time = defaultdict(list)
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[key].append(timestamp)
        self.data[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        i = bisect(self.time[key], timestamp)
        return self.data[key][i - 1] if i > 0 else ''


if __name__ == '__main__':
    t = TimeMap()
    t.set("love", "high", 10)
    t.set("love", "low", 20)
    t.get("love", 5)
    t.get("love", 10)
    t.get("love", 15)
    t.get("love", 20)
    t.get("love", 25)

'''
I initially tried to use the structure dict(key, dict(timestamp, value)), but
it turns out that using structures dict(key, list(values)) and
dict(key, list(timestamps)) is more convenient (because you need to search the
collection of timestamps, so it helps if it is already a list).

Because timestamps are added to the structure in a strictly increasing way,
their collection is sorted. This implies that binary search is an efficient way
to find the largest timestamp that is less than the given timestamp.
'''

