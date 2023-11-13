'''
Permutation in String (#567)

Given two strings `s1` and `s2`, return True if `s2` contains a permutation of
`s1` or False otherwise.
'''

# Time: O(n)
# Auxiliary space: O(1)
def check_inclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    alphabet_primes = [2, 3, 5, 7, 11, 13, 17, 19,
                       23, 29, 31, 37, 41, 43, 47,
                       53, 59, 61, 67, 71, 73, 79,
                       83, 89, 97, 101]
    get_prime = lambda ch: alphabet_primes[ord(ch) - ord('a')]

    target_code = 1
    for ch in s1:
        target_code *= get_prime(ch)

    window_code = 1
    left, right = 0, 0
    while right < len(s1):
        right += 1
        window_code *= get_prime(s2[right - 1])
    if window_code == target_code:
        return True
    while right < len(s2):
        right += 1
        window_code *= get_prime(s2[right - 1])
        window_code //= get_prime(s2[left])
        left += 1
        if window_code == target_code:
            return True

    return False

'''
We need to slide a window of length len(s1) across s2 and check if the window
contains the same characters as s1 at each stage. To do this in linear time, we
need this character check to be O(1). We can do this by mapping collections of
characters to unique numbers using a prime factorization hash.
'''

if __name__ in '__main__':
    s1 = 'adc'
    s2 = 'dcda'
    print(check_inclusion(s1, s2))

