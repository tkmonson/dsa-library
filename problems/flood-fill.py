'''
Flood Fill (#733)

Given an integer matrix of pixel values `image`, a start row index `sr`, a
start column index `sc`, and an integer `color`, perform a flood fill starting
at pixel `image[sr][sc]`. That is, change the color of the starting pixel, plus
any pixels connected 4-directionally to the starting pixel of the same color as
the starting pixel, plus any pixels connected 4-directionally to those pixels
(also of the same color), and so on. Return the modified image.
'''

from collections import deque

def flood_fill_dfs(image: list[int], sr: int, sc: int,
               color: int) -> list[list[int]]:
    def dfs(r, c):
        if image[r][c] == start_color:
            image[r][c] = color
            if c < len(image[0]) - 1:
                dfs(r, c + 1)
            if r > 0:
                dfs(r - 1, c)
            if c > 0:
                dfs(r, c - 1)
            if r < len(image) - 1:
                dfs(r + 1, c)

    start_color = image[sr][sc]
    if color != start_color:
        dfs(sr, sc)
    return image


def flood_fill_bfs(image: list[int], sr: int, sc: int,
               color: int) -> list[list[int]]:
    start_color = image[sr][sc]
    if color != start_color:
        image[sr][sc] = color
        queue = deque([(sr, sc)])
        while queue:
            (r, c) = queue.popleft()
            if c < len(image[0]) - 1 and image[r][c + 1] == start_color:
                image[r][c + 1] = color
                queue.append((r, c + 1))
            if r > 0 and image[r - 1][c] == start_color:
                image[r - 1][c] = color
                queue.append((r - 1, c))
            if c > 0 and image[r][c - 1] == start_color:
                image[r][c - 1] = color
                queue.append((r, c - 1))
            if r < len(image) - 1 and image[r + 1][c] == start_color:
                image[r + 1][c] = color
                queue.append((r + 1, c))
    return image


if __name__ == '__main__':
    image = [[1, 1, 1],
             [1, 1, 0],
             [1, 0, 1]]
    sr, sc, color = 1, 1, 2
    print(flood_fill_bfs(image, sr, sc, color))

