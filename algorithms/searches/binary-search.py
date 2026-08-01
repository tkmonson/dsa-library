def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # protects against integer overflow
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid

    return -1

if __name__ == "__main__":
    arr = list(range(1,101))
    target = 37
    print(binary_search(arr, target))
