# Given an array of integers and a target integer, return all pairs of numbers in the array that sum to the target.

def two_sum(arr, target):
    res = []
    seen = set()
    for i in arr:
        if target - i not in seen:
            seen.add(i)
        else:
            res.append([target-i, i])
    return res

print(two_sum([2, 5, 9, 8, 14, 0, 1, -4], 10))
