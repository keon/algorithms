"""
Minimum Cost Path

Find the minimum cost to travel from station 0 to station N-1 given
a cost matrix where cost[i][j] is the price of going from station i
to station j (for i < j).

Reference: https://en.wikipedia.org/wiki/Shortest_path_problem

Complexity:
    Time:  O(n^2)
    Space: O(n)
"""

from __future__ import annotations

_INF = float("inf")


def min_cost(cost: list[list[int]]) -> int:
    """Compute the minimum cost to reach the last station from station 0.

    Args:
        cost: Square matrix where cost[i][j] is the travel cost from
              station i to station j (for i < j).

    Returns:
        Minimum cost to reach station N-1 from station 0.

    Examples:
        >>> min_cost([[0, 15, 80, 90], [-1, 0, 40, 50], [-1, -1, 0, 70], [-1, -1, -1, 0]])
        65
    """
    length = len(cost)
    dist = [_INF] * length

    dist[0] = 0

    for i in range(length):
        for j in range(i + 1, length):
            dist[j] = min(dist[j], dist[i] + cost[i][j])

    return dist[length - 1]
