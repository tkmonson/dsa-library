'''
Image Overlap (#835)

You are given two images, represented as binary nxn matrices. You can translate
one image by sliding all of the 1 bits left, right, up, and/or down by any
number of units. You can then place that image on top of the other image. The
overlap is the number of positions that have a 1 in both images. Any 1 bits
that are translated outside of the matrix borders are erased.

Return the largest possible overlap.
'''

from collections import defaultdict, deque

# Time: O(n^3) (visit entire translation space O(n^2), compute overlap O(n))
# Auxiliary space: O(n^2) (queue elements are O(n), queue size is O(n))
def largest_overlap(img1: list[list[int]], img2: list[list[int]]) -> int:
    n = len(img1)
    bit1, bit2 = [], []
    for i in range(n):
        bit1.append(int('0b' + ''.join(map(str, img1[i])), 2))
        bit2.append(int('0b' + ''.join(map(str, img2[i])), 2))

    q = deque([(bit1, (0, 0))])
    seen = set()
    max_overlap = 0

    while q:
        curr, op = q.popleft()
        if abs(op[0]) == n or abs(op[1]) == n:
            continue

        overlap = 0
        for i in range(n):
            overlap += (curr[i] & bit2[i]).bit_count()
        max_overlap = max(max_overlap, overlap)

        if (new_op := (op[0] + 1, op[1])) not in seen:
            right = [b >> 1 for b in curr]
            seen.add(new_op)
            q.append((right, new_op))

        if (new_op := (op[0] - 1, op[1])) not in seen:
            left = [(b << 1) & ~(1 << n) for b in curr]
            seen.add(new_op)
            q.append((left, new_op))

        if (new_op := (op[0], op[1] + 1)) not in seen:
            down = [0] + curr[:-1]
            seen.add(new_op)
            q.append((down, new_op))

        if (new_op := (op[0], op[1] - 1)) not in seen:
            up = curr[1:] + [0]
            seen.add(new_op)
            q.append((up, new_op))

    return max_overlap

'''
In the brute-force solution, traversing the translation space is O(n^2) and
computing the overlap is O(n^2). The translation space must be searched
exhaustively, so its complexity cannot be lowered. But the complexity of
computing the overlap can be lowered by flattening one of the dimensions of the
matrices. Each row can be transformed into a bitmask, and the overlap can be
computed using bitwise logic. Horizontal translation can be done with bit
shifting. Thus, the complexity of computing the overlap is lowered to O(n).
This also lowers the space complexity of the queue to O(n^2).
'''

# Time: O(n^4)
# Auxiliary space: O(1)
def largest_overlap2(img1: list[list[int]], img2: list[list[int]]) -> int:
    n = len(img1)
    max_overlap = 0

    for i in range(-n + 1, n):
        for j in range(-n + 1, n):
            overlap = 0
            for r in range(n):
                if (r + i) < 0 or (r + i) >= n:
                    continue
                for c in range(n):
                    if (c + j) < 0 or (c + j) >= n:
                        continue
                    if img2[r][c] and img1[r + i][c + j] == img2[r][c]:
                        overlap += 1
            max_overlap = max(max_overlap, overlap)

    return max_overlap

'''
Traverse the translation space left-to-right, top-to-bottom. At each cell in
the translation space, compute the overlap (skip cells of img1 that are outside
of the bounds of img2).
'''

# Time: O(n^4)
# Auxiliary space: O(n^2)
def largest_overlap3(img1: list[list[int]], img2: list[list[int]]) -> int:
    n = len(img1)
    points1, points2 = [], []
    vectors = defaultdict(lambda: 0)

    for r in range(n):
        for c in range(n):
            if img1[r][c]:
                points1.append((r, c))
            if img2[r][c]:
                points2.append((r, c))

    for p1 in points1:
        for p2 in points2:
            vectors[(p2[0] - p1[0], p2[1] - p1[1])] += 1

    max_vector_count = 0
    for v in vectors:
        max_vector_count = max(max_vector_count, vectors[v])

    return max_vector_count

'''
A 1 in img1[i][j] will overlap a 1 in img2[x][y] when it is translated by a
vector from (i, j) to (x, y). But all of the 1s in img1 must be translated
together. Thus, there is one vector that, when used to translate all of the 1s
in img1, will maximize the overlap.

Find the vectors from every 1 in img1 to every 1 in img2. Count instances of
the same vector. Return the highest count.
'''

# Time: O(n^4) (visit entire translation space O(n^2), compute overlap O(n^2))
# Auxiliary space: O(n^3) (queue elements are O(n^2), queue size is O(n))
def largest_overlap4(img1: list[list[int]], img2: list[list[int]]) -> int:
    n = len(img1)
    q = deque([(img1, (0, 0))])
    seen = set([(0, 0)])
    max_overlap = 0

    while q:
        img, op = q.popleft()
        if abs(op[0]) == n or abs(op[1]) == n:
            continue

        overlap = 0
        for i in range(n):
            for j in range(n):
                overlap += img[i][j] & img2[i][j]
        max_overlap = max(max_overlap, overlap)

        if (new_op := (op[0] + 1, op[1])) not in seen:
            right = [[0] + r[:-1] for r in img]
            seen.add(new_op)
            q.append((right, new_op))

        if (new_op := (op[0] - 1, op[1])) not in seen:
            left = [r[1:] + [0] for r in img]
            seen.add(new_op)
            q.append((left, new_op))

        if (new_op := (op[0], op[1] + 1)) not in seen:
            down = [[0] * n] + img[:-1]
            seen.add(new_op)
            q.append((down, new_op))

        if (new_op := (op[0], op[1] - 1)) not in seen:
            up = img[1:] + [[0] * n]
            seen.add(new_op)
            q.append((up, new_op))

    return max_overlap

'''
The brute-force solution. We need to check every possible overlapping of img1
on img2. We can do this in a BFS or DFS manner. If we define the overlapping of
the original img1 on img2 as the center (0, 0), then a 1-unit translation of
img1 right is (1, 0) and a 1-unit translation of img1 up is (0, -1) and so on.
We can keep track of the state of img1 at each step of the search of the
translation space (mxm where m = 2n - 1).
'''

if __name__ == '__main__':
    img1 = [[1, 1, 0],
            [0, 1, 0],
            [0, 1, 0]]
    img2 = [[0, 0, 0],
            [0, 1, 1],
            [0, 0, 1]]
    print(largest_overlap3(img1, img2))

