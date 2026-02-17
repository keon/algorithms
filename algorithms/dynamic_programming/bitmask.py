"""Bitmask dynamic programming — Travelling Salesman Problem (TSP).

Uses DP with bitmask to find the minimum-cost Hamiltonian cycle in a
weighted graph. The state (visited_mask, current_city) encodes which
cities have been visited and where we are now.

Time: O(2^n * n^2).  Space: O(2^n * n).

Inspired by PR #855 (AmandaStromdahl).
"""

from __future__ import annotations

import math


def tsp(dist: list[list[float]]) -> float:
    """Return the minimum cost of a Hamiltonian cycle.

    *dist* is an n x n distance matrix.

    >>> tsp([[0, 10, 15, 20],
    ...      [10, 0, 35, 25],
    ...      [15, 35, 0, 30],
    ...      [20, 25, 30, 0]])
    80
    """
    n = len(dist)
    full_mask = (1 << n) - 1
    dp: dict[tuple[int, int], float] = {}

    def solve(mask: int, pos: int) -> float:
        if mask == full_mask:
            return dist[pos][0]
        key = (mask, pos)
        if key in dp:
            return dp[key]
        ans = math.inf
        for city in range(n):
            if not (mask & (1 << city)):
                ans = min(ans, dist[pos][city] + solve(mask | (1 << city), city))
        dp[key] = ans
        return ans

    return solve(1, 0)
