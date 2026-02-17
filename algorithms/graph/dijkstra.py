"""
Dijkstra's Single-Source Shortest-Path Algorithm

Finds shortest distances from a source vertex to every other vertex in a
graph with non-negative edge weights.

Reference: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

Complexity:
    Time:  O(V^2)  (adjacency-matrix representation)
    Space: O(V)
"""

from __future__ import annotations


class Dijkstra:
    """A fully connected directed graph with edge weights."""

    def __init__(self, vertex_count: int) -> None:
        """Initialise graph with *vertex_count* vertices.

        Args:
            vertex_count: Number of vertices.
        """
        self.vertex_count = vertex_count
        self.graph: list[list[int]] = [
            [0 for _ in range(vertex_count)] for _ in range(vertex_count)
        ]

    def min_distance(self, dist: list[float], min_dist_set: list[bool]) -> int:
        """Return the unvisited vertex with the smallest distance.

        Args:
            dist: Current shortest distances.
            min_dist_set: Flags indicating already-processed vertices.

        Returns:
            Index of the closest unvisited vertex.
        """
        min_dist = float("inf")
        min_index = 0
        for target in range(self.vertex_count):
            if min_dist_set[target]:
                continue
            if dist[target] < min_dist:
                min_dist = dist[target]
                min_index = target
        return min_index

    def dijkstra(self, src: int) -> list[float]:
        """Compute shortest distances from *src* to all other vertices.

        Args:
            src: Source vertex index.

        Returns:
            List of shortest distances indexed by vertex.

        Examples:
            >>> g = Dijkstra(3)
            >>> g.graph = [[0, 1, 4], [1, 0, 2], [4, 2, 0]]
            >>> g.dijkstra(0)
            [0, 1, 3]
        """
        dist: list[float] = [float("inf")] * self.vertex_count
        dist[src] = 0
        min_dist_set = [False] * self.vertex_count

        for _ in range(self.vertex_count):
            source = self.min_distance(dist, min_dist_set)
            min_dist_set[source] = True

            for target in range(self.vertex_count):
                if self.graph[source][target] <= 0 or min_dist_set[target]:
                    continue
                if dist[target] > dist[source] + self.graph[source][target]:
                    dist[target] = dist[source] + self.graph[source][target]

        return dist
