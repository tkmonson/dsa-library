'''
Find the Duplicate Number (#287)

There is an array of n + 1 integers where each integer is in the range [1, n],
inclusive. The array contains only one duplicate integer, which may appear two
or more times. Return the duplicate integer in O(1) space and without modifying
the input array.
'''

# This problem has many solutions. They are sorted below in order of increasing
# time complexity, and those of the same time complexity are sorted in order of
# increasing space complexity. In short, they are sorted best to worst.

# Time: O(n)
# Auxiliary space: O(1)
def find_duplicate_tortoise_hare(nums: list[int]) -> int:
    tortoise = nums[0]
    hare = nums[0]

    while(True):
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    tortoise = nums[0]
    while(tortoise != hare):
        tortoise = nums[tortoise]
        hare = nums[hare]

    return hare

'''
This is a cycle detection algorithm called Floyd's Tortoise and Hare.

Let f(x) = nums[x]. We can use f(x) to construct the sequence x, nums[x],
nums[nums[x]], ... . Each new element in the sequence is an element in nums at
the index of the previous element. Starting at x = 0, if nums contains a
duplicate element, the sequence will produce a cyclic linked list.

                                                     1 -- 5 -- 3
               0  1  2  3  4  5  6  7  8  9          ^         |
  E.g. nums = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]    2 -- 9         |
                                                     |         |
                                                     7 -- 8 -- 6

The duplicate element is at the entrance to the cycle, so the problem is now to
find that entrance.

Let there be two pointers, tortoise and hare. Hare (hare = nums[nums[hare]])
travels twice as fast as tortoise (tortoise = nums[tortoise]). Hare enters the
cycle first and runs around the cycle. Tortoise enters the cycle, too, and hare
will catch up with it at some intersection point.

       a                   Let X be the starting point, Y be the entrance to
        /----Z--\          the cycle, and Z be the intersection point. Let the
     F  ^       |          distance between X and Y be F, the distance between
  X --- Y       |          Y and Z be a, and the length of the cycle be C.
        |       | C - a    Because the hare travels twice as fast as the
        \-------/          tortoise, 2 * d(tortoise) = d(hare).
                             => 2(F + a) = F + nC + a, where n is an integer.

Thus, you arrive at Z after F + a = nC steps. Now, we want the pointers to
arrive at Y at the same time. From Z, you can get to Y in C - a steps, and
C - a = F when n = 1. Thus, if you start tortoise from X and hare from Z and
have them run at the same speed for F steps, they will arrive at Y together.

  1. Start tortoise and hare at nums[0].
  2. Let tortoise run one node per tick and hare run two nodes per tick until
     they intersect.
  3. Start tortoise at nums[0] and hare at the intersection point.
  4. Let tortoise and hare each run one node per tick until they intersect.
  5. The node where they meet is the duplicate number.
'''

# Time: O(n)
# Auxiliary space: O(1)
def find_duplicate_sign_marking(nums: list[int]) -> int:
    for num in nums:
        num = abs(num)
        if nums[num] < 0:
            return num
        nums[num] = -nums[num]

'''
This solution modifies the input array, so it does not satisfy the constraints
of the problem. Because the elements of nums are all positive, we can use their
sign values to store state (visited or unvisited).
'''

# Time: O(n)
# Auxiliary space: O(1)
def find_duplicate_pigeonhole_iterative(nums: list[int]) -> int:
    while nums[0] != nums[nums[0]]:
        temp = nums[nums[0]]
        nums[nums[0]] = nums[0]
        nums[0] = temp
    return nums[0]

'''
This solution modifies the input array, so it does not satisfy the constraints
of the problem. This approach relies on the pigeonhole principle: if you try to
put n + 1 pigeons into n pigeonholes, at least one of the pigeonholes will
contain two or more pigeons. Position each value v at index i such that v = i.
Because there are n + 1 values and only n valid indicies, we will find a
duplicate when we attempt to put a value into an index i that is already
occupied by some value v = i. There is no v = 0, so i = 0 can contain anything.

The technique used here is cyclic sort, a sorting algorithm that factors an
unsorted array into cycles (as in a graph) that can be rotated to yield a
sorted array.

  E.g. nums = [1, 3, 4, 0, 2] can be factored into cycles (1, 3, 0) and (4, 2).
       Rotate both to the right => (0, 1, 3) and (2, 4). The array is now
       sorted => [0, 1, 2, 3, 4].

The rotation can be implemented by swapping nums[F] with nums[nums[F]], where F
is the index of the first element in a cycle, until nums[F] = F. Then, move on
to the next cycle and repeat.

  [1, 3, 4, 0, 2]
  [3, 1, 4, 0, 2]
  [0, 1, 4, 3, 2]
  [0, 1, 2, 3, 4]

In the case of this problem, let F = 0. Because nums[0] will never be 0, it
will always contain a value that belongs at a different index. When we attempt
to swap nums[0] with an equivalent nums[nums[0]], we know nums[0] is the
duplicate.
'''

