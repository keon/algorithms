"""
Find All Cliques (Bron-Kerbosch)

Finds every maximal clique in an undirected graph.

Reference: Bron, Coen; Kerbosch, Joep (1973), "Algorithm 457: finding all
    cliques of an undirected graph", Communications of the ACM.

Complexity:
    Time:  O(3^(V/3)) worst case
    Space: O(V)
"""

from __future__ import annotations


def find_all_cliques(edges: dict[str, set[str]]) -> list[list[str]]:
    """Return all maximal cliques in the graph.

    Args:
        edges: Adjacency sets keyed by vertex label.

    Returns:
        A list of cliques, where each clique is a list of vertex labels.

    Examples:
        >>> find_all_cliques({'0': {'1'}, '1': {'0'}})
        [['0', '1']]
    """
    compsub: list[str] = []
    solutions: list[list[str]] = []

    def _expand_clique(candidates: set[str], nays: set[str]) -> None:
        if not candidates and not nays:
            solutions.append(compsub.copy())
        else:
            for selected in candidates.copy():
                candidates.remove(selected)
                candidates_temp = _get_connected(selected, candidates)
                nays_temp = _get_connected(selected, nays)
                compsub.append(selected)
                _expand_clique(candidates_temp, nays_temp)
                nays.add(compsub.pop())

    def _get_connected(vertex: str, old_set: set[str]) -> set[str]:
        new_set: set[str] = set()
        for neighbor in edges[str(vertex)]:
            if neighbor in old_set:
                new_set.add(neighbor)
        return new_set

    possibles = set(edges.keys())
    _expand_clique(possibles, set())
    return solutions
