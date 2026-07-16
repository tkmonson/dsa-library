'''
Rotate Array (#189)

Given an integer array `nums`, rotate the array to the right by `k` steps,
where `k` is non-negative.
'''

import math
from collections import deque

# Time: O(n)
# Auxiliary space: O(1)
def rotate_gcd(nums: list[int], k: int) -> None:
    n = len(nums)
    k %= n
    gcd = math.gcd(k, n)
    for i in range(gcd):
        j = i
        curr = nums[j]
        while True:
            next_j = (j + k) % n
            temp = nums[next_j]
            nums[next_j] = curr
            curr = temp

            j = next_j
            if j == i:
                break

'''
This is the juggling algorithm. I came up with this solution myself after
drawing out examples and looking at them for a long time. This was my thought
process:

I tried different k values with n = 7; the array rotated correctly each time.

    a = [1 2 3 4 5 6 7], k = 3
    1 -> 4 -> 7 -> 3 -> 6 -> 2 -> 5 -> 1

This was not the case for n = 6:

             *   *   *                   *     *
    k = 2    1 2 3 4 5 6        k = 3    1 2 3 4 5 6

             *       *                   *         *
    k = 4    1 2 3 4 5 6        k = 5    1 2 3 4 5 6
                 *                         * * * *

Each cycle correctly rotates the elements within it. A cycle can be shifted to
the right by one and run again, until all elements are rotated. How many
independent cycles are there? It definitely depends on n and k.

Let f(n, k) be the number of cycles:
f(6, 2) = 2, f(6, 3) = 3, f(6, 4) = 2, f(6, 5) = 1

It seems like it is some factor of n and k. Is it the greatest common divisor?
Yes, it is, wow. So if you run the cycle and shift it to the right by one
gcd(n, k) times, you will rotate the array by k.

--

Why does this work? Here is a more formal proof:

In a cycle, the possible values for j are i, (i + k) % n, (i + 2k) % n,
(i + 3k) % n, ..., (i + m * k) % n. The cycle terminates when i = j:

(i + m * k) % n = i  =>  m * k % n = 0

The first time you arrive back at the beginning of the cycle is the first time
you can divide m * k by n. Thus, at this point, m * k is the smallest number
divisible by both n and k. m * k is the least common multiple of n and k.

m * k = lcm(n, k). The cycle spans lcm(n, k) elements, but it only rotates
lcm(n, k) / k elements. Let x be the number of independent cycles required to
rotate the array by k (to rotate all n elements).

x * lcm(n, k) / k = n  =>  x = (n * k) / lcm(n, k).

By definition, x = gcd(n, k). The GCD of two numbers can be calculated by
dividing their product by their least common multiple.
'''

# Time: O(n)
# Auxiliary space: O(1)
def rotate(nums: list[int], k: int) -> None:
    n = len(nums)
    k %= n
    for i in range(n // 2):
        nums[i], nums[n - 1 - i] = nums[n - 1 - i], nums[i]
    for i in range(k // 2):
        nums[i], nums[k - 1 - i] = nums[k - 1 - i], nums[i]
    for i in range((n - k) // 2):
        nums[k + i], nums[n - 1 - i] = nums[n - 1 - i], nums[k + i]

'''
If you rotate by n, you will arrive back at the initial state. So if k > n, k
should be reduced to k % n.

Reverse the whole array
Reverse the first k elements
Reverse the last (n - k) elements
'''

# Time: O(n)
# Auxiliary space: O(k)
def rotate2(nums: list[int], k: int) -> None:
    n = len(nums)
    k %= n
    k_arr = []
    for i in range(k):
        k_arr.append(nums[n - k + i])
    for i in range(n - k - 1, -1, -1):
        nums[i + k] = nums[i]
    for i in range(k):
        nums[i] = k_arr[i]

'''
Store the last k elements separately
Shift the first (n - k) elements to the right by k
Overwrite the first k elements with the k elements stored separately
'''

# Time: O(n)
# Auxiliary space: O(n)
def rotate3(nums: list[int], k: int) -> None:
    d = deque(nums)
    for _ in range(k):
        d.appendleft(d.pop())
    for i in range(len(nums)):
        nums[i] = d[i]


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6]
    k = 3
    rotate_gcd(nums, k)
    print(nums)
