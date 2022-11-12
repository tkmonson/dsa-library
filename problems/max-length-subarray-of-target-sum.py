'''
Maximum Length Subarray of Target Sum (from Moveworks interview 08/22)
PASSES BUT NOT OPTIMIZED FOR TIME, SPACE, OR READABILITY

Given an array of integers and a target sum Y, return the maximum length
subarray whose elements sum to Y.
'''

def max_length_subarray(arr, Y):
    L = len(arr)
    s = [0]
    for i in range(L):
        s.append(s[-1] + arr[i])
    for max_length in reversed(range(1, L + 1)):
        for i in range(max_length, L + 1):
            j = i - max_length
            if s[i] - s[j] == Y:
                return arr[j:i]
    return []

if __name__ == '__main__':
    print(max_length_subarray([1, -1, 5, -2, 3], 3))

'''
Once you have the sums of all subarrays that start at the 0th index, you can
use those values to quickly compute the sums of all other subarrays. Think of
these subarrays like overlapping sets. For i < j, sum(a[:j]) - sum(a[:i]) =
sum(a[i:j]).

In order to consider the subarrays that start at the 0th index, you need to
have cases where the sum being subtracted represents a subarray of length 0. An
easy way to do this is to prepend a 0 to the sums array.
'''
