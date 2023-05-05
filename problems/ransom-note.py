'''
Ransom Note (#383)

Given two strings `ransom_note` and `magazine`, return True if `ransom_note`
can be constructed by using the letters from `magazine` and False otherwise.
Each letter in `magazine` can only be used once in `ransom_note`.
'''

from collections import defaultdict, Counter

def can_construct(ransom_note: str, magazine: str) -> bool:
    hash_map = defaultdict(lambda: 0)
    for m in magazine:
        hash_map[m] += 1
    for r in ransom_note:
        if hash_map[r] == 0:
            return False
        hash_map[r] -= 1
    return True


def can_construct2(ransom_note: str, magazine: str) -> bool:
    for c in set(ransom_note):
        if magazine.count(c) < ransom_note.count(c):
            return False
    return True


def can_construct3(ransom_note: str, magazine: str) -> bool:
    return (r := Counter(ransom_note)) & Counter(magazine) == r


if __name__ == '__main__':
    ransom_note = 'aab'
    magazine = 'aabbc'
    print(can_construct(ransom_note, magazine))

