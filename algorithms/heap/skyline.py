"""
Skyline Problem

Given building triplets [left, right, height], compute the skyline
contour as a list of key points using a heap-based sweep line approach.

Reference: https://leetcode.com/problems/the-skyline-problem/

Complexity:
    Time:  O(n log n)
    Space: O(n)
"""

from __future__ import annotations

import heapq


def get_skyline(lrh: list[list[int]]) -> list[list[int]]:
    """Compute the skyline from a list of buildings.

    Args:
        lrh: List of [left, right, height] building triplets, sorted
            by left coordinate.

    Returns:
        List of [x, height] key points defining the skyline.

    Examples:
        >>> get_skyline([[2, 9, 10], [3, 7, 15]])
        [[2, 10], [3, 15], [7, 10], [9, 0]]
    """
    skyline: list[list[int]] = []
    live: list[list[int]] = []
    i, n = 0, len(lrh)
    while i < n or live:
        if not live or i < n and lrh[i][0] <= -live[0][1]:
            x = lrh[i][0]
            while i < n and lrh[i][0] == x:
                heapq.heappush(live, [-lrh[i][2], -lrh[i][1]])
                i += 1
        else:
            x = -live[0][1]
            while live and -live[0][1] <= x:
                heapq.heappop(live)
        height = len(live) and -live[0][0]
        if not skyline or height != skyline[-1][1]:
            skyline += [[x, height]]
    return skyline
