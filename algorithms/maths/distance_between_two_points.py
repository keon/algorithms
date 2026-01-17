"""
Distance Between Two Points in 2D Space

Reference:
https://en.wikipedia.org/wiki/Distance#Euclidean_distance
"""

from math import sqrt


def distance_between_two_points(
    x1: float, y1: float, x2: float, y2: float
) -> float:
    """
    Calculate the Euclidean distance between two points in 2D space.

    Formula:
        d = sqrt((x2 - x1)^2 + (y2 - y1)^2)

    :param x1: x-coordinate of first point
    :param y1: y-coordinate of first point
    :param x2: x-coordinate of second point
    :param y2: y-coordinate of second point
    :return: Euclidean distance

    >>> distance_between_two_points(0, 0, 3, 4)
    5.0
    >>> distance_between_two_points(-1, -1, 2, 3)
    5.0
    """
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
