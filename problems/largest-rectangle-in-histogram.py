'''
Largest Rectangle in Histogram (#84)

Given an array of integers `heights` representing the heights of bars in a
histogram, where each bar has a width of 1, return the area of the largest
rectangle in the histogram.

E.g. heights = [2, 1, 5, 6, 2, 3] => 10

        *
      o o
      o o
      o o   *
  *   o o * *
  * * o o * *
'''

import heapq

# Time: O(n)
# Auxiliary space: O(n)
def largest_rectangle_area(heights: list[int]) -> int:
    max_area = 0
    stack = []

    for curr_i, curr_h in enumerate(heights):
        start = curr_i
        while stack and stack[-1][1] >= curr_h:
            pop_i, pop_h = stack.pop()
            max_area = max(max_area, pop_h * (curr_i - pop_i))
            start = pop_i
        stack.append((start, curr_h))

    for i, h in stack:
        max_area = max(max_area, h * (len(heights) - i))

    return max_area

'''
Three simple examples:

      *  The left bar can extend into the right bar to make a rectangle of
    * *  height 1 and width 2.

    * *  The left bar can extend into the right bar to make a rectangle of
    * *  height 2 and width 2.

    *    The left bar cannot extend into the right bar because the right bar is
    * *  shorter. But the right bar can extend back into the left bar to make a
         rectangle of height 1 and width 2.

A more complicated example:

    Ideally, to find the largest rectangle that starts at index i and has
    height h[i], we would draw this rectangle all the way to the end. But
    really, if we run into a bar with a shorter height, we have to stop the
    rectangle right before it.

          *    Bar 3 cannot extend into bar 4; the largest height-4 rectangle
        * *    starting at 3 has width 1. Bar 2 cannot extend into bar 4; the
      * * * *  largest height-3 rectangle starting at 2 has width 2. But bar 4
    * * * * *  can extend back into bars 3 and 2 to make a rectangle of height
    0 1 2 3 4  2 and width 3, starting at 2. (There is no need to extend back
               further into bar 1 because bar 1 can already extend forward into
    bar 4.) Finally, there are three rectangles (i, h, w) that extend all the
    way to the end: (0, 1, 5), (1, 2, 4), and (2, 2, 3).

The optimal solution uses a monotonically increasing stack. As the bars are
linearly traversed, each height is pushed to the stack if it is greater than or
equal to the height at the top of the stack. Otherwise, heights are popped from
the stack until this condition is met, and each time a height is popped, an
area is calculated for the rectangle of that height that extends to the current
index. Indicies are stored in the stack alongside heights in order to calculate
width. Once enough heights have been popped such that the new height can be
pushed to the stack, it is paired with the index of the most recently popped
height, to signify that the rectangle has "extended back" to that point. After
traversing the bars, pairs left in the stack represent rectangles that can be
drawn all the way to the end.

For each bar i, exactly one rectangle is evaluated. If h[i] >= h[i - 1] (or
i = 0), it is the largest rectangle of height h[i] that starts at i. If
h[i] < h[i - 1], it is the largest rectangle of height h[i] that starts at j,
where j is the index of the leftmost bar in the largest subarray h[j : i] of
bars that are taller than bar i.
'''

if __name__ == '__main__':
    heights = [2, 1, 5, 6, 2, 3]
    print(largest_rectangle_area(heights))

