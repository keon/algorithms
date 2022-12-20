
# Matrix Exponentiation

Matrix exponentiation is a technique used to calculate a matrix raised to the power of n, where n is a positive integer. This technique can be used to solve problems in various fields, such as graph theory.

## Algorithm

The algorithm for matrix exponentiation is based on repeated squaring. We start by raising the matrix to the power of 2, and then raising the result to the power of 4, then 8 and so on, until we reach the desired power.

For example, to calculate the matrix raised to the power of 9, we can calculate it as follows:

`matrix_exponentiation(mat, 9)`

= `multiply(matrix_exponentiation(mat, 8), mat)`

= `multiply(multiply(matrix_exponentiation(mat, 4), matrix_exponentiation(mat, 4)), mat)`

= `multiply(multiply(multiply(matrix_exponentiation(mat, 2), matrix_exponentiation(mat, 2)), matrix_exponentiation(mat, 2)), mat)`

## Code Snippet

The code snippet below implements the matrix exponentiation algorithm in Python.

```python
def multiply(matA: list, matB: list) -> list:
    """
    Multiplies two square matrices matA and matB od size n x n
    Time Complexity: O(n^3)
    """
    n = len(matA)
    matC = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                matC[i][j] += matA[i][k] * matB[k][j]

    return matC


def identity(n: int) -> list:
    """
    Returns the Identity matrix of size n x n
    Time Complexity: O(n^2)
    """
    I = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        I[i][i] = 1

    return I


def matrix_exponentiation(mat: list, n: int) -> list:
    """
    Calculates mat^n by repeated squaring
    Time Complexity: O(d^3 log(n))
                     d: dimension of the square matrix mat
                     n: power the matrix is raised to
    """
    if n == 0:
        return identity(len(mat))
    elif n % 2 == 1:
        return multiply(matrix_exponentiation(mat, n - 1), mat)
    else:
        tmp = matrix_exponentiation(mat, n // 2)
        return multiply(tmp, tmp)
```

## Time Complexity

The time complexity of the matrix exponentiation algorithm is O(d<sup>3</sup> log(n)), where d is the dimension of the square matrix mat and n is the power the matrix is raised to.