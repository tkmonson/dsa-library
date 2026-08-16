# Time: O(n^2)
# Auxiliary space: O(1)
def insertion_sort(nums: list[int]) -> list[int]:
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j - 1] > nums[j]:
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
    return nums

'''
Insertion sort is how one would naturally sort a new card into a sorted hand.
Draw a card. Compare it to the sorted cards in your hand, from right to left.
Shift larger cards to the right until you find the correct empty slot, then
insert the card.

1. Consider the first element sorted
2. Traverse through the rest of the cards left to right
3. Sift each one down until it is in its proper place
'''
