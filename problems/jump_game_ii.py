'''
Jump Game II (#45)

Given an array where each element represents the maximum forward jump length
(in indicies) from that position, return the minimum number of jumps to reach
the last index. Assume that you are always able to make it to the last index.
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
Starting at i = 0, you can jump within range(1, nums[0] + 1). In that range,
there is a jump value that will take you the farthest to the right. The range
of the next jump would be range(prev_right + 1, farthest + 1). This is a greedy
algorithm because you are always taking the jump value that can take you
farthest to the right.

 *  *        *     *
[2, 3, 1, 1, 4, 5, 6]
[ ][    ][    ][    ]
'''

if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4, 5, 6]
    print(jump(nums))

'''
This problem can also be solved with dynamic programming, but the solutions
would be slower.
'''