# Time: O(n)
# Auxiliary space: O(n)
def find_duplicate_pigeonhole_recursive(nums: list[int]) -> int:
    def store(x):
        nonlocal nums
        if x == nums[x]:
            return x
        next = nums[x]
        nums[x] = x
        return store(next)

    return store(0)

'''
This solution modifies the input array and does not use constant space, so it
does not satisfy the constraints of the problem. This approach also uses cyclic
sort, but the rotation is implemented differently. Instead of swapping, we
traverse through the cycle, overwriting each node with the value of the
previous node. If the node to be overwritten is already at the correct index,
the cycle has been sorted and we can move on to the next cycle.

[1, 3, 4, 0, 2]
[1, 1, 4, 0, 2],  x = 3
[1, 1, 4, 3, 2],  x = 0
[0, 1, 4, 3, 2],  x = 1,  new cycle
[0, 1, 4, 3, 4],  x = 2
[0, 1, 2, 3, 4],  x = 4

In the case of this problem, start at i = 0, because nums[i] will always belong
somewhere else. We will have found a duplicate when we attempt to overwrite an
equivalent value.
'''

# Time: O(n)
# Auxiliary space: O(n) (looks like O(1) but bit length of seen grows linearly)
def find_duplicate_seen(nums: list[int]) -> int:
    seen = 0
    for num in nums:
        if seen & (1 << num):
            return num
        seen |= 1 << num

'''
This solution does not use constant space, so it does not satisfy the
constraints of the problem. Instead of using an array or set to keep track of
whether a number in [1, n] has been seen before, we can store this state in the
bits of an integer. Clever, but this still ultimately requires linear space.
'''

# Time: O(nlogn)
# Auxiliary space: O(1)
def find_duplicate_binary_search(nums: list[int]) -> int:
    n = len(nums) - 1
    lo, hi = 1, n

    while lo < hi:
        mi = (lo + hi) >> 1
        less, equal = 0, 0
        for num in nums:
            if num < mi:
                less += 1
            elif num == mi:
                equal += 1
        if equal > 1:
            return mi
        if less >= mi:
            hi = mi - 1
        else:
            lo = mi + 1

    return lo

'''
Binary searching based on value rather than index. For example, if the numbers
less than mi do not repeat, there will be mi - 1 of them or fewer. If there are
more than that, that implies that the duplicate value is less than mi and we
should narrow the search there.
'''

# Time: O(nlogn)
# Auxiliary space: O(1)
def find_duplicate_bit_count(nums: list[int]) -> int:
    n = len(nums) - 1
    nbits = n.bit_length()
    ans = 0
    for p in range(nbits):  # logn
        mask = 1 << p
        nums_count = sum(1 if num & mask else 0 for num in nums)
        base_count = sum(1 if num & mask else 0 for num in range(1, n + 1))
        if nums_count > base_count:
            ans |= mask
    return ans

'''
Which bits does the duplicate number have set to 1?
For each bit i:
    a = number of elements in nums with ith bit set to 1
    b = number of elements in [1, n] with ith bit set to 1
    If a > b, the duplicate element has its ith bit set to 1
'''

# Time: O(nlogn)
# Auxiliary space: O(n) (language-dependent, Python uses Timsort)
def find_duplicate_sort(nums: list[int]) -> int:
    n = len(nums) - 1
    nums.sort()
    for i in range(n):
        if nums[i] == nums[i + 1]:
            return nums[i]

'''
This solution modifies the input array and does not use constant space, so it
does not satisfy the constraints of the problem.
'''

# Time: O(n^2)
# Auxiliary space: O(1)
def find_duplicate_naive(nums: list[int]) -> int:
    n = len(nums) - 1
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            if nums[j] == nums[i]:
                return nums[i]


if __name__ == '__main__':
    nums = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]
    print(find_duplicate_pigeonhole_iterative(nums))

