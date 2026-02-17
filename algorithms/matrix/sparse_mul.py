"""
Sparse Matrix Multiplication

Given two sparse matrices A and B, return their product A * B.
Skips zero elements for efficiency. A's column count must equal
B's row count.

Reference: https://leetcode.com/problems/sparse-matrix-multiplication/

Complexity:
    Time:  O(m * n * p) worst case, better with sparsity
    Space: O(m * p)
"""

from __future__ import annotations


def sparse_multiply(
    mat_a: list[list[int]], mat_b: list[list[int]]
) -> list[list[int]] | None:
    """Multiply two sparse matrices, skipping zero elements.

    Args:
        mat_a: First matrix of size m x n.
        mat_b: Second matrix of size n x p.

    Returns:
        Product matrix of size m x p, or None if either input is None.

    Raises:
        Exception: If the matrices have incompatible dimensions.

    Examples:
        >>> sparse_multiply([[1, 0, 0], [-1, 0, 3]], [[7, 0, 0], [0, 0, 0], [0, 0, 1]])
        [[7, 0, 0], [-7, 0, 3]]
    """
    if mat_a is None or mat_b is None:
        return None
    rows_a, cols_a = len(mat_a), len(mat_a[0])
    cols_b = len(mat_b[0])
    if len(mat_b) != cols_a:
        raise Exception("A's column number must be equal to B's row number.")
    result = [[0] * cols_b for _ in range(rows_a)]
    for i, row in enumerate(mat_a):
        for k, elem_a in enumerate(row):
            if elem_a:
                for j, elem_b in enumerate(mat_b[k]):
                    if elem_b:
                        result[i][j] += elem_a * elem_b
    return result
