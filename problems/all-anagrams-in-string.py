'''
Find All Anagrams in a String (#438)

Given two strings `s` and `p`, return, in any order, an array of all the start
indicies of `p`'s anagrams in `s`.
'''

# Time: O(n)
# Auxiliary space: O(n)
def find_anagrams(s: str, p: str) -> list[int]:
    result = []
    if len(s) < len(p):
        return result

    target = {c: 0 for c in 'abcdefghijklmnopqrstuvwxyz'}
    for c in p:
        target[c] += 1

    window = {c: 0 for c in 'abcdefghijklmnopqrstuvwxyz'}
    for j in range(i := 0, len(p)):
        window[s[j]] += 1

    while True:
        if window == target:
            result.append(i)
        window[s[i]] -= 1
        i += 1
        j += 1
        try:
            window[s[j]] += 1
        except(IndexError):
            break

    return result


# Time: O(n)
# Auxiliary space: O(1)
def find_anagrams2(s: str, p: str) -> list[int]:
    result = []
    if (S := len(s)) < (P := len(p)):
        return result

    s_sum = 0
    for i in range(P):
        s_sum += hash(s[i])

    p_sum = 0
    for c in p:
        p_sum += hash(c)

    for i in range(P, S):
        if p_sum == s_sum:
            result.append(i - P)
        s_sum += hash(s[i]) - hash(s[i - P])

    return result


if __name__ == '__main__':
    s = 'cbaebabacd'
    p = 'abc'
    print(find_anagrams2(s, p))

