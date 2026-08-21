'''
Jump Game II (#45)

Given an array where each element represents the maximum forward jump length
(in indicies) from that position, return the minimum number of jumps to reach
the last index. Assume that you are always able to make it to the last index.

0 <= nums[i] <= 1000
'''

# Time: O(n)
# Auxiliary space: O(1)
def jump(nums: list[int]) -> int:
    result = 0
    left = right = 0

    while right < len(nums) - 1:
        farthest = 0
        for i in range(left, right + 1):
            farthest = max(farthest, i + nums[i])
        left = right + 1
        right = farthest
        result += 1

    return result

'''
 *  *        *     *
[2, 3, 1, 1, 4, 5, 6]
[ ][    ][    ][    ]
    L  R
 0   1     2     3     <- minimum number of jumps to reach these values

Let there be two pointers L and R that define the range that you can jump into
from some position i. Because we are guaranteed to be able to reach the last
index, we can assume a[0] > 0. The next range is L = 1, R = a[0].

In that range, there is some position that will be able to take you the
farthest to the right. Each position i can take you to, at most, i + a[i]. Find
the position (farthest) that maximizes i + a[i]. The next range is L = R + 1,
R = farthest.

This is a greedy algorithm because you are always taking the position that can
take you the farthest to the right. It is also like a 1D BFS, where each range
represents a new depth.
'''

if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4, 5, 6]
    print(jump(nums))

'''
This problem can also be solved with dynamic programming, but the solutions
would be slower.
'''
