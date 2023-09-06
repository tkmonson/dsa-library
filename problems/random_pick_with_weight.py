'''
Random Pick with Weight (#528)

Given an array of positive integers `w`, return an index in `[0, len(w) - 1]`,
inclusive, that is chosen randomly, where the probability of picking an index
`i` is `w[i] / sum(w)`.
'''

import random
import bisect

class Solution1:  # binary search in normalized prefix sum array
    def __init__(self, w: list[int]):
        running = 0
        total = sum(w)
        self.probs = []
        for i in range(len(w)):
            running += w[i] / total
            self.probs.append(running)

    # Time: O(logn)
    # Auxiliary space: O(1)
    def pick_index(self) -> int:
        return bisect.bisect_left(self.probs, random.random())


class Solution2:  # binary search in prefix sum array
    def __init__(self, w: list[int]):
        running = 0
        self.prefix = []
        for i in range(len(w)):
            running += w[i]
            self.prefix.append(running)

    # Time: O(logn)
    # Auxiliary space: O(1)
    def pick_index(self) -> int:
        target = random.uniform(0, self.prefix[-1])
        left, right = 0, len(self.prefix) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.prefix[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


class Solution3:  # update prefix sum variable until it meets or exceeds target
    def __init__(self, w: list[int]):
        self.w = w

    # Time: O(n)
    # Auxiliary space: O(1)
    def pick_index(self) -> int:
        target = random.randint(1, sum(self.w))
        running = 0
        for i in range(len(self.w)):
            running += self.w[i]
            if running >= target:
                return i


if __name__ == '__main__':
    w = [2, 4, 8, 1]
    s = Solution3(w)
    d = {i: 0 for i in range(len(w))}
    for _ in range(1000):
        d[s.pick_index()] += 1
    print(d)

