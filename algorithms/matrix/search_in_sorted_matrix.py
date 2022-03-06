#
# Search a key in a row wise and column wise sorted (non-decreasing) matrix.
# m- Number of rows in the matrix
# n- Number of columns in the matrix
# T(n)- O(m+n)
#


def search_in_a_sorted_matrix(mat, m, n, key):
    i, j = m-1, 0
    while i >= 0 and j < n:
        if key == mat[i][j]:
            position = [i+1, j+1]
            return position
        if key < mat[i][j]:
            i -= 1
        else:
            j += 1
    raise Exception('Key not found')

