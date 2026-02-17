"""Manhattan distance — L1 distance between two points.

Also known as taxicab distance or city-block distance, it is the sum
of absolute differences of coordinates.

Inspired by PR #877 (ChinZhengSheng).
"""

from __future__ import annotations


def manhattan_distance(a: tuple[float, ...], b: tuple[float, ...]) -> float:
    """Return the Manhattan (L1) distance between points *a* and *b*.

    Works in any number of dimensions.

    >>> manhattan_distance((1, 2), (4, 6))
    7
    >>> manhattan_distance((0, 0, 0), (1, 2, 3))
    6
    """
    return sum(abs(x - y) for x, y in zip(a, b, strict=False))
