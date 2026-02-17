"""
Search in Sorted Matrix

Search for a key in a matrix that is sorted row-wise and column-wise
in non-decreasing order. Start from the bottom-left corner and move
up or right depending on the comparison.

Reference: https://leetcode.com/problems/search-a-2d-matrix-ii/

Complexity:
    Time:  O(m + n)
    Space: O(1)
"""

from __future__ import annotations


def search_in_a_sorted_matrix(
    mat: list[list[int]], rows: int, cols: int, key: int
) -> bool:
    """Search for a key in a row-wise and column-wise sorted matrix.

    Args:
        mat: Sorted matrix of size m x n.
        rows: Number of rows.
        cols: Number of columns.
        key: Value to search for.

    Returns:
        True if the key is found, False otherwise.

    Examples:
        >>> search_in_a_sorted_matrix([[2, 5, 7], [4, 8, 13], [9, 11, 15]], 3, 3, 13)
        True
        >>> search_in_a_sorted_matrix([[2, 5, 7], [4, 8, 13], [9, 11, 15]], 3, 3, 6)
        False
    """
    i, j = rows - 1, 0
    while i >= 0 and j < cols:
        if key == mat[i][j]:
            return True
        if key < mat[i][j]:
            i -= 1
        else:
            j += 1
    return False
