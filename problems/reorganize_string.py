'''
Reorganize String (#767)

Given a string s, rearrange the characters of s so that any two adjacent
characters are not the same.

Return any possible rearrangement of s or return "" if not possible.
'''

from collections import Counter
import heapq

# Time: O(nlogn)
# Auxiliary space: O(n)
def reorganize_string(s: str) -> str:
    count = Counter(s)
    heap = []
    result = []

    for k in count:
        heapq.heappush(heap, (-count[k], k))

    prev = None
    while heap:
        freq, ch = heapq.heappop(heap)
        result.append(ch)
        freq += 1

        if prev:
            heapq.heappush(heap, prev)
        prev = (freq, ch) if freq else None

    return '' if prev else ''.join(result)

'''
When appending characters to the result string, you want to append the character
that appears most frequently in the remaining characters and is different from
the most recently appended character.

Get the frequencies of the characters.
Keep the characters sorted by frequency in a heap.
Hold the most recently appended character outside of the heap for a turn.
The root of the heap holds the most frequent character that differs from the
most recently appended character.
A character is pushed back onto the heap every turn.
'''

# Time: O(nlogn)
# Auxiliary space: O(n)
def reorganize_string2(s: str) -> str:
    count = Counter(s)
    heap = []
    result = []

    for k in count:
        heapq.heappush(heap, (-count[k], k))

    while heap:
        freq, ch = heapq.heappop(heap)
        while freq < 0:
            result.append(ch)
            freq += 1
            try:
                freq2, ch2 = heapq.heappop(heap)
            except IndexError:
                break
            result.append(ch2)
            freq2 += 1
            if freq2 < 0:
                heapq.heappush(heap, (freq2, ch2))

    return '' if freq else ''.join(result)

'''
This solution passes all test cases, but I don't know if it is formally
correct. It pops two characters. The first stays outside of the heap and
appends every other time until used up. The second appends once and is put back
on the heap.
'''

if __name__ == '__main__':
    print(reorganize_string("baaba"))
