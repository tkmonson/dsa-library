'''
Group Anagrams (#49)

Given an array of strings, group the anagrams together. Return a list of the
groups in any order.
'''

from collections import defaultdict

def group_anagrams_hash(strs: list[str]) -> list[list[str]]:
    d = defaultdict(list)
    alphabet_primes = [2, 3, 5, 7, 11, 13, 17, 19,
                       23, 29, 31, 37, 41, 43, 47,
                       53, 59, 61, 67, 71, 73, 79,
                       83, 89, 97, 101]

    for word in strs:
        prime_code = 1
        for ch in word:
            prime_code *= alphabet_primes[ord(ch) - ord('a')]
        d[prime_code].append(word)

    return list(d.values())

'''
We would like to devise a function that, when given any member of the same
anagram group, produces the same value, with no collisions otherwise. Given
that every prime factorization corresponds to a unique number, we can associate
each letter with a prime number and produce a product for each word. Anagrams
will have the same product because they have the same prime factorization.
'''

def group_anagrams_sort(strs: list[str]) -> list[list[str]]:
    d = defaultdict(list)
    for word in strs:
        sorted_word = ''.join(sorted(word))
        d[sorted_word].append(word)
    return list(d.values())


if __name__ == '__main__':
    strs = ['eat', 'ate', 'tea', 'cat', 'hhh', 'tac']
    print(group_anagrams(strs))

