'''
Top K Frequent Words (#692)

Given an array of strings and an integer `k`, return the `k` most frequent
strings, sorted by decreasing frequency, with strings of equal frequency sorted
in lexicographic order.
'''

from collections import Counter
import heapq

class Node:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __gt__(self, other):
        if self.freq != other.freq:
            return self.freq > other.freq
        else:
            return self.word < other.word


# Time: O(nlogk) (logk for each word)
# Auxiliary space: O(n)
def top_k_frequent(words: list[str], k: int) -> list[str]:
    c = Counter(words)
    heap = []
    for word in c:
        node = Node(word, c[word])
        if len(heap) < k:
            heapq.heappush(heap, node)
        else:
            if node > heap[0]:
                heapq.heapreplace(heap, node)

    ans = []
    while heap:
        ans.append(heapq.heappop(heap).word)

    return ans[::-1]


# Time: O(nlogn)
# Auxiliary space: O(n)
def top_k_frequent_sort(words: list[str], k: int) -> list[str]:
    c = Counter(words)
    nodes = [Node(word, freq) for word, freq in c.items()]
    nodes.sort(reverse=True)
    return [node.word for node in nodes[:k]]


if __name__ == '__main__':
    words = ['the', 'day', 'is', 'sunny', 'the',
             'the', 'the', 'sunny', 'is', 'is']
    k = 4
    print(top_k_frequent_sort(words, k))

'''
There are O(n) solutions to this problem (bucket sort + trie, quickselect), but
they are less intuitive.
'''

