'''
Pacific Atlantic Water Flow (#417)

There is an mxn rectangular island bordered on the top and left by the Pacific
Ocean and on the bottom and right by the Atlantic Ocean. When it rains on the
island, water will flow from a current cell to an adjacent cell if the adjacent
cell's height is less than or equal to the current cell's height, and water
will flow from any cell adjacent to an ocean into that ocean. Given an mxn
integer matrix `heights` that represents the height above sea level for each
cell on the island, return a list of grid coordinates `result` where
`result[i] = [r_i, c_i]` denotes that water can flow from cell `(r_i, c_i)` to
both the Pacific and Atlantic oceans.
'''

def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    if not heights:
        return []

    p_land = set()
    a_land = set()
    R, C = len(heights), len(heights[0])

    def spread(i, j, land):
        land.add((i, j))
        for r, c in ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)):
            if (0 <= r < R and 0 <= c < C and heights[r][c] >= heights[i][j]
                    and (r, c) not in land):
                spread(r, c, land)
                
    for i in range(R):
        spread(i, 0, p_land)
        spread(i, C - 1, a_land)

    for j in range(C):
        spread(0, j, p_land)
        spread(R - 1, j, a_land)

    return [[r, c] for r, c in p_land & a_land]

'''
Envision rain falling on a mountainous island but with time running in reverse.
At each cell adjacent to an ocean, water will rise up out of the ocean and
spread into any adjacent cell of greater or equal height. And it will spread in
a similar way at any new cell that it spreads into. And if it cannot spread in
any direction at some cell (i.e. it has arrived at a local maximum), it will
then separate into raindrops and fly upward toward the clouds.

This algorithm simulates this behavior by running this spreading process at
each cell adjacent to an ocean. This is a DFS implementation, but BFS should
work as well.
'''

if __name__ == '__main__':
    heights = [
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
    ]
    print(pacific_atlantic(heights))

