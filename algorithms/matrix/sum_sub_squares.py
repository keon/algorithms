"""
Sum of Sub-Squares

Given a square matrix of size n x n and an integer k, compute the sum
of all k x k sub-squares and return the results as a matrix.

Reference: https://www.geeksforgeeks.org/given-n-x-n-square-matrix-find-sum-sub-squares-size-k-x-k/

Complexity:
    Time:  O(n^2 * k^2)
    Space: O((n - k + 1)^2)
"""

from __future__ import annotations


def sum_sub_squares(matrix: list[list[int]], k: int) -> list[list[int]] | None:
    """Compute sums of all k x k sub-squares in the matrix.

    Args:
        matrix: Square matrix of size n x n.
        k: Side length of the sub-squares.

    Returns:
        Matrix of sub-square sums, or None if k > n.

    Examples:
        >>> sum_sub_squares([[1, 1, 1], [2, 2, 2], [3, 3, 3]], 2)
        [[6, 6], [9, 9]]
    """
    size = len(matrix)
    if k > size:
        return None
    result_size = size - k + 1
    result = [[0] * result_size for _ in range(result_size)]
    for i in range(result_size):
        for j in range(result_size):
            total = 0
            for p in range(i, k + i):
                for q in range(j, k + j):
                    total += matrix[p][q]
            result[i][j] = total
    return result
