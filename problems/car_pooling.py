'''
Car Pooling (#1094)

There is a car with `capacity` empty seats. The vehicle only drives east (i.e.,
it cannot turn around and drive west). You are given the integer `capacity` and
an array `trips` where `trips[i] = [numPassengers_i, from_i, to_i]` indicates
that the ith trip has `numPassengers_i` passengers and the locations to pick
them up and drop them off are `from_i and `to_i` respectively. The locations
are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all
the given trips, or false otherwise.

1 <= trips.length <= 1000
1 <= numPassengers_i <= 100
0 <= from_i < to_i <= 1000
1 <= capacity <= 10^5
'''

import heapq

# Time: O(n)
# Auxiliary space: O(1) (technically worse than O(n) in this case)
def car_pooling(trips: list[list[int]], capacity: int) -> bool:
    stops = [0] * 1001
    for passengers, start, end in trips:
        stops[start] += passengers
        stops[end] -= passengers
        
    curr = 0
    for change in stops:
        curr += change
        if curr > capacity:
            return False
    return True

'''
Similar to the sweep line algorithm below, but this avoids the heapsort by
creating a big array for the brackets instead. 
'''

# Time: O(nlogn)
# Auxiliary space: O(n)
def car_pooling2(trips: list[list[int]], capacity: int) -> bool:
    heap = []
    for np, start, end in trips:
        heapq.heappush(heap, (start, np))
        heapq.heappush(heap, (end, -np))

    curr = 0
    while heap:
        curr += heapq.heappop(heap)[1]
        if curr > capacity:
            return False

    return True

'''
This is a sweep line algorithm. Split the intervals into left and right
brackets and put them in a heap. Left brackets add passengers, right brackets
subtract passengers. This is a good choice when you need to traverse a space
with many overlapping intervals.
'''

if __name__ == '__main__':
    trips = [[2, 1, 5], [3, 3, 7]]
    capacity = 4
    print(car_pooling(trips, capacity))
