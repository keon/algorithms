"""
A* (A-star) Search Algorithm

Finds the shortest path in a weighted graph using a heuristic function.

Reference: https://en.wikipedia.org/wiki/A*_search_algorithm

Complexity:
    Time:  O(E log V) with a binary heap
    Space: O(V)
"""

from __future__ import annotations

import heapq
from typing import Any, Callable


def a_star(
    graph: dict[Any, list[tuple[Any, float]]],
    start: Any,
    goal: Any,
    h: Callable[[Any], float],
) -> tuple[list[Any] | None, float]:
    """Find the shortest path using A* search.

    Args:
        graph: Adjacency list mapping node to list of (neighbor, cost) pairs.
        start: Starting node.
        goal: Goal node.
        h: Heuristic function estimating cost from a node to the goal.

    Returns:
        A tuple (path, total_cost). If no path exists, returns (None, inf).

    Examples:
        >>> g = {'A': [('B', 1)], 'B': [('C', 2)], 'C': []}
        >>> a_star(g, 'A', 'C', lambda n: 0)
        (['A', 'B', 'C'], 3)
    """
    open_set: list[tuple[float, float, Any, list[Any]]] = []
    heapq.heappush(open_set, (h(start), 0, start, [start]))
    visited: set[Any] = set()

    while open_set:
        f_score, g_score, current, path = heapq.heappop(open_set)
        if current == goal:
            return path, g_score

        if current in visited:
            continue
        visited.add(current)

        for neighbor, cost in graph.get(current, []):
            if neighbor not in visited:
                g = g_score + cost
                f = g + h(neighbor)
                heapq.heappush(open_set, (f, g, neighbor, path + [neighbor]))

    return None, float("inf")
