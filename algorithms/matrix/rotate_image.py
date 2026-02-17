"""
Rotate Image

Rotate an n x n 2D matrix representing an image by 90 degrees clockwise,
in-place. First reverse the rows top-to-bottom, then transpose.

Reference: https://leetcode.com/problems/rotate-image/

Complexity:
    Time:  O(n^2)
    Space: O(1)
"""

from __future__ import annotations


def rotate(mat: list[list[int]]) -> list[list[int]]:
    """Rotate a square matrix 90 degrees clockwise in-place.

    Args:
        mat: Square matrix of size n x n.

    Returns:
        The same matrix, rotated 90 degrees clockwise.

    Examples:
        >>> rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    """
    if not mat:
        return mat
    mat.reverse()
    for i in range(len(mat)):
        for j in range(i):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    return mat
