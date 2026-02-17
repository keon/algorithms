"""
Dijkstra's Shortest-Path Algorithm (Heap-Optimised)

Computes single-source shortest paths in a graph with non-negative edge
weights using a min-heap (priority queue) for efficient vertex selection.

This adjacency-list implementation is faster than the O(V²) matrix version
for sparse graphs.

Reference: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

Complexity:
    Time:  O((V + E) log V)  using a binary heap
    Space: O(V + E)
"""

from __future__ import annotations

import heapq


def dijkstra(
    graph: dict[str, dict[str, int | float]],
    source: str,
    target: str = "",
) -> tuple[int | float, list[str]]:
    """Return the shortest distance and path from *source* to *target*.

    Args:
        graph: Adjacency-list mapping each vertex to a dict of
               {neighbour: weight}.
        source: Starting vertex.
        target: Destination vertex.  When empty, compute shortest
                distances to all reachable vertices and return the path
                to the last vertex relaxed (mainly useful when a target
                is provided).

    Returns:
        A ``(distance, path)`` tuple where *distance* is the total
        shortest-path cost and *path* is the list of vertices from
        *source* to *target* inclusive.  If *target* is unreachable the
        distance is ``float('inf')`` and the path is empty.

    Examples:
        >>> g = {
        ...     "s": {"a": 2, "b": 1},
        ...     "a": {"s": 3, "b": 4, "c": 8},
        ...     "b": {"s": 4, "a": 2, "d": 2},
        ...     "c": {"a": 2, "d": 7, "t": 4},
        ...     "d": {"b": 1, "c": 11, "t": 5},
        ...     "t": {"c": 3, "d": 5},
        ... }
        >>> dijkstra(g, "s", "t")
        (8, ['s', 'b', 'd', 't'])
    """
    dist: dict[str, int | float] = {v: float("inf") for v in graph}
    dist[source] = 0
    prev: dict[str, str | None] = {v: None for v in graph}
    heap: list[tuple[int | float, str]] = [(0, source)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        if u == target:
            break
        for v, weight in graph[u].items():
            alt = dist[u] + weight
            if alt < dist.get(v, float("inf")):
                dist[v] = alt
                prev[v] = u
                heapq.heappush(heap, (alt, v))

    # Reconstruct path
    path: list[str] = []
    node: str | None = target if target else None
    if node and dist.get(node, float("inf")) < float("inf"):
        while node is not None:
            path.append(node)
            node = prev.get(node)
        path.reverse()

    return (dist.get(target, float("inf")), path) if target else (0, [])
