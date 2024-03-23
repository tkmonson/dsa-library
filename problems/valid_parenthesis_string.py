'''
Valid Parenthesis String (#678)

Given a string `s` of characters '(', ')', and '*', where '*' can reduce to
'(', ')', or '', return True if `s` can be a valid parenthesis string.
'''

# Time: O(n)
# Auxiliary space: O(1)
def check_valid_string(s: str) -> bool:
    left_min, left_max = 0, 0
    for c in s:
        if c == '(':
            left_min += 1
            left_max += 1
        elif c == ')':
            left_min -= 1
            left_max -= 1
        else:
            left_min -= 1
            left_max += 1

        if left_max < 0:
            return False
        if left_min < 0:
            left_min = 0

    return left_min == 0

'''
[left_min, left_max] represents the range of possible values for the number of
open left parentheses. When given a choice (when the current character is '*'),
we prefer to decrement left_min by choosing ')' and increment left_max by
choosing '('.

The last two conditionals are hard to understand. Here are some statements that
are intended to give intuition:

If you have too many ')' at some point, left_max will be less than 0 => False.
If you have more than enough '*' at some point, left_min will be less than 0
    => some of the '*' can be ''
    => we don't need to decrement left_min for those '*'
    => left_min can be 0.

left_max: spamming '(', if it still becomes < 0 because of too many ')', False
left_min: spamming ')', if it becomes < 0 because not enough '(', then we don't
          have to spam so hard (some '*' can be '')
'''

# Time: O(n^2) (would be 3^n without caching)
# Auxiliary space: O(n^2)
def check_valid_string2(s: str) -> bool:
    @cache
    def f(i, t):  # t = number of open left parentheses
        if i == len(s) or t < 0:
            return t == 0
        if s[i] == '(':
            return f(i + 1, t + 1)
        if s[i] == ')':
            return f(i + 1, t - 1)
        return f(i + 1, t + 1) or f(i + 1, t) or f(i + 1, t - 1)
    return f(0, 0)

'''
A backtracking solution. At each '*', explore each path: '(', ')', and ''. With
each call, we move forward in the string by one character, and we could choose
to increment t every time or decrement t every time. So the maximum size of the
cache is n^2, but it would look like this:

    t
    |       *
    |     * *
    |   * * *
    | * * * *
    * * * * * -- i
      * * * *
        * * *
          * *
            *
'''

if __name__ == '__main__':
    s = '(*)))(*)'
    s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
    s = '(*)('
    print(check_valid_string(s))

