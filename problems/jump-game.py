'''
Jump Game

INCOMPLETE, INCORRECT
'''

def can_jump(nums: list[int]) -> bool:
    if nums == [0]:
        return True

    n = len(nums)
    zeros_i = []
    for i in range(n):
        if nums[i] == 0 and (i == n - 1 or nums[i + 1] != 0):
            zeros_i.append(i)

    left_i = -1
    for right_i in zeros_i:
        can_pass_0 = False
        for mid_i in range(right_i - 1, left_i, -1):
            gap = right_i - mid_i
            if right_i == n - 1:
                gap -= 1
            if nums[mid_i] > gap:
                can_pass_0 = True
                break
        if not can_pass_0:
            return False
        left_i = right_i

    return True

if __name__ == '__main__':
    print(can_jump([2,0,0]))

