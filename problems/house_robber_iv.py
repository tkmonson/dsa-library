'''
House Robber IV (#2560)

There is a row of houses along a street, each with a certain amount of money
stashed. Adjacent houses have a security system connected that will contact the
police if both houses are robbed. The capability of a robber is the maximum
amount of money he robs from one house of all the houses he robbed. Given an
array representing the amount of money in each house and an integer `k`, return
the minimum capability of a robber who must rob at least `k` houses without
alerting the police. Assume it is always possible to rob at least `k` houses.
'''

# Time: O(nlogn)
# Auxiliary space: O(1)
def min_capability(nums: list[int], k: int) -> int:
    def possible(capability):
        count = 0
        neighbor_taken = False
        for num in nums:
            if neighbor_taken:
                neighbor_taken = False
            elif num <= capability:
                count += 1
                neighbor_taken = True
        return count >= k

    left, right = min(nums), max(nums)
    while left <= right:
        mid = (left + right) // 2
        if possible(mid):
            res = mid
            right = mid - 1
        else:
            left = mid + 1

    return res

'''
Ignoring the k constraint, the least possible capability is min(nums) and the
greatest possible capability is max(nums). Given the k constraint, the minimum
capability is somewhere in the range [min(nums), max(nums)], inclusive. Perform
a binary search over this range of capabilities. For each middle element, check
to see if it is possible to rob at least k non-adjacent houses of lesser or
equal value. If so, look for a smaller capability. If not, look for a larger
capability.
'''

