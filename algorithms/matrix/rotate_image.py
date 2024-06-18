"""
You are given an n x n 2D mat representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""

branch_coverage = {
    "rotate_matrix_1": False,  # if not branch for mat
    "rotate_matrix_2": False,  # invisible else branch
    "rotate_matrix_3": False,  # for branch
    "rotate_matrix_4": False,  # for branch

}

# clockwise rotate
# first reverse up to down, then swap the symmetry
# 1 2 3     7 8 9     7 4 1
# 4 5 6  => 4 5 6  => 8 5 2
# 7 8 9     1 2 3     9 6 3

def rotate(mat):
    if not mat:
        branch_coverage["rotate_matrix_1"] = True
        return mat

    branch_coverage["rotate_matrix_2"] = True

    mat.reverse()
    for i in range(len(mat)):
        branch_coverage["rotate_matrix_3"] = True

        for j in range(i):
            branch_coverage["rotate_matrix_4"] = True

            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    return mat

def print_coverage():
    for branch, hit in branch_coverage.items():
        print(f"{branch} was {'hit' if hit else 'not hit'}")
        total = len(branch_coverage)
        hit = sum(branch_coverage.values())
        result = hit / total * 100

    print("The total branch coverage is:", result, "%")

rotate([])
print_coverage()
print("\n")
print_coverage()
rotate([[1, 2], [3, 4]])
print("\n")
print_coverage()
rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n")



