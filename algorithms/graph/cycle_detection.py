"""
Cycle Detection in a Directed Graph

Uses DFS with three-colour marking to determine whether a directed graph
contains a cycle.

Reference: https://en.wikipedia.org/wiki/Cycle_(graph_theory)

Complexity:
    Time:  O(V + E)
    Space: O(V)
"""

from __future__ import annotations

from enum import Enum


class TraversalState(Enum):
    """Vertex states during DFS traversal."""

    WHITE = 0
    GRAY = 1
    BLACK = 2


def is_in_cycle(
    graph: dict[str, list[str]],
    traversal_states: dict[str, TraversalState],
    vertex: str,
) -> bool:
    """Return True if *vertex* is part of a cycle.

    Args:
        graph: Adjacency list of a directed graph.
        traversal_states: Current DFS colour for each vertex.
        vertex: Vertex to inspect.

    Returns:
        True if a cycle is detected through *vertex*.
    """
    if traversal_states[vertex] == TraversalState.GRAY:
        return True
    traversal_states[vertex] = TraversalState.GRAY
    for neighbor in graph[vertex]:
        if is_in_cycle(graph, traversal_states, neighbor):
            return True
    traversal_states[vertex] = TraversalState.BLACK
    return False


def contains_cycle(graph: dict[str, list[str]]) -> bool:
    """Return True if *graph* contains at least one cycle.

    Args:
        graph: Directed graph as ``{vertex: [neighbours], ...}``.

    Returns:
        True when a cycle exists.

    Examples:
        >>> contains_cycle({'A': ['B'], 'B': ['A']})
        True
        >>> contains_cycle({'A': ['B'], 'B': []})
        False
    """
    traversal_states = {vertex: TraversalState.WHITE for vertex in graph}
    for vertex, state in traversal_states.items():
        if state == TraversalState.WHITE and is_in_cycle(
            graph, traversal_states, vertex
        ):
            return True
    return False
