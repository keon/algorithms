"""
Find Paths in a Graph

Provides functions to find a single path, all paths, or the shortest path
between two nodes using recursion and backtracking.

Complexity:
    Time:  O(V!) worst case (exponential backtracking)
    Space: O(V) per recursion stack
"""

from __future__ import annotations

from typing import Any


def find_path(
    graph: dict[Any, list[Any]],
    start: Any,
    end: Any,
    path: list[Any] | None = None,
) -> list[Any] | None:
    """Find a path between *start* and *end* using backtracking.

    Args:
        graph: Adjacency list.
        start: Source node.
        end: Target node.
        path: Accumulated path (internal use).

    Returns:
        A list representing the path, or None if no path exists.

    Examples:
        >>> find_path({'A': ['B'], 'B': ['C'], 'C': []}, 'A', 'C')
        ['A', 'B', 'C']
    """
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            return newpath
    return None


def find_all_path(
    graph: dict[Any, list[Any]],
    start: Any,
    end: Any,
    path: list[Any] | None = None,
) -> list[list[Any]]:
    """Find all paths between *start* and *end*.

    Args:
        graph: Adjacency list.
        start: Source node.
        end: Target node.
        path: Accumulated path (internal use).

    Returns:
        A list of all paths, where each path is a list of nodes.

    Examples:
        >>> find_all_path({'A': ['B', 'C'], 'B': ['C'], 'C': []}, 'A', 'C')
        [['A', 'B', 'C'], ['A', 'C']]
    """
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths: list[list[Any]] = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_path(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def find_shortest_path(
    graph: dict[Any, list[Any]],
    start: Any,
    end: Any,
    path: list[Any] | None = None,
) -> list[Any] | None:
    """Find the shortest path between *start* and *end*.

    Args:
        graph: Adjacency list.
        start: Source node.
        end: Target node.
        path: Accumulated path (internal use).

    Returns:
        The shortest path as a list of nodes, or None if unreachable.

    Examples:
        >>> find_shortest_path({'A': ['B', 'C'], 'B': ['C'], 'C': []}, 'A', 'C')
        ['A', 'C']
    """
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest: list[Any] | None = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath and (not shortest or len(newpath) < len(shortest)):
                    shortest = newpath
    return shortest
