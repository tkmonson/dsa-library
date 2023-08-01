'''
Daily Temperatures (#739)

Given an array of integers `temperatures` that represents daily temperatures,
return an array `result` such that `result[i]` is the number of days you have
to wait after the `ith` day to get a warmer temperature. If there is no future
day that is warmer, let `result[i] == 0`.
'''

# Time: O(n)
# Auxiliary space: O(n)
def daily_temperatures(temperatures: list[int]) -> list[int]:
    result = [0] * len(temperatures)
    stack = [(-1, float('inf'))]

    for curr_i, curr_t in enumerate(temperatures):
        while stack[-1][1] < curr_t:
            pop_i, _ = stack.pop()
            result[pop_i] = curr_i - pop_i
        stack.append((curr_i, curr_t))

    return result

'''
This problem is an easier version of "Largest Rectangle in Histogram." The
solution uses a monotonically decreasing stack that is popped such that new
elements can be pushed without causing the stack to become unsorted.
'''

if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    print(daily_temperatures(temperatures))

