'''
Matchsticks to Square (#473)

You are given an integer array `matchsticks` where `matchsticks[i]` is the
length of the ith matchstick. You want to use all the matchsticks to make one
square. You should not break any stick, but you can link them up, and each
matchstick must be used exactly one time.

Return True if you can make this square and False otherwise.
'''

# Time: O(4^n)
# Auxiliary space: O(n)
def make_square(matchsticks: list[int]) -> bool:
    total = sum(matchsticks)
    if (target := total // 4) != total / 4:
        return False

    matchsticks.sort(reverse=True)
    if matchsticks[0] > target:
        return False

    sides = [0, 0, 0, 0]
    def dfs(i):
        if i == len(matchsticks):
            return True
        
        for j in range(4):
            if sides[j] + matchsticks[i] <= target:
                sides[j] += matchsticks[i]
                if dfs(i + 1):
                    return True
                sides[j] -= matchsticks[i]

            if sides[j] == 0:
                break

        return False
    
    return dfs(0)

'''
Basic backtracing solution. It's important to sort in descending order because
larger sticks are harder to place, so you will fail and backtrack faster. It
also allows you to check for a stick that is larger than the target.

`if sides[j] == 0: break` is also very important. If you tried including and
not including a stick in an empty side, that means your mistake is located
further up the call stack and you need to backtrack.
'''

# Time: O(4^n)
# Auxiliary space: O(n)
def make_square2(matchsticks: list[int]) -> bool:
    total = sum(matchsticks)
    if (target := total // 4) != total / 4:
        return False

    matchsticks.sort(reverse=True)
    if matchsticks[0] > target:
        return False

    sides = [0, 0, 0, 0]
    indexes = set()
    def dfs(i, s):
        if s == 4:
            return True
        if sides[s] == target:
            return dfs(0, s + 1)
        if i == len(matchsticks):
            return False
        if i in indexes:
            return dfs(i + 1, s)
            
        sides[s] += matchsticks[i]
        indexes.add(i)
        if sides[s] <= target and dfs(i + 1, s):
            return True
        sides[s] -= matchsticks[i]
        indexes.remove(i)

        if sides[s] == 0:
            return False

        return dfs(i + 1, s)
    
    return dfs(0, 0)

'''
This solution is faster because it fills a side completely before considering
the other sides. This avoids wasting time exploring states of partially filled
sides that will not resolve.
'''

if __name__ == '__main__':
    matchsticks = [5,5,5,5,4,4,4,4,3,3,3,3]
    print(make_square(matchsticks))

'''
Backtracking optimization lessons:

Sort the input so you first consider the elements that are more likely to lead
to failure. You want to fail fast to avoid wasting time on configurations that
will fail close to the end.

If you take an element into an empty partition and all paths after that
decision lead to failure, there is no point taking any other remaining element
into the empty set. Your mistake is further up and you need to backtrack.

When solving a partition problem, it is usually faster to fill a partition
completely before trying to add elements to any other partitions.
'''
