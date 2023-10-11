'''
Find K Closest Elements (#658)

Given a sorted integer array and two integers `k` and `x`, return the `k`
closest integers to `x` in the array in ascending order.

An integer `a` is closer to `x` than an integer `b` if:
    * |a - x| < |b - x|, or
    * |a - x| == |b - x| and a < b
'''

from bisect import bisect_left
from random import randint

# Time: O(log(n) + k)
# Auxiliary space: O(k)
def find_k_closest_integers(arr: list[int], k: int, x: int) -> list[int]:
    right = bisect_left(arr, x)
    left = right - 1
    for _ in range(k):
        if left < 0:
            right += 1
        elif right >= len(arr):
            left -= 1
        elif x - arr[left] <= arr[right] - x:
            left -= 1
        else:
            right += 1

    return arr[left + 1 : right]

'''
Find x or the closest element to x, add elements on either side of it in order
of increasing distance from x, return the subarray once it contains k elements.
'''

# Time: O(log(n - k))
# Auxiliary space: O(k)
def find_k_closest_integers2(arr: list[int], k: int, x: int) -> list[int]:
    left, right = 0, len(arr) - k

    while left < right:
        m = (left + right) // 2
        if x - arr[m] > arr[m + k] - x:
            left = m + 1
        else:
            right = m
    return arr[left : left + k]

'''
This method slides a k-length window around during a binary search. If the
distance between x and the leftmost element in the window is greater than the
distance between x and the element just to the right of the window, that
implies that the window should be shifted to the right (the binary search
should take the right path). Otherwise, it should be shifted to the left (the
binary search should take the left path). The binary search will find the first
element of the window that contains the k closest integers to x.
'''

if __name__ == '__main__':
    arr = [randint(0, 50) for _ in range(20)]
    arr.sort()
    arr = [0,0,1,2,3,3,4,7,7,8]
    k, x = 7, randint(0, 50)
    k, x = 3, 5
    print(f'arr: {arr}')
    print(f'k, x: {k}, {x}')
    print(f'ans: {find_k_closest_integers2(arr, k, x)}')

