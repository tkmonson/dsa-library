'''
Majority Element II (#229)

Given an integer array of size n, find all elements that appear more than
floor(n / 3) times.
'''

from collections import Counter
from math import floor

# Time: O(n)
# Auxiliary space: O(1)
def majority_element(nums: list[int]):
    cand1 = cand2 = None
    count1 = count2 = 0
    for num in nums:
        if num == cand1:
            count1 += 1
        elif num == cand2:
            count2 += 1
        elif count1 == 0:
            cand1, count1 = num, 1
        elif count2 == 0:
            cand2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    return [n for n in (cand1, cand2) if nums.count(n) > len(nums) // 3]

'''
This is a modified Boyer-Moore Voting Algorithm for majority threshold of
floor(n / 3). At most 2 elements can be majority elements for this threshold,
so keep track of 2 leading candidates. The algorithm is basically the same as
the floor(n / 2) version, but you need to pass over the array a second time to
verify that the leading candidates are actually majority elements.
'''

# Time: O(n)
# Auxiliary space: O(n)
def majority_element2(nums: list[int]):
    ans = []
    th = floor(len(nums) // 3)
    c = Counter(nums)
    for num in c:
        if c[num] > th:
            ans.append(num)

    return ans

if __name__ == '__main__':
    nums = [3, 2, 3]
    print(majority_element(nums))

'''
If an element must appear > floor(n / k) times to be a majority element, there
are at most k - 1 majority elements.
'''