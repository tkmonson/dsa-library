'''
Two Sum II (#167)

Given a 1-indexed array of integers `numbers` that is sorted in non-decreasing
order, find two numbers that add up to a specific number `target`. Return the
indicies of these numbers in the form `[i, j]`, where `1 <= i < j <
len(numbers)`. Assume there is exactly one solution. The algorithm must use
only constant space.
'''

def two_sum(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1
    while True:
        s = numbers[left] + numbers[right]
        if s < target:
            left += 1
        elif s > target:
            right -= 1
        else:
            return [left + 1, right + 1]

