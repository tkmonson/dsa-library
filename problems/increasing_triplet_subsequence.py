'''
Increasing Triplet Subsequence (#334)
PASSES, BUT BETTER SOLUTIONS MAY EXIST

Given an integer array nums, return true if there exists a triple of indices
(i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. Otherwise,
return false.
'''

def increasingTriplet(nums: list[int]) -> bool:
    n = len(nums)
    min_val = nums[0]
    max_val = nums[-1]
    for j in range(1, n - 1):
        j2 = -1 - j

        j_val = nums[j]
        if j_val is not None:
            if min_val >= j_val:
                nums[j] = None
            elif j > n + j2:
                return True
            min_val = min(min_val, j_val)

        j2_val = nums[j2]
        if j2_val is not None:
            if j2_val >= max_val:
                nums[j2] = None
            elif j >= n + j2:
                return True
            max_val = max(max_val, j2_val)

    return False

if __name__ == '__main__':
    print(increasingTriplet(
        [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
    ))

'''
The naive solution is to test every possible triplet to see if it is increasing
by using a triple for-loop. This method would have O(n^3) time complexity.

A key insight is that an increasing triplet subsequence (i, j, k) reduces to a
pair of increasing pair subsequences (i, j) and (j, k). This implies that if
you find an index j such that j > some index i and nums[i] < nums[j], j is
potentially the middle index of an increasing triplet subsequence, and you need
only find some index k such that j < k and nums[j] < nums[k] to prove that such
a subsequence exists.

Another key insight is that, as you iterate from left to right looking for a
potentially suitable j, you know what is to the left of you because you have
already explored it. If you keep track of the minimum element to the left of j,
you can know whether j is a potential middle index of an increasing triplet
subsequence by evaluating min < nums[j]. After traversing the whole array from
left to right, you can then traverse it again from right to left, keeping track
of the maximum element to the right of the current iterator j. If j was a
potential middle index and nums[j] < max, an increasing triplet subsequence
exists. This reasoning led to my first solution (O(n) time, O(n) space):

    potential_js = set()
    min_val = nums[0]
    for j in range(1, len(nums) - 1):
        if min_val < nums[j]:
            potential_js.add(j)
        min_val = min(min_val, nums[j])

    max_val = nums[-1]
    for j in range(1, len(nums) - 1)[::-1]:
        if nums[j] < max_val and j in potential_js:
            return True
        max_val = max(max_val, nums[j])

    return False

Storing potential js in a separate set means that this solution has an O(n)
space complexity. However, this information can be stored within the given
array itself, yielding an O(1) space complexity. Because only potential js are
considered when evaluating nums[j] < max, the values of non-potential js are
non-essential and can be replaced with a signal value like None. Thus, all
non-None values are potential js.

    min_val = nums[0]
    for j in range(1, len(nums) - 1):
        j_val = nums[j]
        if min_val >= j_val:
            nums[j] = None
        min_val = min(min_val, j_val)

    max_val = nums[-1]
    for j in range(1, len(nums) - 1)[::-1]:
        if nums[j] is None:
            continue
        if nums[j] < max_val:
            return True
        max_val = nums[j]

    return False

The final solution given at the top of this file makes one further
modification. Instead of looking for potential js from left to right and then
looking for increasing triplet subsequences from right to left, it uses two
pointers in a single for-loop that look for potential js as they move toward
the center and look for increasing triplet subsequences as they move away from
the center.
'''

