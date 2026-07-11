'''
Minimum Size Subarray Sum (#209)

Given an array of positive integers `nums` and a positive integer `target`,
return the minimal length of a subarray whose sum is greater than or equal to
`target`. If there is no such subarray, return 0 instead.
'''

def min_sub_array_len(target: int, nums: list[int]) -> int:
    min_length = float('inf')
    curr_sum = 0
    left = 0
    for right in range(len(nums)):
        curr_sum += nums[right]
        while curr_sum >= target:
            min_length = min(min_length, right - left + 1)
            curr_sum -= nums[left]
            left += 1

    return min_length if min_length != float('inf') else 0


def min_sub_array_len2(target: int, nums: list[int]) -> int:
    if sum(nums) < target:
        return 0

    min_length = float('inf')
    curr_sum = nums[0]
    left, right = 0, 0

    while right < len(nums):
        while curr_sum < target:
            right += 1
            try:
                curr_sum += nums[right]
            except IndexError:
                break
        while curr_sum >= target:
            min_length = min(min_length, right - left + 1)
            curr_sum -= nums[left]
            left += 1

    return min_length

'''
Similar to Kruskal's algorithm. Expand to the right until greater than or equal
to the target, contract from the left until less than the target. Note that the
result should be updated every time the window changes in length while the sum
is greater than or equal to the target (that is, before each contraction).
'''

if __name__ == '__main__':
    target = 7
    nums = [2,3,1,2,4,3]
    print(min_sub_array_len(target, nums))
