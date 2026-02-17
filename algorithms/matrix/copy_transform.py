"""
Copy Transform

Rotate and invert a matrix by creating transformed copies.
Provides clockwise rotation, counterclockwise rotation, top-left
inversion (transpose), and bottom-left inversion (anti-transpose).

Reference: https://en.wikipedia.org/wiki/Transpose

Complexity:
    Time:  O(m * n)
    Space: O(m * n)
"""

from __future__ import annotations


def rotate_clockwise(matrix: list[list[int]]) -> list[list[int]]:
    """Rotate a matrix 90 degrees clockwise via copy.

    Args:
        matrix: 2D list of integers.

    Returns:
        New matrix rotated 90 degrees clockwise.

    Examples:
        >>> rotate_clockwise([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    """
    result: list[list[int]] = []
    for row in reversed(matrix):
        for i, elem in enumerate(row):
            try:
                result[i].append(elem)
            except IndexError:
                result.insert(i, [])
                result[i].append(elem)
    return result


def rotate_counterclockwise(matrix: list[list[int]]) -> list[list[int]]:
    """Rotate a matrix 90 degrees counterclockwise via copy.

    Args:
        matrix: 2D list of integers.

    Returns:
        New matrix rotated 90 degrees counterclockwise.

    Examples:
        >>> rotate_counterclockwise([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
    """
    result: list[list[int]] = []
    for row in matrix:
        for i, elem in enumerate(reversed(row)):
            try:
                result[i].append(elem)
            except IndexError:
                result.insert(i, [])
                result[i].append(elem)
    return result


def top_left_invert(matrix: list[list[int]]) -> list[list[int]]:
    """Transpose a matrix (reflect over the main diagonal).

    Args:
        matrix: 2D list of integers.

    Returns:
        Transposed matrix.

    Examples:
        >>> top_left_invert([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    """
    result: list[list[int]] = []
    for row in matrix:
        for i, elem in enumerate(row):
            try:
                result[i].append(elem)
            except IndexError:
                result.insert(i, [])
                result[i].append(elem)
    return result


def bottom_left_invert(matrix: list[list[int]]) -> list[list[int]]:
    """Anti-transpose a matrix (reflect over the anti-diagonal).

    Args:
        matrix: 2D list of integers.

    Returns:
        Anti-transposed matrix.

    Examples:
        >>> bottom_left_invert([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        [[9, 6, 3], [8, 5, 2], [7, 4, 1]]
    """
    result: list[list[int]] = []
    for row in reversed(matrix):
        for i, elem in enumerate(reversed(row)):
            try:
                result[i].append(elem)
            except IndexError:
                result.insert(i, [])
                result[i].append(elem)
    return result
