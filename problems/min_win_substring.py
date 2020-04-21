def min_win_substring(full_string, target):
    target_set = set(target)
    left = 0
    right = len(full_string) + 1
    for p1 in range(len(full_string)):
        target_set = set(target)
        for p2 in range(p1, len(full_string)):
            if full_string[p2] in target_set:
                target_set.remove(full_string[p2]) 
            if len(target_set) == 0:
                if (p2 - p1) < (right - left):
                    left = p1
                    right = p2
                break
    return full_string[left:right+1]

print(min_win_substring("ADOBECODEBANC", "ABC"))
