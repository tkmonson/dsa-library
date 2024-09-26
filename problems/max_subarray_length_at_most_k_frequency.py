'''
Length of Longest Subarray With At Most K Frequency (#2958) (CodeSignal 09/24)

Given a non-empty array and a positive integer `k`, return the length of the
longest subarray whose most common element appears at most `k` times.
'''

from collections import Counter, defaultdict

# Time: O(n)
# Auxiliary space: O(n)
def max_subarray_length(nums: list[int], k: int) -> int:
    result = 0
    freq = defaultdict(lambda: 0)
    left = 0

    for right in range(len(nums)):  # right is inclusive
        freq[nums[right]] += 1
        while freq[nums[right]] > k:
            freq[nums[left]] -= 1
            left += 1
        result = max(result, right - left + 1)

    return result


# Time: O(n^2) (subarrays are explored from longest to shortest)
# Auxiliary space: O(n)
def max_subarray_length2(nums: list[int], k: int) -> int:
    n = len(nums)
    _freq = Counter(nums)
    _too_frequent = set([_k for (_k, v) in _freq.items() if v > k])
    if not _too_frequent:
        return n

    for length in range(n - 1, 1, -1):
        left, right = 0, length  # right is exclusive

        freq = _freq.copy()
        too_frequent = _too_frequent.copy()

        freq[nums[right]] -= 1
        if nums[right] in too_frequent and freq[nums[right]] == k:
            too_frequent.remove(nums[right])

        _freq = freq.copy()
        _too_frequent = too_frequent.copy()

        while right < n:
            if not too_frequent:
                return length

            freq[nums[right]] += 1
            if freq[nums[right]] > k:
                too_frequent.add(nums[right])

            freq[nums[left]] -= 1
            if nums[left] in too_frequent and freq[nums[left]] == k:
                too_frequent.remove(nums[left])

            left += 1
            right += 1

        if not too_frequent:
            return length

    return 1


if __name__ == '__main__':
    nums = [1, 2, 2, 3, 1, 2, 3]
    k = 2
    print(max_subarray_length(nums, k))

'''
The brute-force approach is O(n^3): for each subarray (O(n^2)), count its
elements to see if it qualifies (O(n)). Both parts can be improved.

You don't have to count every subarray from scratch. Given the count of the
current window, when you slide the window, you can decrement the count of
elements that are removed and increment the count of elements that are added.
Finding the count of a subarray like this is O(1) (amortized).

To lower the complexity of visiting subarrays to O(n), we have to find the
answer in one pass. Starting with an empty subarray, we increase the length by
expanding the window to the right until the subarray does not qualify. If the
subarray a[i:j] does not qualify, then no subarray a[i:x] where x > j will
qualify either. Thus, you should contract the window from the left until the
subarray qualifies before expanding the window to the right again.

This is a variation of Kadane's algorithm.
'''

