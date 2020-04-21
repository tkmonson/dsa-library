# Given an array of positive integers and a threshold, find the minimum divisor to ceiling-divide the elements of the array such that their sum is less than or equal to the threshold.

# Input:
    # nums = [1,3,5,7]
    # threshold = 7

# Output:
    # 1/3 + 3/3 + 5/3 + 7/3
    # 1 + 1 + 2 + 3 = 7
    # res = 3

# Time: O(NlogM) where m is the max number of nums and n is the length of nums
# Space: O(1)

# Assume a maximum divisor of 10^6.

def minimum_divisor(nums, threshold):
    lo = 1
    hi = 1000000
    while lo <= hi:
        mid = lo + (hi-lo) // 2
        total = 0
        for num in nums:
            rounding = (num % mid) > 0
            total += (num // mid) + rounding
        if total <= threshold:
            hi = mid - 1
        else:
            lo = mid + 1

    return lo

nums = [1,3,5,7,9,41]
threshold = 7
print(minimum_divisor(nums, threshold))

# [1,3,5,7]

#                      mid
#                      v
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ...
# ^                                                  ^
# lo                                                hi

#### 1/11 + 3/11 + 5/11 + 7/11 = 1 + 1 + 1 + 1 = 4 < 7

#         mid
#         v
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ...
# ^                 ^
# lo                hi

#### 1/5 + 3/5 + 5/5 + 7/5 = 1 + 1 + 1 + 2 = 5 < 7

#   mid
#   v
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ...
# ^     ^
# lo    hi

#### 1/2 + 3/2 + 5/2 + 7/2 = 1 + 2 + 3 + 4 = 10 > 7

#     mid
#     v
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ...
#     ^ ^
#    lo hi

#### 1/3 + 3/3 + 5/3 + 7/3 = 1 + 1 + 2 + 3 = 7

#     v
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 ...
#   ^ ^
#  hi lo

#### hi < lo => done

# ------------------------------------

# Pseudocode:

# create lo and hi variables
# while lo is less than or equal to hi
    # create mid variable (midpoint of lo and hi)
    # find the sum of elements ceiling-divided by mid
        # if it's less than or equal to threshold
            # hi = mid - 1
        # else
            # lo = mid + 1
# return lo
