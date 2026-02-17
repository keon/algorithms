"""
Prim's Minimum Spanning Tree

Computes the weight of a minimum spanning tree for a connected weighted
undirected graph using a priority queue.

Reference: https://en.wikipedia.org/wiki/Prim%27s_algorithm

Complexity:
    Time:  O(E log V)
    Space: O(V + E)
"""

from __future__ import annotations

import heapq
from typing import Any


def prims_minimum_spanning(
    graph_used: dict[Any, list[list[int | Any]]],
) -> int:
    """Return the total weight of the MST using Prim's algorithm.

    Args:
        graph_used: Adjacency list as ``{node: [[weight, neighbour], ...]}``.

    Returns:
        Sum of edge weights in the minimum spanning tree.

    Examples:
        >>> prims_minimum_spanning({1: [[1, 2]], 2: [[1, 1]]})
        1
    """
    vis: list[Any] = []
    heap: list[list[int | Any]] = [[0, 1]]
    prim: set[Any] = set()
    mincost = 0

    while len(heap) > 0:
        cost, node = heapq.heappop(heap)
        if node in vis:
            continue

        mincost += cost
        prim.add(node)
        vis.append(node)

        for distance, adjacent in graph_used[node]:
            if adjacent not in vis:
                heapq.heappush(heap, [distance, adjacent])

    return mincost
