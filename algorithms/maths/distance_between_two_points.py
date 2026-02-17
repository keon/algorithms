"""
Distance Between Two Points in 2D Space

Calculate the Euclidean distance between two points using the distance
formula derived from the Pythagorean theorem.

Reference: https://en.wikipedia.org/wiki/Euclidean_distance

Complexity:
    Time:  O(1)
    Space: O(1)
"""

from __future__ import annotations

from math import sqrt


def distance_between_two_points(
    x1: float, y1: float, x2: float, y2: float
) -> float:
    """Calculate the Euclidean distance between two points in 2D space.

    Args:
        x1: x-coordinate of the first point.
        y1: y-coordinate of the first point.
        x2: x-coordinate of the second point.
        y2: y-coordinate of the second point.

    Returns:
        The Euclidean distance between the two points.

    Examples:
        >>> distance_between_two_points(0, 0, 3, 4)
        5.0
        >>> distance_between_two_points(-1, -1, 2, 3)
        5.0
    """
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
