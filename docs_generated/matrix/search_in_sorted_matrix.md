
# Searching in a Sorted Matrix
Given a (row-wise and column-wise) sorted matrix, we need to search a key in it.

The time complexity of searching in a sorted matrix is **O(m + n)**, where m is the number of rows and n is the number of columns in the matrix. 

## Algorithm

1. Start with the top right element in the matrix.
2. If the key is larger than the current element, move one column to the left.
3. If the key is smaller than the current element, move one row down.
4. Repeat steps 2 and 3 until the key is found or the matrix boundaries are reached.

## Implementation

```
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
```

Let us consider a matrix `mat` as shown below:

```
mat = [
           [2, 5, 7],
           [4, 8, 13],
           [9, 11, 15],
           [12, 17, 20]
          ]
```

To search for the key `13` in the matrix, we have to execute the following code:

```
key = 13
search_in_a_sorted_matrix(mat, len(mat), len(mat[0]), key)
```

The output of the above code would be:

```
Key 13 found at row- 2 column- 3
```