"""
Matrix Exponentiation

Compute the n-th power of a square matrix using repeated squaring
(exponentiation by squaring). Useful for computing Fibonacci numbers,
linear recurrences, and graph path counting.

Reference: https://en.wikipedia.org/wiki/Exponentiation_by_squaring

Complexity:
    Time:  O(d^3 * log n)  where d is the matrix dimension
    Space: O(d^2)
"""

from __future__ import annotations


def multiply(mat_a: list[list[int]], mat_b: list[list[int]]) -> list[list[int]]:
    """Multiply two square matrices.

    Args:
        mat_a: First square matrix (n x n).
        mat_b: Second square matrix (n x n).

    Returns:
        Product matrix of mat_a and mat_b.

    Examples:
        >>> multiply([[1, 0], [0, 1]], [[2, 3], [4, 5]])
        [[2, 3], [4, 5]]
    """
    size = len(mat_a)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += mat_a[i][k] * mat_b[k][j]
    return result


def identity(size: int) -> list[list[int]]:
    """Return the identity matrix of the given size.

    Args:
        size: Dimension of the identity matrix.

    Returns:
        Identity matrix of size n x n.

    Examples:
        >>> identity(3)
        [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    """
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        result[i][i] = 1
    return result


def matrix_exponentiation(mat: list[list[int]], power: int) -> list[list[int]]:
    """Compute mat raised to the given power by repeated squaring.

    Args:
        mat: Square matrix to exponentiate.
        power: Non-negative integer exponent.

    Returns:
        Matrix mat^power.

    Examples:
        >>> matrix_exponentiation([[1, 0], [0, 1]], 5)
        [[1, 0], [0, 1]]
    """
    if power == 0:
        return identity(len(mat))
    elif power % 2 == 1:
        return multiply(matrix_exponentiation(mat, power - 1), mat)
    else:
        half = matrix_exponentiation(mat, power // 2)
        return multiply(half, half)
