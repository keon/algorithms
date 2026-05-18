"""Chebyshev distance — L-infinity distance between two points.

Also known as chessboard distance, it is the maximum absolute difference
across coordinates. In chess, it is the minimum number of moves a king
needs to travel between two squares.
"""

from __future__ import annotations


def chebyshev_distance(a: tuple[float, ...], b: tuple[float, ...]) -> float:
    """Return the Chebyshev (L-infinity) distance between points *a* and *b*.

    Works in any number of dimensions.

    >>> chebyshev_distance((1, 2, 3), (4, 5, 6))
    3
    >>> chebyshev_distance((1, 2), (1, 2))
    0
    >>> chebyshev_distance((-1, -2), (4, 3))
    5
    """
    if len(a) != len(b):
        msg = "Points must have the same number of dimensions."
        raise ValueError(msg)
    return max(abs(x - y) for x, y in zip(a, b, strict=False))
