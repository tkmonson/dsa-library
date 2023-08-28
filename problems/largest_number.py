'''
Largest Number (#179)

Given a list of non-negative integers nums, arrange them such that they form
the largest number and return it as a string.
'''

import functools

# Time: O(n*log(n))
# Auxiliary Space: O(n)
def largest_number(nums: list[int]) -> str:
    def comparator(s1, s2):
        if (s1 + s2) < (s2 + s1):
            return -1
        if (s1 + s2) > (s2 + s1):
            return 1
        return 0

    nums = [str(n) for n in nums]
    nums = sorted(nums, key=functools.cmp_to_key(comparator), reverse=True)
    return '0' if nums[0] == '0' else ''.join(nums)

if __name__ == '__main__':
    nums = [3, 30, 34, 5, 9]
    print(largest_number(nums))

'''
This is a custom sort problem, which suggests that one should write a
custom comparator that will produce a key function when passed to
functools.cmp_to_key.

The comparator determines the ascending order of elements in nums. For example,
comparator('32','3') would return -1 because '323' comes before '332' in
lexicographic order, implying that '32' should come before '3' if one wishes to
sort elements such that their concatenation yields the smallest number
possible. The descending order is then used to produce the largest number
possible.
'''

