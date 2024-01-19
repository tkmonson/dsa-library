'''
Combinations (#77)

Given two integers `n` and `k`, return all possible combinations of `k`
numbers chosen from the range `[1, n]` in any order.
'''

def combine(n: int, k: int) -> list[list[int]]:
    result = []

    def backtrack(state, start):
        if len(state) == k:
            result.append(state[:])
            return

        need = k - len(state)
        remain = n - start + 1
        available = remain - need

        for step in range(start, start + available + 1):
            state.append(step)
            start += 1
            backtrack(state, start)  # Take
            state.pop()  # Not take

    backtrack([], 1)
    return result


if __name__ == '__main__':
    n = 4
    k = 2
    print(combine(n, k))

