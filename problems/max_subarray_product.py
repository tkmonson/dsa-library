'''
Given an array of integers, find its maximum subarray product.

[-6, 4, -5, 8, -10, 0, 8]  =>  1600 (subarray is [4, -5, 8, -10])
[40, 0, -20, -10]  =>  200 (subarray is [-20, -10])

Time Complexity: O(n)
Auxiliary Space Complexity: O(1)

The naive O(n^2) solution is to calculate the product of every subarray.
The better solution is to realize that the product of a subarray is
equal to its last element times the product of its previous elements.
And the maximum product of a subarray ending at index i is equal to A[i]
times either the minimum or maximum product of a subarray ending at
i - 1, depending on whether A[i] is negative or positive. At each index
i, we collect the minimum and maximum product of subarrays ending at i,
and we use them to inform answers at higher indices. Finally, we return the
maximum product of the subarray ending at index n - 1.
'''

def max_subarray_product(arr):
    max_ending, min_ending, curr_max = (arr[0],) * 3
    for i in range(1, len(arr)):
        temp = max_ending
        max_ending = max(arr[i], max(arr[i] * max_ending, arr[i] * min_ending))
        min_ending = min(arr[i], min(arr[i] * temp, arr[i] * min_ending))
        curr_max = max(curr_max, max_ending)
    return curr_max

if __name__ == "__main__":
    arr = [-6, 4, -5, 8, -10, 0, 8]
    print(max_subarray_product(arr))
