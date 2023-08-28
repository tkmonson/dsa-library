# Given an array of integers, return all equilibrium indices.
# An index is an equilibrium index if the sum of all elements to the left of it is equal to the sum of all elements to the right of it.

# [0, -3, 5, -4, -2, 3, 1, 0]  =>  [0, 3, 7]

# [5, 5, 5, 5, 5, 5, 5, 5]  => []

# Time Complexity: O(n)
# Space Complexity: O(1)

def equilibrium_index(arr):
    n = len(arr)
    total = sum(arr)
    result = []

    left = 0
    for i in range(n):
        if left == (total - (left + arr[i])):
            result.append(i)
        left += arr[i]

    return result

arr = [0, -3, 5, -4, -2, 3, 1, 0]
print(equilibrium_index(arr))
