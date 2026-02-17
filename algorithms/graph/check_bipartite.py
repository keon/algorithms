"""
Check Bipartite Graph

Determine whether an undirected graph is bipartite using BFS colouring.

Reference: https://en.wikipedia.org/wiki/Bipartite_graph

Complexity:
    Time:  O(V^2)  (adjacency-matrix representation)
    Space: O(V)
"""

from __future__ import annotations


def check_bipartite(adj_list: list[list[int]]) -> bool:
    """Return True if the graph represented by *adj_list* is bipartite.

    Args:
        adj_list: An n*n adjacency matrix where adj_list[i][j] is truthy if
            there is an edge between vertex *i* and vertex *j*.

    Returns:
        True if bipartite, False otherwise.

    Examples:
        >>> check_bipartite([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
        True
    """
    vertices = len(adj_list)

    set_type = [-1 for _ in range(vertices)]
    set_type[0] = 0

    queue = [0]

    while queue:
        current = queue.pop(0)

        if adj_list[current][current]:
            return False

        for adjacent in range(vertices):
            if adj_list[current][adjacent]:
                if set_type[adjacent] == set_type[current]:
                    return False

                if set_type[adjacent] == -1:
                    set_type[adjacent] = 1 - set_type[current]
                    queue.append(adjacent)

    return True
