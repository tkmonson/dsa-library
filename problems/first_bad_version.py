'''
First Bad Version (#278)

When developing a product, a version that fails the quality check is bad. All
versions that come after a bad version are also bad. Given a number of versions
`n` (a list of the versions would look like `[1, 2, ..., n]`), find the first
bad version. You are given an API `is_bad_version(version)` that returns
whether `version` is bad. Minimize the number of calls to this API.

1 <= bad <= n <= 2^31 - 1
'''

def f(n: int, bad: int) -> int:
    def is_bad_version(version: int) -> bool:
        return version >= bad

    def first_bad_version(n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            if is_bad_version(mid):
                if not is_bad_version(mid - 1):
                    return mid
                right = mid - 1
            else:
                left = mid + 1

    return first_bad_version(n)


if __name__ == '__main__':
    n = 10
    bad = 7
    print(f(n, bad))

