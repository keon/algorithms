"""
Count Connected Components in an Undirected Graph

Uses DFS to count the number of connected components.

Reference: https://en.wikipedia.org/wiki/Component_(graph_theory)

Complexity:
    Time:  O(V + E)
    Space: O(V)
"""

from __future__ import annotations


def count_components(adjacency_list: list[list[int]], size: int) -> int:
    """Return the number of connected components.

    Args:
        adjacency_list: Adjacency list where adjacency_list[i] contains
            the neighbours of vertex *i* (1-indexed vertices).
        size: Number of vertices.

    Returns:
        The count of connected components.

    Examples:
        >>> count_components([[], [2], [1]], 2)
        1
    """
    count = 0
    visited = [False] * (size + 1)
    for i in range(1, size + 1):
        if not visited[i]:
            _dfs(i, visited, adjacency_list)
            count += 1
    return count


def _dfs(
    source: int,
    visited: list[bool],
    adjacency_list: list[list[int]],
) -> None:
    """Mark all vertices reachable from *source* as visited.

    Args:
        source: Starting vertex.
        visited: Visited flags (modified in place).
        adjacency_list: Graph adjacency list.
    """
    visited[source] = True
    for child in adjacency_list[source]:
        if not visited[child]:
            _dfs(child, visited, adjacency_list)
