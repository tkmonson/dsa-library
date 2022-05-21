'''
Dam Design (from Fathom test 04/22)

A company is designing a dam made of one or more concrete walls with mud
segments packed in between them. Each wall and mud segment has a width of 1
unit, and the height of a mud segment cannot exceed 1 unit more than that of an
adjacent wall or mud segment. Given the positions and heights of the walls,
return the maximum height of a mud segment that can be built. If no mud segment
can be built, return 0.

-------------------------------------------------------------------------------

     #              # = wall, . = mud
    .#              Ex. 1: [1, 6], [3, 8] => gap = 4, dh = 5
   ..#       .      Ex. 2: [1, 6], [3, 5] => gap = 4, dh = 1
  ...#      ...
 ....#     ....#    Note that when the difference in the height of the walls
#....#    #....#    is greater than the width of the gap between the walls
#....#    #....#    (dh > gap), there is an upper limit on the height of a mud
#....#    #....#    segment between said walls: the height of the lower wall
                    plus the width of the gap (h_lo + gap). When dh < gap, a
portion of the gap (dh) can be used to increment mud segments up to the height
of the higher wall (h_hi). From here, consider the subproblem of two walls of
height h_hi separated by the remaining gap (gap - dh), within which mud
segments may increment up to the midpoint before decrementing. Thus, the
maximum height of a mud segment in this case is h_hi + (gap - dh + 1) // 2.
When dh = gap, both formulas produce the same answer.
'''

def max_mud_height(wall_positions, wall_heights):
    h_mud_max = 0
    for i in range(len(wall_positions) - 1):
        gap = wall_positions[i + 1] - wall_positions[i] - 1
        h_lo = min(wall_heights[i + 1], wall_heights[i])
        h_hi = max(wall_heights[i + 1], wall_heights[i])
        dh = h_hi - h_lo
        h_mud = h_lo + gap if dh > gap else h_hi + (gap - dh + 1) // 2
        h_mud_max = max(h_mud_max, h_mud)
    return h_mud_max

if __name__ == '__main__':
    print(max_mud_height([1,11], [3,10]))

