"""
Matrix Multiplication

Multiply two compatible matrices and return their product. The number of
columns in the multiplicand must equal the number of rows in the multiplier.

Reference: https://en.wikipedia.org/wiki/Matrix_multiplication

Complexity:
    Time:  O(m * n * p)  for (m x n) * (n x p)
    Space: O(m * p)
"""

from __future__ import annotations


def multiply(
    multiplicand: list[list[int]], multiplier: list[list[int]]
) -> list[list[int]]:
    """Multiply two matrices.

    Args:
        multiplicand: Matrix of size m x n.
        multiplier: Matrix of size n x p.

    Returns:
        Product matrix of size m x p.

    Raises:
        Exception: If the matrices are not compatible for multiplication.

    Examples:
        >>> multiply([[1, 2, 3], [2, 1, 1]], [[1], [2], [3]])
        [[14], [7]]
    """
    multiplicand_rows, multiplicand_cols = len(multiplicand), len(multiplicand[0])
    multiplier_rows, multiplier_cols = len(multiplier), len(multiplier[0])
    if multiplicand_cols != multiplier_rows:
        raise Exception(
            "Multiplicand matrix not compatible with Multiplier matrix."
        )
    result = [[0] * multiplier_cols for _ in range(multiplicand_rows)]
    for i in range(multiplicand_rows):
        for j in range(multiplier_cols):
            for k in range(len(multiplier)):
                result[i][j] += multiplicand[i][k] * multiplier[k][j]
    return result
