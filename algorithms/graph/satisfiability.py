"""
2-SAT Satisfiability

Given a formula in conjunctive normal form (2-CNF), finds an assignment of
True/False values that satisfies all clauses, or reports that no solution
exists.

Reference: https://en.wikipedia.org/wiki/2-satisfiability

Complexity:
    Time:  O(V + E)
    Space: O(V)
"""

from __future__ import annotations

from typing import Any


def _dfs_transposed(
    vertex: Any,
    graph: dict[Any, list[Any]],
    order: list[Any],
    visited: dict[Any, bool],
) -> None:
    """DFS on the transposed graph, recording finish order.

    Args:
        vertex: Current vertex.
        graph: Transposed graph adjacency list.
        order: Finish order (appended to).
        visited: Visited flags.
    """
    visited[vertex] = True
    for adjacent in graph[vertex]:
        if not visited[adjacent]:
            _dfs_transposed(adjacent, graph, order, visited)
    order.append(vertex)


def _dfs(
    vertex: Any,
    current_comp: int,
    vertex_scc: dict[Any, int],
    graph: dict[Any, list[Any]],
    visited: dict[Any, bool],
) -> None:
    """DFS assigning SCC labels.

    Args:
        vertex: Current vertex.
        current_comp: Current component label.
        vertex_scc: SCC mapping (modified in place).
        graph: Graph adjacency list.
        visited: Visited flags.
    """
    visited[vertex] = True
    vertex_scc[vertex] = current_comp
    for adjacent in graph[vertex]:
        if not visited[adjacent]:
            _dfs(adjacent, current_comp, vertex_scc, graph, visited)


def _add_edge(graph: dict[Any, list[Any]], vertex_from: Any, vertex_to: Any) -> None:
    """Add a directed edge.

    Args:
        graph: Adjacency list (modified in place).
        vertex_from: Source vertex.
        vertex_to: Target vertex.
    """
    if vertex_from not in graph:
        graph[vertex_from] = []
    graph[vertex_from].append(vertex_to)


def _scc(graph: dict[Any, list[Any]]) -> dict[Any, int]:
    """Compute SCCs using Kosaraju's algorithm.

    Args:
        graph: Directed graph adjacency list.

    Returns:
        Mapping from vertex to its SCC index.
    """
    order: list[Any] = []
    visited = {vertex: False for vertex in graph}

    graph_transposed: dict[Any, list[Any]] = {vertex: [] for vertex in graph}

    for source, neighbours in graph.items():
        for target in neighbours:
            _add_edge(graph_transposed, target, source)

    for vertex in graph:
        if not visited[vertex]:
            _dfs_transposed(vertex, graph_transposed, order, visited)

    visited = {vertex: False for vertex in graph}
    vertex_scc: dict[Any, int] = {}

    current_comp = 0
    for vertex in reversed(order):
        if not visited[vertex]:
            _dfs(vertex, current_comp, vertex_scc, graph, visited)
            current_comp += 1

    return vertex_scc


def _build_graph(
    formula: list[tuple[tuple[str, bool], tuple[str, bool]]],
) -> dict[tuple[str, bool], list[tuple[str, bool]]]:
    """Build the implication graph from a 2-CNF formula.

    Args:
        formula: List of clauses, each a pair of literals
            ``(name, is_negated)``.

    Returns:
        Implication graph as an adjacency list.
    """
    graph: dict[tuple[str, bool], list[tuple[str, bool]]] = {}

    for clause in formula:
        for lit, _ in clause:
            for neg in [False, True]:
                graph[(lit, neg)] = []

    for (a_lit, a_neg), (b_lit, b_neg) in formula:
        _add_edge(graph, (a_lit, a_neg), (b_lit, not b_neg))
        _add_edge(graph, (b_lit, b_neg), (a_lit, not a_neg))

    return graph


def solve_sat(
    formula: list[tuple[tuple[str, bool], tuple[str, bool]]],
) -> dict[str, bool] | None:
    """Solve a 2-SAT formula.

    Args:
        formula: List of clauses in 2-CNF.

    Returns:
        A satisfying assignment as ``{variable: value}`` or None if
        unsatisfiable.

    Examples:
        >>> solve_sat([(('x', False), ('y', False)), (('x', True), ('y', True))])
        {'x': False, 'y': False}
    """
    graph = _build_graph(formula)
    vertex_scc = _scc(graph)

    for var, _ in graph:
        if vertex_scc[(var, False)] == vertex_scc[(var, True)]:
            return None

    comp_repr: dict[int, tuple[str, bool]] = {}

    for vertex in graph:
        if vertex_scc[vertex] not in comp_repr:
            comp_repr[vertex_scc[vertex]] = vertex

    comp_value: dict[int, bool] = {}
    components = sorted(vertex_scc.values())

    for comp in components:
        if comp not in comp_value:
            comp_value[comp] = False
            lit, neg = comp_repr[comp]
            comp_value[vertex_scc[(lit, not neg)]] = True

    value = {var: comp_value[vertex_scc[(var, False)]] for var, _ in graph}

    return value
