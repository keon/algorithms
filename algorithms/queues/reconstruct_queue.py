"""
Reconstruct Queue by Height

Given a list of people described by (height, k) pairs where k is the
number of taller-or-equal people in front, reconstruct the queue by
sorting and inserting.

Reference: https://leetcode.com/problems/queue-reconstruction-by-height/

Complexity:
    Time:  O(n^2)
    Space: O(n)
"""

from __future__ import annotations


def reconstruct_queue(people: list[list[int]]) -> list[list[int]]:
    """Reconstruct the queue from (height, k) pairs.

    Args:
        people: List of [height, k] pairs.

    Returns:
        The reconstructed queue as a list of [height, k] pairs.

    Examples:
        >>> reconstruct_queue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
        [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
    """
    queue: list[list[int]] = []
    people.sort(key=lambda x: (-x[0], x[1]))
    for height, count in people:
        queue.insert(count, [height, count])
    return queue
