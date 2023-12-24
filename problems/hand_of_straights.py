'''
Hand of Straights (#846)

There is a collection of cards represented by an integer array `hand`, where
`hand[i]` is the value written on the ith card, and we want to arrange these
cards in groups of size `group_size` such that each group contains cards whose
values are consecutive. Return whether or not such an arrangement is possible.

e.g. hand = [1, 2, 3, 6, 2, 3, 4, 7, 8], group_size = 3
    => True, the cards can be grouped as [1, 2, 3], [2, 3, 4], [6, 7, 8]

1 < len(hand) <= 10^4
0 < hand[i] <= 10^9
'''

from collections import Counter
import heapq

# Time: O(nlogn) (looping through n cards, popping a heap is logn)
# Auxiliary space: O(n)
def is_n_straight_hand(hand: list[int], group_size: int) -> bool:
    if len(hand) % group_size:
        return False

    count = Counter(hand)
    heap = list(count.keys())
    heapq.heapify(heap)

    while heap:
        for card in range(heap[0], heap[0] + group_size):
            if card not in count:
                return False
            count[card] -= 1

            if count[card] == 0:
                if card != heap[0]:
                    return False
                heapq.heappop(heap)

    return True

'''
Given a random card c in the hand, there are group_size possible groups that it
could be a part of. For example, if c = 3 and group_size = 3, c could be in
[3, 4, 5], [2, 3, 4], or [1, 2, 3]. If instead of choosing a random card, we
choose s, the smallest card in the hand that has not already been grouped, we
know that s can only be part of one group: list(range(s, s + group_size)).
Thus, it would be helpful to know which cards are still available (Counter) and
which available card is the smallest (min-heap).

After creating a group G = list(range(heap[0], heap[0] + group_size)), the top
of the heap will be some element t in G (unless every element in G originally
had a count of 1, in which case t will be some number greater than G[-1] and
the following case will not occur). If, while creating G, some element c in G,
where c > t, had its count reduced to 0, that implies that the next group
H = list(range(t, t + group_size)) cannot be created because c is also in H but
its count is now 0. Thus, if any element in the heap other than the minimum
element has its count reduced to 0, the cards cannot be grouped according to
the constraints of the problem.
'''


def is_n_straight_hand2(hand: list[int], group_size: int) -> bool:
    if len(hand) % group_size:
        return False

    groups = [[] for _ in range(len(hand) // group_size)]
    i = j = 0
    hand.sort()

    for card in hand:
        try:
            while (len(groups[j]) == group_size or
                  (groups[j] and groups[j][-1] != card - 1)):
                j += 1
            groups[j].append(card)
        except IndexError:
            return False
        if len(groups[i]) == group_size:
            i += 1
        j = i

    return True

if __name__ == '__main__':
    hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    group_size = 3
    print(is_n_straight_hand(hand, group_size))
    
