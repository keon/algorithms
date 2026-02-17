"""
Spiral Traversal

Return all elements of an m x n matrix in spiral order, traversing
right, down, left, and up repeatedly while shrinking the boundaries.

Reference: https://leetcode.com/problems/spiral-matrix/

Complexity:
    Time:  O(m * n)
    Space: O(m * n)
"""

from __future__ import annotations


def spiral_traversal(matrix: list[list[int]]) -> list[int]:
    """Return matrix elements in spiral order.

    Args:
        matrix: 2D list of integers (m x n).

    Returns:
        List of elements in spiral order.

    Examples:
        >>> spiral_traversal([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [1, 2, 3, 6, 9, 8, 7, 4, 5]
    """
    result: list[int] = []
    if len(matrix) == 0:
        return result
    row_begin = 0
    row_end = len(matrix) - 1
    col_begin = 0
    col_end = len(matrix[0]) - 1

    while row_begin <= row_end and col_begin <= col_end:
        for i in range(col_begin, col_end + 1):
            result.append(matrix[row_begin][i])
        row_begin += 1

        for i in range(row_begin, row_end + 1):
            result.append(matrix[i][col_end])
        col_end -= 1

        if row_begin <= row_end:
            for i in range(col_end, col_begin - 1, -1):
                result.append(matrix[row_end][i])
        row_end -= 1

        if col_begin <= col_end:
            for i in range(row_end, row_begin - 1, -1):
                result.append(matrix[i][col_begin])
        col_begin += 1

    return result
