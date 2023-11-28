import random

def _find_indicies(arr, op, r):
    stack = []
    result = [-1] * len(arr)
    for i in r:
        while stack and op(arr[i], arr[stack[-1]]):
            result[stack.pop()] = i
        stack.append(i)
    return result


def _find_indicies2(arr, op):
    stack = []
    result = [-1] * len(arr)
    for i in range(len(arr)):
        while stack and op(arr[i], arr[stack[-1]]):
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(i)
    return result


def find_next_greater_indicies(arr):
    return _find_indicies(arr, lambda x, y: x > y, range(len(arr)))

def find_prev_greater_indicies(arr):
    return _find_indicies(arr, lambda x, y: x > y, range(len(arr) - 1, -1, -1))
#    return _find_indicies2(arr, lambda x, y: x >= y)

def find_next_lesser_indicies(arr):
    return _find_indicies(arr, lambda x, y: x < y, range(len(arr)))

def find_prev_lesser_indicies(arr):
#    return _find_indicies(arr, lambda x, y: x < y, range(len(arr) - 1, -1, -1))
    return _find_indicies2(arr, lambda x, y: x <= y)


if __name__ == '__main__':
    arr = []
    for _ in range(8):
        arr.append(random.randint(1, 50))
    print(f'Arr: {arr}')
#    print(f'Next Greater: {find_next_greater_indicies(arr)}')
#    print(f'Prev Greater: {find_prev_greater_indicies(arr)}')
#    print(f'Next Lesser: {find_next_lesser_indicies(arr)}')
    print(f'Prev Lesser: {find_prev_lesser_indicies(arr)}')

