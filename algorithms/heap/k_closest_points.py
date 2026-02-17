"""
K Closest Points to Origin

Given a list of points, find the k closest to the origin using a max
heap of size k. For each subsequent point, replace the heap root if
the new point is closer.

Reference: https://leetcode.com/problems/k-closest-points-to-origin/

Complexity:
    Time:  O(k + (n - k) log k)
    Space: O(k)
"""

from __future__ import annotations

from heapq import heapify, heappushpop


def k_closest(
    points: list[tuple[int, int]],
    k: int,
    origin: tuple[int, int] = (0, 0),
) -> list[tuple[int, int]]:
    """Find the k closest points to the origin.

    Args:
        points: List of (x, y) coordinate tuples.
        k: Number of closest points to return.
        origin: The reference point, defaults to (0, 0).

    Returns:
        List of the k closest points.

    Examples:
        >>> k_closest([(1, 0), (-1, 0), (2, 3)], 2)
        [(-1, 0), (1, 0)]
    """
    heap = [(-_distance(p, origin), p) for p in points[:k]]
    heapify(heap)

    for point in points[k:]:
        dist = _distance(point, origin)
        heappushpop(heap, (-dist, point))

    return [point for _, point in heap]


def _distance(point: tuple[int, int], origin: tuple[int, int] = (0, 0)) -> int:
    """Compute squared Euclidean distance from point to origin.

    Args:
        point: The (x, y) coordinate.
        origin: The reference point.

    Returns:
        Squared Euclidean distance.
    """
    return (point[0] - origin[0]) ** 2 + (point[1] - origin[1]) ** 2
