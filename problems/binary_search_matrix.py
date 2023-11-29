'''
Search a 2D Matrix (#74)

You are given an mxn integer matrix where each row is sorted in non-decreasing
order and the first integer of each row is greater than the last integer of the
previous row. Given an integer `target`, return True if `target` is in the
matrix, False otherwise.
'''

def search_matrix(matrix: list[list[int]], target: int) -> bool:
    mxn = len(matrix) * len(matrix[0])
    left, right = 0, mxn - 1
    while left <= right:
        mid = (left + right) // 2
        row = mid // len(matrix[0])
        col = mid % len(matrix[0])
        if matrix[row][col] < target:
            left = mid + 1
        elif matrix[row][col] > target:
            right = mid - 1
        else:
            return True
    return False


if __name__ == '__main__':
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(search_matrix(matrix, target))

'''
This is no different than binary searching an array; the array has just been
chopped and stacked into a matrix.
'''

