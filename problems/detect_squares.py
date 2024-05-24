'''
Detect Squares (#2013)

You are given a stream of points on the xy plane. Design an algorithm that:

1. Adds new points from the stream into a data structure. Duplicate points are
   allowed and should be treated as different points.
2. Given a query point, counts the number of ways to choose three points from
   the data structure such that the three points and the query point form an
   axis-aligned square with positive area.

An axis-aligned square is a square whose edges are all the same length and are
either parallel or perpendicular to the x-axis and y-axis.
'''

from collections import defaultdict

class DetectSquares:
    def __init__(self):
        self.ys = defaultdict(lambda: set())
        self.pt_count = defaultdict(lambda: 0)

    def add(self, point: list[int]) -> None:
        self.ys[point[0]].add(point[1])
        self.pt_count[tuple(point)] += 1

    def count(self, point: list[int]) -> int:
        qx, qy = point
        total = 0
        for y in self.ys[qx]:
            if y == qy:
                continue
            c1 = self.pt_count[(qx, y)]
            up = qy - y > 0
            d = abs(qy - y)
            for x in [qx - d, qx + d]:
                c2 = self.pt_count[(x, qy)]
                c3 = self.pt_count[(x, qy - d if up else qy + d)]
                total += c1 * c2 * c3
        return total

'''
Given a query point (qx, qy), consider all points where x = qx. Below, if the
query point is Q, these points would be B and G. If the point being considered
is B (higher than Q), then the diagonal point we are looking for is A or C. If
the point is G (lower than Q), then the diagonal point is F or H.

A     B     C


D     Q     E


F     G     H
'''

if __name__ == '__main__':
    ds = DetectSquares()
    ds.add([3, 10])
    ds.add([11, 2])
    ds.add([3, 2])
    print(ds.count([11, 10]))
    print(ds.count([14, 8]))
    ds.add([11, 2])
    print(ds.count([11, 10]))

