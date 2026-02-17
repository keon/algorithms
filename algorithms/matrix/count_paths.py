"""
Count Paths

Count the number of unique paths from the top-left corner to the
bottom-right corner of an m x n grid. Movement is restricted to
right or down only. Uses dynamic programming.

Reference: https://leetcode.com/problems/unique-paths/

Complexity:
    Time:  O(m * n)
    Space: O(m * n)
"""

from __future__ import annotations


def count_paths(rows: int, cols: int) -> int:
    """Count unique paths from top-left to bottom-right of an m x n grid.

    Args:
        rows: Number of rows in the grid.
        cols: Number of columns in the grid.

    Returns:
        Number of unique paths, or -1 if dimensions are invalid.

    Examples:
        >>> count_paths(3, 3)
        6
    """
    if rows < 1 or cols < 1:
        return -1
    count = [[None for _ in range(cols)] for _ in range(rows)]

    for i in range(cols):
        count[0][i] = 1
    for j in range(rows):
        count[j][0] = 1

    for i in range(1, rows):
        for j in range(1, cols):
            count[i][j] = count[i - 1][j] + count[i][j - 1]

    return count[rows - 1][cols - 1]
