'''
Longest Repeating Character Replacement (#424)

Given a string of uppercase letters and an integer `k`, you may replace any
character in the string with a different uppercase letter at most `k` times.
After replacement, return the length of the longest substring containing the
same letter.
'''

from collections import defaultdict

# Time: O(n)
# Auxiliary space: O(n)
def longest_repeating_character_replacement(s: str, k: int) -> int:
    count = defaultdict(lambda: 0)
    left = 0
    mode_count = 0

    for right in range(len(s)):
        count[s[right]] += 1
        mode_count = max(mode_count, count[s[right]])

        if (right - left + 1) - mode_count > k:
            count[s[left]] -= 1
            left += 1

    return (right - left + 1)

'''
The mode of a substring is the most common letter. A substring is only valid if
it has k or fewer letters that differ from the mode.

Expand a sliding window to the right. Keep track of the count of the mode. If
the number of letters in the window minus the count of the mode is greater than
k, shrink the sliding window from the left.

Note that the sliding window will always end at the end of the string. It does
not represent the actual longest substring containing the same letter after
replacement. It simply keeps track of how many times you need to shrink the
window while expanding to the right to stay under k replacements.
'''

if __name__ == '__main__':
    s = 'AABABBA'
    k = 1
    print(longest_repeating_character_replacement(s, k))

