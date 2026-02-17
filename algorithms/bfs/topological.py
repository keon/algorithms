"""
Topological Sort (Kahn's Algorithm / BFS)

Computes a topological ordering of a directed acyclic graph.  Raises
ValueError when a cycle is detected.

Reference: https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm

Complexity:
    Time:  O(V + E)
    Space: O(V + E)
"""

from __future__ import annotations

from collections import defaultdict, deque


def topological_sort(vertices: int, edges: list[tuple[int, int]]) -> list[int]:
    """Return a topological ordering of the vertices.

    Args:
        vertices: Number of vertices (labelled 0 .. vertices-1).
        edges: Directed edges as (u, v) meaning u -> v.

    Returns:
        List of vertices in topological order.

    Raises:
        ValueError: If the graph contains a cycle.

    Examples:
        >>> topological_sort(3, [(0, 1), (1, 2)])
        [0, 1, 2]
    """
    graph: dict[int, list[int]] = defaultdict(list)

    in_degree = [0] * vertices

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    queue: deque[int] = deque()
    for i in range(vertices):
        if in_degree[i] == 0:
            queue.append(i)

    sorted_order: list[int] = []
    processed = 0

    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        processed += 1

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if processed != vertices:
        raise ValueError("Cycle detected, topological sort failed")

    return sorted_order
