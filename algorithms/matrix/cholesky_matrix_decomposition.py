"""
Cholesky Matrix Decomposition

Decompose a Hermitian positive-definite matrix A into a lower-triangular
matrix V such that V * V^T = A. Mainly used for numerical solution of
linear equations Ax = b.

Reference: https://en.wikipedia.org/wiki/Cholesky_decomposition

Complexity:
    Time:  O(n^3)
    Space: O(n^2)
"""

from __future__ import annotations

import math


def cholesky_decomposition(matrix: list[list[float]]) -> list[list[float]] | None:
    """Compute the Cholesky decomposition of a positive-definite matrix.

    Args:
        matrix: Hermitian positive-definite matrix (n x n).

    Returns:
        Lower-triangular matrix V such that V * V^T = matrix,
        or None if the matrix cannot be decomposed.

    Examples:
        >>> cholesky_decomposition([[4, 12, -16], [12, 37, -43], [-16, -43, 98]])
        [[2.0, 0.0, 0.0], [6.0, 1.0, 0.0], [-8.0, 5.0, 3.0]]
    """
    size = len(matrix)
    for row in matrix:
        if len(row) != size:
            return None
    result = [[0.0] * size for _ in range(size)]
    for j in range(size):
        diagonal_sum = sum(result[j][k] ** 2 for k in range(j))
        diagonal_sum = matrix[j][j] - diagonal_sum
        if diagonal_sum <= 0:
            return None
        result[j][j] = math.sqrt(diagonal_sum)
        for i in range(j + 1, size):
            off_diagonal_sum = sum(result[i][k] * result[j][k] for k in range(j))
            result[i][j] = (matrix[i][j] - off_diagonal_sum) / result[j][j]
    return result
