

# Spiral Matrix Traversal

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

```
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
```

You should return `[1,2,3,6,9,8,7,4,5]`.

## Solution

The basic idea is to iterate through the matrix in a spiral pattern, starting from the top-left corner. We can use four variables to keep track of the boundaries of the spiral pattern: `row_begin`, `row_end`, `col_begin`, and `col_end`.

```python
def spiral_traversal(matrix):
    res = []
    if len(matrix) == 0:
        return res
    row_begin = 0
    row_end = len(matrix) - 1
    col_begin = 0
    col_end = len(matrix[0]) - 1
```

We can then use a while loop to iterate through the matrix until all elements have been visited.

```python
while row_begin <= row_end and col_begin <= col_end:
    # iterate through the first row from left to right
    for i in range(col_begin, col_end+1):
        res.append(matrix[row_begin][i])
    row_begin += 1
```

Now we can iterate through the last column from top to bottom.

```python
    # iterate through the last column from top to bottom
    for i in range(row_begin, row_end+1):
        res.append(matrix[i][col_end])
    col_end -= 1
```

We then need to check if the row_begin is less than or equal to row_end (in case the matrix is a single row) and iterate through the last row from right to left.

```python
    # iterate through the last row from right to left
    if row_begin <= row_end:
        for i in range(col_end, col_begin-1, -1):
            res.append(matrix[row_end][i])
        row_end -= 1
```

Finally, we need to check if the col_begin is less than or equal to col_end (in case the matrix is a single column) and iterate through the first column from bottom to top.

```python
    # iterate through the first column from bottom to top
    if col_begin <= col_end:
        for i in range(row_end, row_begin-1, -1):
            res.append(matrix[i][col_begin])
        col_begin += 1

    return res
```

## Test

```python
if __name__ == "__main__":
    mat = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
    print(spiral_traversal(mat))
```

Output: `[1, 2, 3, 6, 9, 8, 7, 4, 5]`