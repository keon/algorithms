"""
Topological Sort

Topological sort produces a linear ordering of vertices in a directed
acyclic graph (DAG) such that for every directed edge (u, v), vertex u
comes before v.  Two implementations are provided: one recursive
(DFS-based) and one iterative.

Reference: https://en.wikipedia.org/wiki/Topological_sorting

Complexity:
    Time:  O(V + E)
    Space: O(V)
"""

from __future__ import annotations

_GRAY, _BLACK = 0, 1


def top_sort_recursive(graph: dict[str, list[str]]) -> list[str]:
    """Return a topological ordering of *graph* using recursive DFS.

    Args:
        graph: Adjacency-list representation of a directed graph.

    Returns:
        A list of vertices in topological order.

    Raises:
        ValueError: If the graph contains a cycle.

    Examples:
        >>> top_sort_recursive({'a': ['b'], 'b': []})
        ['b', 'a']
    """
    order: list[str] = []
    enter = set(graph)
    state: dict[str, int] = {}

    def _dfs(node: str) -> None:
        state[node] = _GRAY
        for neighbour in graph.get(node, ()):
            neighbour_state = state.get(neighbour, None)
            if neighbour_state == _GRAY:
                raise ValueError("cycle")
            if neighbour_state == _BLACK:
                continue
            enter.discard(neighbour)
            _dfs(neighbour)
        order.append(node)
        state[node] = _BLACK

    while enter:
        _dfs(enter.pop())
    return order


def top_sort(graph: dict[str, list[str]]) -> list[str]:
    """Return a topological ordering of *graph* using an iterative approach.

    Args:
        graph: Adjacency-list representation of a directed graph.

    Returns:
        A list of vertices in topological order.

    Raises:
        ValueError: If the graph contains a cycle.

    Examples:
        >>> top_sort({'a': ['b'], 'b': []})
        ['b', 'a']
    """
    order: list[str] = []
    enter = set(graph)
    state: dict[str, int] = {}

    def _is_ready(node: str) -> bool:
        neighbours = graph.get(node, ())
        if len(neighbours) == 0:
            return True
        for neighbour in neighbours:
            neighbour_state = state.get(neighbour, None)
            if neighbour_state == _GRAY:
                raise ValueError("cycle")
            if neighbour_state != _BLACK:
                return False
        return True

    while enter:
        node = enter.pop()
        stack: list[str] = []
        while True:
            state[node] = _GRAY
            stack.append(node)
            for neighbour in graph.get(node, ()):
                neighbour_state = state.get(neighbour, None)
                if neighbour_state == _GRAY:
                    raise ValueError("cycle")
                if neighbour_state == _BLACK:
                    continue
                enter.discard(neighbour)
                stack.append(neighbour)
            while stack and _is_ready(stack[-1]):
                node = stack.pop()
                order.append(node)
                state[node] = _BLACK
            if len(stack) == 0:
                break
            node = stack.pop()

    return order
