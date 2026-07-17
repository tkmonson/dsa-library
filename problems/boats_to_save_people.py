'''
Boats to Save People (#881)

You are given an array people where `people[i]` is the weight of the `ith`
person, and an infinite number of boats where each boat can carry a maximum
weight of `limit`. Each boat carries at most two people at the same time,
provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

1 <= people[i] <= limit
'''

# Time: O(nlogn)
# Auxiliary space: O(1)
def num_rescue_boats(people: list[int], limit: int) -> int:
    n = len(people)
    people.sort()

    boats = 0
    lo, hi = 0, n - 1
    while lo <= hi:
        if people[lo] + people[hi] <= limit:
            lo += 1
            hi -= 1
        else:
            hi -= 1
        boats += 1

    return boats

'''
You need to make ideal pairings of people. To do this, you should try to pair
the heaviest person with the lightest person, the 2nd heaviest with the 2nd
lightest, and so on. The heaviest person has to get on a boat, right? The best
chance of putting them on a boat as part of a pair (to minimize the number of
boats) is to pair them with the lightest person. If the pair exceeds the limit,
the heavier person will have to take a boat by themselves. This means you have
to sort the array, in order to make optimal pairings.

Rearrangement inequality: given two sorted sequences, summing elements in the
same order (largest with largest) will maximize the maximum sum and summing
elements in the opposite order (smallest with largest) will minimize the
maximum sum. In this problem, we are trying to minimize the maximum sum in
order to stay under the limit and minimize the number of boats.
'''

# Time: O(nlogn)
# Auxiliary space: O(1)
def num_rescue_boats2(people: list[int], limit: int) -> int:
    n = len(people)
    people.sort()

    def can_fit(boats):
        pairs = n - boats
        for i in range(pairs):
            if people[i] + people[2 * pairs - 1 - i] > limit:
                return False
        return True

    result = 0
    left = (n + n % 2) // 2
    right = n
    while left <= right:
        mid = (left + right) // 2
        if can_fit(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

'''
This is my original solution. I was thinking this problem was going to be like
#1011, where you determine a lower and upper bound for the answer (at least 1
boat for every 2 people, at most 1 boat per person) and then binary search for
it, but it turns out this solution is actually slow because you need to
traverse the array and re-pair people each time you try a different number of
boats, so the post-sorting time complexity is nlogn, compared to n in the above
solution.

The reason binary search is not optimal here is because a greedy solution
exists. You want to make the locally optimal choice for the heaviest person
remaining, because they have the fewest number of possible partners. The
locally optimal choice is to put the heaviest person in a pair, if possible,
and the best chance of doing that is to pair them with the lightest person
remaining. Specifically, because there is a constraint of 2 people per boat and
the people can be sorted, which allows for optimal pairing, there is a greedy
solution.

By contrast, #1011 does not have a greedy solution. The items are not sorted
and an arbitrary number of items can be packed on a ship, which means that
local decisions affect future decisions. #1011 is an instance of the bin
packing problem, which is NP-hard, but the optimal solution avoids this
difficulty by defining a monotonic function of the variable to be minimized
and doing a binary search over it.
'''

if __name__ == '__main__':
    people = [3,1,7]
    limit = 7
    print(num_rescue_boats(people, limit))
