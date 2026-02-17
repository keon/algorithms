"""
Hosoya Triangle

The Hosoya triangle (originally Fibonacci triangle) is a triangular arrangement
of numbers where each entry is the sum of two entries above it.

Reference: https://en.wikipedia.org/wiki/Hosoya%27s_triangle

Complexity:
    Time:  O(n^3)  (naive recursive per entry)
    Space: O(n)    (call stack depth)
"""

from __future__ import annotations


def hosoya(height: int, width: int) -> int:
    """Compute a single entry in the Hosoya triangle.

    Args:
        height: Row index (0-based).
        width: Column index (0-based).

    Returns:
        The value at position (height, width) in the Hosoya triangle.

    Examples:
        >>> hosoya(4, 2)
        4
    """
    if (width == 0) and (height in (0, 1)):
        return 1
    if (width == 1) and (height in (1, 2)):
        return 1
    if height > width:
        return hosoya(height - 1, width) + hosoya(height - 2, width)
    if width == height:
        return hosoya(height - 1, width - 1) + hosoya(height - 2, width - 2)
    return 0


def hosoya_testing(height: int) -> list[int]:
    """Generate a flat list of all Hosoya triangle values up to given height.

    Args:
        height: Number of rows to generate.

    Returns:
        Flat list of triangle values row by row.

    Examples:
        >>> hosoya_testing(1)
        [1]
    """
    res = []
    for i in range(height):
        for j in range(i + 1):
            res.append(hosoya(i, j))
    return res
