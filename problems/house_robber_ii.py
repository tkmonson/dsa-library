'''
House Robber II (#213)

There is a group of houses arranged in a circle (i.e. the first is the neighbor
of the last), each with a certain amount of money stashed. Adjacent houses have
a security system connected that will contact the police if both houses are
robbed. Given an array representing the amount of money in each house, return
the maximum amount of money you can rob without alerting the police.
'''

from house_robber import rob as _rob

# Time: O(n)
# Auxiliary space: O(n)
def rob(nums: list[int]):
    if (n := len(nums)) == 1:
        return nums[0]
    return max(_rob(nums[:n - 1]), _rob(nums[1:]))


# Time: O(n)
# Auxiliary space: O(1)
def rob2(nums: list[int]):
    if (n := len(nums)) == 1:
        return nums[0]

    ans = 0
    for r in (range(n - 1), range(1, n)):
        prev1, prev2 = 0, 0
        for i in r:
            prev2, prev1 = prev1, max(prev1, prev2 + nums[i])
        ans = max(ans, prev1)

    return ans


if __name__ == '__main__':
  nums = [1, 2, 3, 1]
  print(rob(nums))

'''
The functions above use the same algorithm, but one is written explicitly to
avoid passing slices of the given array into the imported function, which
requires linear space.

The one change to this problem from the original is that the first and last
houses are now neighbors. So you can either rob the first, the last, or
neither, but you cannot rob both. This is equivalent to finding the maximum
value of robbing a row of houses [0, n - 2] or a row of houses [1, n - 1],
inclusive.
'''

