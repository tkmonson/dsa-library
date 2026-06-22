'''
Top K Frequent Elements (#347)

Given an integer array `nums` and an integer `k`, return the `k` most frequent
elements. You may return the answer in any order.
'''

from collections import Counter

def top_k_frequent_elements(nums: list[int], k: int) -> list[int]:
    c = Counter(nums)
    buckets = [[] for _ in range(len(nums))]
    for n in c:
        buckets[c[n] - 1].append(n)

    result = [] 
    for i in range(len(buckets) - 1, -1, -1):
        while buckets[i] and len(result) < k:
            result.append(buckets[i].pop())
        if len(result) == k:
            break

    return result

'''
Get counts
Create a list of len(nums) buckets
Group the elements in the buckets by their frequency
Return k of the elements in descending order of frequency
'''

if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(top_k_frequent_elements(nums, k))

