'''
Pairs of Songs with Total Durations Divisible by 60

Given a list of song durations in seconds, return the number of pairs of songs
whose combined duration is divisible by 60 (the number of index pairs i, j such
that i < j and (time[i] + time[j]) % 60 = 0).
'''

import math

def num_pairs_divisible_by_60(time: list[int]) -> int:
    num_pairs = 0
    d = {}
    for t in time:
        d[t % 60] = d.get(t % 60, 0) + 1
    for key in d.keys():
        if key == 0 or key == 30:
            num_pairs += math.comb(d[key], 2)
        else:
            num_pairs += d[key] * d.get(60 - key, 0)
            if 60 - key in d:
                d[60 - key] = 0
    return num_pairs

if __name__ == '__main__':
    print(num_pairs_divisible_by_60([30, 20, 150, 100, 40]))

