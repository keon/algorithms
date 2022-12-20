
# Inverting an n x n Matrix

Inverting an invertible n x n matrix is a four step process that can be done with the following steps:

1. Calculate the matrix of minors: Create an n x n matrix by considering each position in the original matrix in turn. Exclude the current row and column and calculate the determinant of the remaining matrix, then place that value in the current position's equivalent in the matrix of minors.
2. Create the matrix of cofactors: Take the matrix of minors and multiply alternate values by -1 in a checkerboard pattern.
3. Adjugate: Hold the top left to bottom right diagonal constant, but swap all other values over it.
4. Multiply the adjugated matrix by 1 / the determinant of the original matrix.

This code combines steps 1 and 2 into one method to reduce traversals of the matrix:

```python
def get_matrix_of_minors(m):
    """get the matrix of minors and alternate signs"""
    matrix_of_minors = [[0 for i in range(len(m))] for j in range(len(m))]
    for row in range(len(m)):
        for col in range(len(m[0])):
            if (row + col) % 2 == 0:
                sign = 1
            else:
                sign = -1
            matrix_of_minors[row][col] = sign * get_determinant(get_minor(m, row, col))
    return matrix_of_minors
```

For a 2 x 2 matrix, inversion is simpler. The code for this is as follows:

```python
if len(m) == 2:
    # simple case
    multiplier = 1 / get_determinant(m)
    inverted = [[multiplier] * len(m) for n in range(len(m))]
    inverted[0][1] = inverted[0][1] * -1 * m[0][1]
    inverted[1][0] = inverted[1][0] * -1 * m[1][0]
    inverted[0][0] = multiplier * m[1][1]
    inverted[1][1] = multiplier * m[0][0]
    return inverted
```

Possible edge cases: will not work for 0x0 or 1x1 matrix, though these are trivial to calculate without use of this file.