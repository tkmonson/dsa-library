'''
Merge Triplets to Form Target Triplet (#1899)

You are given an array `triplets` where `triplets[i] = [a_i, b_i, c_i]` is the
ith triplet. You are also given an array `target = [x, y, z]`. You can perform
the following operation zero or more times:
    
    Given two distinct indicies `i` and `j`, update `triplets[j]` to
    `[max(a_i, a_j), max(b_i, b_j), max(c_i, c_j)]`.
    
Return whether it is possible to obtain `target` as an element of `triplets`.
'''

def merge_triplets(triplets: list[list[int]], target: list[int]) -> bool:
    curr = [0, 0, 0]
    i = 0
    while curr != target:
        try:
            t = triplets[i]
        except IndexError:
            return False
        if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
            curr = [max(t[0], curr[0]), max(t[1], curr[1]), max(t[2], curr[2])]
        i += 1
                
    return True


if __name__ == '__main__':
    triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
    target = [2, 7, 5]
    print(merge_triplets(triplets, target))

