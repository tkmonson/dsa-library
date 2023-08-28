'''
3D Surface Area

Given a 2D board (array) A of size H (rows) x W (columns), where each cell
(i, j) has an integer A_ij (>= 1) that represents the number of 1 x 1 x 1 cubes
stacked on that cell, return the surface area of the described 3D shape.
'''

def surface_area(A: list[list[int]]) -> int:
    H, W = len(A), len(A[0])
    lateral_area = 0
    for r in range(H):
        for c in range(W):
            z = A[r][c]
            top_z = A[r - 1][c] if r > 0 else 0
            bottom_z = A[r + 1][c] if r < H - 1 else 0
            left_z = A[r][c - 1] if c > 0 else 0
            right_z = A[r][c + 1] if c < W - 1 else 0
            for z2 in [top_z, bottom_z, left_z, right_z]:
                diff_z = z - z2
                lateral_area += diff_z if diff_z > 0 else 0
    return 2*H*W + lateral_area

if __name__ == '__main__':
    print(surface_area([[1,3,4],[2,2,3],[1,2,4]]))

