"""
Crout Matrix Decomposition

Decompose a matrix A into lower-triangular matrix L and upper-triangular
matrix U such that L * U = A. L has non-zero elements only on and below
the diagonal; U has non-zero elements only on and above the diagonal
with ones on the diagonal.

Reference: https://en.wikipedia.org/wiki/Crout_matrix_decomposition

Complexity:
    Time:  O(n^3)
    Space: O(n^2)
"""

from __future__ import annotations


def crout_matrix_decomposition(
    matrix: list[list[float]],
) -> tuple[list[list[float]], list[list[float]]]:
    """Perform Crout decomposition of a square matrix.

    Args:
        matrix: Square matrix of size n x n.

    Returns:
        Tuple (L, U) of lower and upper triangular matrices.

    Examples:
        >>> crout_matrix_decomposition([[9, 9], [7, 7]])
        ([[9.0, 0.0], [7.0, 0.0]], [[1.0, 1.0], [0.0, 1.0]])
    """
    size = len(matrix)
    lower = [[0.0] * size for _ in range(size)]
    upper = [[0.0] * size for _ in range(size)]
    for j in range(size):
        upper[j][j] = 1.0
        for i in range(j, size):
            alpha = float(matrix[i][j])
            for k in range(j):
                alpha -= lower[i][k] * upper[k][j]
            lower[i][j] = float(alpha)
        for i in range(j + 1, size):
            temp = float(matrix[j][i])
            for k in range(j):
                temp -= float(lower[j][k] * upper[k][i])
            if int(lower[j][j]) == 0:
                lower[j][j] = float(0.1**40)
            upper[j][i] = float(temp / lower[j][j])
    return (lower, upper)
