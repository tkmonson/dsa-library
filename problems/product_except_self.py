'''
Product of Array Except Self (#238)

Given an integer array `nums`, return an array `answer` such that answer[i] is
equal to the product of all the elements of `nums` except `nums[i]`. You can't
use the division operation.
'''

# Time: O(n)
# Auxiliary space: O(n)
def product_except_self(nums: list[int]) -> list[int]:
    answer = [1]
    for i in range(len(nums) - 1):
        answer.append(answer[-1] * nums[i])
    right_product = 1
    for i in reversed(range(1, len(nums))):
        right_product *= nums[i]
        answer[i - 1] *= right_product
    return answer

'''
[1, 2, 3, 4]     [1]

--- 1        =>  [1, 1]
------ 2     =>  [1, 1, 2]
--------- 6  =>  [1, 1, 2, 6]

       4 --- =>  [1,   1, 8, 6]
   12 ------ =>  [1,  12, 8, 6]
24 --------- =>  [24, 12, 8, 6]
'''

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6]
    print(product_except_self(nums))

