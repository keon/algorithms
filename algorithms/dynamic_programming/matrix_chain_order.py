"""
Matrix Chain Multiplication

Find the optimal parenthesization of a chain of matrices to minimize
the total number of scalar multiplications.

Reference: https://en.wikipedia.org/wiki/Matrix_chain_multiplication

Complexity:
    Time:  O(n^3)
    Space: O(n^2)
"""

from __future__ import annotations

_INF = float("inf")


def matrix_chain_order(array: list[int]) -> tuple[list[list[int]], list[list[int]]]:
    """Compute minimum multiplication cost and optimal split positions.

    Args:
        array: List of matrix dimensions where matrix i has dimensions
               array[i-1] x array[i].

    Returns:
        A tuple of (cost_matrix, split_matrix) where cost_matrix[i][j]
        holds the minimum cost and split_matrix[i][j] holds the optimal
        split point.

    Examples:
        >>> m, s = matrix_chain_order([30, 35, 15, 5, 10, 20, 25])
        >>> m[1][6]
        15125
    """
    n = len(array)
    matrix = [[0 for x in range(n)] for x in range(n)]
    sol = [[0 for x in range(n)] for x in range(n)]
    for chain_length in range(2, n):
        for a in range(1, n - chain_length + 1):
            b = a + chain_length - 1

            matrix[a][b] = _INF
            for c in range(a, b):
                cost = (
                    matrix[a][c]
                    + matrix[c + 1][b]
                    + array[a - 1] * array[c] * array[b]
                )
                if cost < matrix[a][b]:
                    matrix[a][b] = cost
                    sol[a][b] = c
    return matrix, sol
