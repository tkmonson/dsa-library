'''
Longest Consecutive Sequence (#128)

Given an unsorted array of integers, return the length of the longest
subsequence of consecutive elements. The algorithm must run in O(n) time.

E.g. [100, 4, 200, 1, 3, 2] => [4, 1, 3, 2] => 4
'''

# Time: O(n)
# Auxiliary space: O(n)
def longest_consecutive(nums: list[int]) -> int:
    s = set(nums)
    max_count = 0

    for n in nums:
        if n in s:
            s.remove(n)
            count = 1
            for i in (-1, 1):
                c = n + i
                while c in s:
                    s.remove(c)
                    count += 1
                    c += i
            max_count = max(max_count, count)

    return max_count

'''
A subsequence does not have to be contiguous, the elements in the subsequence
do not have to be in order, and "consecutive" implies that the subsequence will
not contain duplicates. All of this implies that we should create a set of the
array's elements.
'''

if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    print(longest_consecutive(nums))

