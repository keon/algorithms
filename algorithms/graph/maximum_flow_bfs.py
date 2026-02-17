"""
Maximum Flow via BFS

Computes maximum flow in a network represented as an adjacency matrix,
using BFS to find augmenting paths.

Reference: https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm

Complexity:
    Time:  O(V * E^2)
    Space: O(V^2)
"""

from __future__ import annotations

import copy
import math
import queue


def maximum_flow_bfs(adjacency_matrix: list[list[int]]) -> int:
    """Compute maximum flow using BFS augmenting paths.

    The source is the first vertex and the sink is the last vertex.

    Args:
        adjacency_matrix: n*n capacity matrix.

    Returns:
        The maximum flow value.

    Examples:
        >>> maximum_flow_bfs([[0, 10, 0], [0, 0, 10], [0, 0, 0]])
        10
    """
    new_array = copy.deepcopy(adjacency_matrix)
    total = 0

    while True:
        min_flow = math.inf
        visited = [0] * len(new_array)
        path = [0] * len(new_array)

        bfs: queue.Queue[int] = queue.Queue()

        visited[0] = 1
        bfs.put(0)

        while bfs.qsize() > 0:
            src = bfs.get()
            for k in range(len(new_array)):
                if new_array[src][k] > 0 and visited[k] == 0:
                    visited[k] = 1
                    bfs.put(k)
                    path[k] = src

        if visited[len(new_array) - 1] == 0:
            break

        tmp = len(new_array) - 1

        while tmp != 0:
            if min_flow > new_array[path[tmp]][tmp]:
                min_flow = new_array[path[tmp]][tmp]
            tmp = path[tmp]

        tmp = len(new_array) - 1

        while tmp != 0:
            new_array[path[tmp]][tmp] = new_array[path[tmp]][tmp] - min_flow
            tmp = path[tmp]

        total = total + min_flow

    return total
