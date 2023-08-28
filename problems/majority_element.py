'''
Majority Element (#169)

Given an array of size n, return the majority element, the element that appears
more than floor(n / 2) times. Assume a majority element always exists in the
array.
'''

from collections import Counter

# Time: O(n)
# Auxiliary space: O(n)
def majority_element(nums: list[int]) -> int:
    mode_count = 0
    counter = Counter(nums)
    for num in counter:
        if counter[num] > mode_count:
            mode = num
            mode_count = counter[num]
    return mode


# Time: O(n)
# Auxiliary space: O(1)
def majority_element2(nums: list[int]) -> int:
    ans, count = None, 0
    for num in nums:
        if count == 0:
            ans = num
        count += (1 if num == ans else -1)
    return ans


if __name__ == '__main__':
    nums = [1, 1, 1, 4, 4, 4, 4]
    print(majority_element(nums))

