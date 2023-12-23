'''
Happy Number (#202)

Given a number, return whether or not it is happy. A happy number is defined by
the following process:

    * Starting with any positive integer, replace the number with the sum of
      the squares of its digits.
    * Repeat the process until the number equals 1 (where it will stay) or it
      loops endlessly in a cycle which does not include 1.
    * Those numbers for which this process ends in 1 are happy.
'''

# Time: O(n)
# Auxiliary space: O(1)
def is_happy(n: int) -> bool:
    def f(n):
        result = 0
        while n > 0:
            d = n % 10
            result += d * d
            n //= 10
        return result

    slow, fast = f(n), f(f(n))
    while slow != fast and fast != 1:
        slow, fast = f(slow), f(f(fast))

    return fast == 1

'''
This is an application of Floyd's Tortoise and Hare Cycle Detection algorithm,
but it is simplified because we don't need to know where the entrance to a
potential cycle is located, we only need to know whether or not such a cycle
exists. Thus, we can just run a slow and fast pointer, and if there is a cycle,
they will eventually intersect. If not, the fast pointer will hit 1 first.
'''

# Time: O(n)
# Auxiliary space: O(n)
def is_happy2(n: int) -> bool:
    seen = set()
    while n not in seen and n != 1:
        seen.add(n)
        new = 0
        for d in str(n):
            new += int(d) ** 2
        n = new

    return n == 1


if __name__ == '__main__':
    n = 19
    print(is_happy(n))

