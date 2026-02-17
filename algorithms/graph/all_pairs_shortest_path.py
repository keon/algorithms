"""
All-Pairs Shortest Path (Floyd-Warshall)

Given an n*n adjacency matrix, computes the shortest path between every pair
of vertices using the Floyd-Warshall algorithm.

Reference: https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm

Complexity:
    Time:  O(V^3)
    Space: O(V^2)
"""

from __future__ import annotations

import copy


def all_pairs_shortest_path(
    adjacency_matrix: list[list[float]],
) -> list[list[float]]:
    """Compute shortest distances between all pairs of vertices.

    Args:
        adjacency_matrix: An n*n matrix where entry [i][j] is the edge weight
            from vertex i to vertex j.

    Returns:
        A new n*n matrix containing the shortest distance between each pair.

    Examples:
        >>> all_pairs_shortest_path(
        ...     [[0, 1, float('inf')], [float('inf'), 0, 1],
        ...      [1, float('inf'), 0]])
        [[0, 1, 2], [2, 0, 1], [1, 2, 0]]
    """
    new_array = copy.deepcopy(adjacency_matrix)

    size = len(new_array)
    for k in range(size):
        for i in range(size):
            for j in range(size):
                if new_array[i][j] > new_array[i][k] + new_array[k][j]:
                    new_array[i][j] = new_array[i][k] + new_array[k][j]

    return new_array
