"""
Bellman-Ford Algorithm for Single-Source Shortest Path

Finds the shortest paths from a source vertex to all other vertices in a
weighted directed graph.  Unlike Dijkstra's algorithm it can handle graphs
with negative edge weights.

Reference: https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm

Complexity:
    Time:  O(V * E)
    Space: O(V)
"""

from __future__ import annotations


def bellman_ford(graph: dict[str, dict[str, float]], source: str) -> bool:
    """Compute shortest paths from *source* and detect negative cycles.

    Args:
        graph: Weighted directed graph as
            ``{node: {neighbor: edge_weight, ...}, ...}``.
        source: The starting vertex.

    Returns:
        True if shortest paths were computed (no negative cycle), False
        otherwise.

    Examples:
        >>> g = {'a': {'b': 1}, 'b': {'c': 2}, 'c': {}}
        >>> bellman_ford(g, 'a')
        True
    """
    distance: dict[str, float] = {}
    predecessor: dict[str, str | None] = {}

    _initialize_single_source(graph, source, distance, predecessor)

    num_vertices = len(graph)
    for _ in range(1, num_vertices):
        for current_node in graph:
            for neighbor in graph[current_node]:
                edge_weight = graph[current_node][neighbor]
                if distance[neighbor] > distance[current_node] + edge_weight:
                    distance[neighbor] = distance[current_node] + edge_weight
                    predecessor[neighbor] = current_node

    for current_node in graph:
        for neighbor in graph[current_node]:
            edge_weight = graph[current_node][neighbor]
            if distance[neighbor] > distance[current_node] + edge_weight:
                return False

    return True


def _initialize_single_source(
    graph: dict[str, dict[str, float]],
    source: str,
    distance: dict[str, float],
    predecessor: dict[str, str | None],
) -> None:
    """Set up initial distances and predecessors.

    Args:
        graph: The weighted directed graph dictionary.
        source: The source vertex.
        distance: Dictionary to store shortest distances (modified in place).
        predecessor: Dictionary to store path predecessors (modified in place).
    """
    for node in graph:
        distance[node] = float("inf")
        predecessor[node] = None
    distance[source] = 0
