'''
Longest Turbulent Subarray (#978)

Given an integer array `arr`, return the length of a maximum size turbulent
subarray of `arr`. A subarray is turbulent if the comparison sign flips between
each adjacent pair of elements in the subarray.

More formally, a subarray `[arr[i], arr[i + 1], ..., arr[j]]` of `arr` is said
to be turbulent if and only if:

For `i <= k < j`:
    * `arr[k] > arr[k + 1]` when `k` is odd, and
    * `arr[k] < arr[k + 1]` when `k` is even.

Or, for `i <= k < j`:
    * `arr[k] > arr[k + 1]` when `k` is even, and
    * `arr[k] < arr[k + 1]` when `k` is odd.
'''

# Time: O(n) (fastest because sometimes only needs one comparison per loop)
# Auxiliary space: O(1)
def max_turbulence_size(arr: list[int]) -> int:
    max_length = 1
    up, down = 1, 1
    for i in range(1, len(arr)):
        if arr[i - 1] < arr[i]:
            up, down = down + 1, 1
        elif arr[i - 1] > arr[i]:
            up, down = 1, up + 1
        else:
            up, down = 1, 1
        max_length = max(max_length, up, down)
    return max_length


# Time: O(n)
# Auxiliary space: O(1)
def max_turbulence_size2(arr: list[int]) -> int:
    n = len(arr)
    if n < 2:
        return n

    def compare(x, y):
        if x < y:
            return -1
        elif x > y:
            return 1
        else:
            return 0

    max_length = 1
    L = 0
    for R in range(1, n):
        c = compare(arr[R - 1], arr[R])
        if c == 0:
            L = R
        else:
            if R == n - 1 or c * compare(arr[R], arr[R + 1]) != -1:
                max_length = max(max_length, R - L + 1)
                L = R

    return max_length

'''
Sliding window solution. Left pointer is fixed, right increments. Left needs to
reset and the max_length needs to update when you reach the end or when the
turbulent sequence ends.
'''

# Time: O(n)
# Auxiliary space: O(1)
def max_turbulence_size3(arr: list[int]) -> int:
    comp1 = lambda k: arr[k] > arr[k + 1] if k % 2 == 1 else arr[k] < arr[k + 1]
    comp2 = lambda k: arr[k] > arr[k + 1] if k % 2 == 0 else arr[k] < arr[k + 1]

    max_length = 1
    next1, next2 = 1, 1
    for i in range(len(arr) - 2, -1, -1):
        curr1 = next1 + 1 if comp1(i) else 1
        curr2 = next2 + 1 if comp2(i) else 1
        max_length = max(max_length, curr1, curr2)
        next1, next2 = curr1, curr2

    return max_length

'''
Considers maximum length of a turbulent subarray starting at i. Uses answer to
smaller problem to find answer to bigger problem. Keeps track of both possible
versions of turbulent subarray. Goes right to left, but could go left to right.
'''

# Time: O(n)
# Auxiliary space: O(n) (stack)
def max_turbulence_size4(arr: list[int]) -> int:
    comp1 = lambda k: arr[k] > arr[k + 1] if k % 2 == 1 else arr[k] < arr[k + 1]
    comp2 = lambda k: arr[k] > arr[k + 1] if k % 2 == 0 else arr[k] < arr[k + 1]

    max_length = 1
    def dfs(i):
        nonlocal max_length
        if i == len(arr) - 1:
            return (1, 1)
        next1, next2 = dfs(i + 1)
        curr = (next1 + 1 if comp1(i) else 1, next2 + 1 if comp2(i) else 1)
        max_length = max(max_length, curr[0], curr[1])
        return curr
    
    dfs(0)
    return max_length

'''
Recursive version of previous solution.
'''

if __name__ == '__main__':
    arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
    print(max_turbulence_size(arr))
