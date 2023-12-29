'''
Palindrome Partitioning (#131)

Given a string `s`, partition `s` such that every substring of the partition is
a palindrome. Return all possible palindrome partitions of `s`.

E.g. s = 'aab'  =>  [['a', 'a', 'b'], ['aa', 'b']]
'''

# Time: O(n2^n)
# Auxiliary space: O(n)
def partition(s: str) -> list[list[str]]:
    result = []
    n = len(s)

    def backtrack(i, curr):
        if i == n:
            result.append(curr)
            return

        for j in range(i + 1, n + 1):
            a = s[i:j]
            if a == a[::-1]:
                backtrack(j, curr + [a])

    backtrack(0, [])
    return result


# Faster
def partition2(s: str) -> list[list[str]]:
    n = len(s)
    dp = [[] for _ in range(n + 1)]
    dp[-1].append([])

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n + 1):
            curr = s[i:j]

            if curr == curr[::-1]:
                for e in dp[j]:
                    dp[i].append([curr] + e)

    return dp[0]

'''
For 'oooo':
dp[4] = [[]]
dp[3] = [[o]]
dp[2] = [[o, o], [oo]]
dp[1] = [[o, o, o], [oo, o], [o, oo], [ooo]]
dp[0] = [[o, o, o, o], [oo, o, o], [o, oo, o], [ooo, o], [o, o, oo], [oo, oo], [o, ooo], [oooo]]
'''

if __name__ == '__main__':
    s = 'ooooo'
    print(partition2(s))

