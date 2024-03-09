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
            print('Key %s found at row- %s column- %s' % (key, i+1, j+1))
            return
        if key < mat[i][j]:
            i -= 1
        else:
            j += 1
    print('Key %s not found' % (key))


def main():
    mat = [
           [2, 5, 7],
           [4, 8, 13],
           [9, 11, 15],
           [12, 17, 20]
          ]
    key = 13
    print(mat)
    search_in_a_sorted_matrix(mat, len(mat), len(mat[0]), key)


if __name__ == '__main__':
    main()
