'''
Container With Most Water (#11)

You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of the ith line are (i, 0) and
(i, height[i]). Find two lines that together with the x-axis form a container,
such that the container contains the most water. Return the maximum amount of
water a container can store.

E.g. height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    *                   *
    *-------------------*-------*
    *   *               *       *
    *   *       *       *       *
    *   *       *   *   *       *    =>  max water = 7 x 7 = 49
    *   *       *   *   *   *   *
    *   *   *   *   *   *   *   *
*   *   *   *   *   *   *   *   *
'''

def max_area(height: list[int]) -> int:
    area = 0
    left, right = 0, len(height) - 1
    while left < right:
        x = right - left
        y1, y2 = height[left], height[right]
        if y1 < y2:
            area = max(area, x * y1)
            left += 1
        else:
            area = max(area, x * y2)
            right -= 1
    return area


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(max_area(height))

'''
The naive solution is to check all pairs of vertical lines, (0, 1) to
(0, n - 1), (1, 2) to (1, n - 1), ..., (n - 2, n - 1).

The better solution comes from realizing that you are trying to maximize x*y.
Start with the maximum possible x by setting a left pointer at 0 and a right
pointer at n - 1. As x decrements, you would like y to increase. Because
y = min(h[left], h[right]), only moving the pointer pointing to the smaller
height can possibly yield a greater area. This is a greedy algorithm: trying to
increase the area at each step will eventually produce the largest possible
area.
'''

