def group_anagrams(words):
    group_set = set()
    letter_primes = [2, 3, 5, 7, 11, 13, 17, 19,
                     23, 29, 31, 37, 41, 43, 47,
                     53, 59, 61, 67, 71, 73, 79,
                     83, 89, 97, 101]

    for word in words:
        prime_code = 1
        for letter in word:
            prime_code *= letter_primes[ord(letter) - ord('a')]
        group_set.add(prime_code)

    return len(group_set)

print(str(group_anagrams(['eat', 'ate', 'tea', 'cat', 'hhh', 'tac'])))
