"""
Graph Traversal Algorithms

Provides DFS and BFS traversal of a graph represented as an adjacency
dictionary.

Complexity:
    Time:  O(V + E)
    Space: O(V)
"""

from __future__ import annotations

from typing import Any


def dfs_traverse(graph: dict[Any, list[Any]], start: Any) -> set[Any]:
    """Traverse the graph from *start* using iterative DFS.

    Args:
        graph: Adjacency list.
        start: Starting node.

    Returns:
        Set of visited nodes.

    Examples:
        >>> sorted(dfs_traverse({'a': ['b'], 'b': []}, 'a'))
        ['a', 'b']
    """
    visited: set[Any] = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for next_node in graph[node]:
                if next_node not in visited:
                    stack.append(next_node)
    return visited


def bfs_traverse(graph: dict[Any, list[Any]], start: Any) -> set[Any]:
    """Traverse the graph from *start* using BFS.

    Args:
        graph: Adjacency list.
        start: Starting node.

    Returns:
        Set of visited nodes.

    Examples:
        >>> sorted(bfs_traverse({'a': ['b'], 'b': []}, 'a'))
        ['a', 'b']
    """
    visited: set[Any] = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            for next_node in graph[node]:
                if next_node not in visited:
                    queue.append(next_node)
    return visited


def dfs_traverse_recursive(
    graph: dict[Any, list[Any]],
    start: Any,
    visited: set[Any] | None = None,
) -> set[Any]:
    """Traverse the graph from *start* using recursive DFS.

    Args:
        graph: Adjacency list.
        start: Starting node.
        visited: Already-visited set (internal use).

    Returns:
        Set of visited nodes.

    Examples:
        >>> sorted(dfs_traverse_recursive({'a': ['b'], 'b': []}, 'a'))
        ['a', 'b']
    """
    if visited is None:
        visited = set()
    visited.add(start)
    for next_node in graph[start]:
        if next_node not in visited:
            dfs_traverse_recursive(graph, next_node, visited)
    return visited
