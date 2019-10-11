"""
You are given an n x n 2D mat representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""


# clockwise rotate
# first reverse up to down, then swap the symmetry
# 1 2 3     7 8 9     7 4 1
# 4 5 6  => 4 5 6  => 8 5 2
# 7 8 9     1 2 3     9 6 3

def rotate(mat):
    if not mat:
        return mat
    mat.reverse()
    for i in range(len(mat)):
        for j in range(i):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    return mat


if __name__ == "__main__":
    mat = [[1,2,3],
           [4,5,6],
           [7,8,9]]
    print(mat)
    rotate(mat)
    print(mat)
