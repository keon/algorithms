"""
Kahn's Algorithm (Topological Sort via BFS)

Computes a topological ordering of a directed acyclic graph using an
in-degree based BFS approach.

Reference: https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm

Complexity:
    Time:  O(V + E)
    Space: O(V)
"""

from __future__ import annotations

from collections import deque


class Solution:
    """Wrapper class for Kahn's topological sort."""

    def topological_sort(
        self, vertices: int, adj: list[list[int]]
    ) -> list[int]:
        """Return a topological ordering of the graph.

        Args:
            vertices: Number of vertices.
            adj: Adjacency list where adj[i] lists neighbours of vertex *i*.

        Returns:
            A list of vertices in topological order, or an empty list if a
            cycle is detected.

        Examples:
            >>> Solution().topological_sort(3, [[1], [2], []])
            [0, 1, 2]
        """
        in_degree = [0] * vertices
        for i in range(vertices):
            for neighbor in adj[i]:
                in_degree[neighbor] += 1

        queue = deque(
            [i for i in range(vertices) if in_degree[i] == 0]
        )
        topo_order: list[int] = []

        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(topo_order) != vertices:
            return []

        return topo_order
