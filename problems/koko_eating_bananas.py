'''
Koko Eating Bananas (#875)

There are `n` piles of bananas. Koko wants to eat all of the bananas before the
guards return in `h` hours. Koko can decide her bananas-per-hour eating speed
`k`. Each hour, she chooses a pile and eats `k` bananas from it. If there are
less than `k` bananas in the pile, she finishes the pile and does not eat any
more bananas during the hour. Koko would like to eat as slowly as possible
while still finishing before the guards return. Return the minimum integer `k`
such that she can eat all the bananas within `h` hours.
'''

def min_eating_speed(piles: list[int], h: int) -> int:
    def hours_required(k):
        result = 0
        for pile in piles:
            result += (pile + k - 1) // k
        return result

    left, right = 1, max(piles)
    while left < right:
        k = (left + right) // 2
        hours = hours_required(k)
        if hours > h:
            left = k + 1  # Taking too long, eat faster
        else:
            right = k  # Finishing in time, try to eat slower

    return left

'''
The fastest effective eating rate is one pile per hour (k = max(piles)). Thus,
the range of possible k values is 1 to max(piles). Do a binary search on this
range. For each step in the search, calculate the number of hours it would take
to eat all the bananas with the current k. If it's greater than h, search the
right subarray (faster eating rates). Else, search the left subarray (slower
eating rates).

This is an application of the binary search algorithm for finding the leftmost
duplicate target.
'''

if __name__ == '__main__':
    piles = [30, 11, 23, 4, 20]
    h = 6
    print(min_eating_speed(piles, h))

