"""
Check if a Directed Graph is Strongly Connected

A directed graph is strongly connected if every vertex is reachable from
every other vertex.  This implementation uses two DFS passes (one on the
original graph and one on the reversed graph).

Reference: https://en.wikipedia.org/wiki/Strongly_connected_component

Complexity:
    Time:  O(V + E)
    Space: O(V + E)
"""

from __future__ import annotations

from collections import defaultdict


class Graph:
    """A directed graph for strong-connectivity testing."""

    def __init__(self, vertex_count: int) -> None:
        """Create a new graph with *vertex_count* vertices.

        Args:
            vertex_count: Number of vertices (labelled 0 .. vertex_count-1).
        """
        self.vertex_count = vertex_count
        self.graph: dict[int, list[int]] = defaultdict(list)

    def add_edge(self, source: int, target: int) -> None:
        """Add a directed edge from *source* to *target*.

        Args:
            source: Source vertex.
            target: Target vertex.
        """
        self.graph[source].append(target)

    def dfs(self) -> bool:
        """Return True if all vertices are reachable from vertex 0."""
        visited = [False] * self.vertex_count
        self._dfs_util(0, visited)
        return visited == [True] * self.vertex_count

    def _dfs_util(self, source: int, visited: list[bool]) -> None:
        """Recursive DFS helper.

        Args:
            source: Current vertex.
            visited: Visited flags (modified in place).
        """
        visited[source] = True
        for adjacent in self.graph[source]:
            if not visited[adjacent]:
                self._dfs_util(adjacent, visited)

    def reverse_graph(self) -> Graph:
        """Return a new graph with every edge reversed.

        Returns:
            A new Graph instance with reversed edges.
        """
        reverse = Graph(self.vertex_count)
        for source, adjacent in self.graph.items():
            for target in adjacent:
                reverse.add_edge(target, source)
        return reverse

    def is_strongly_connected(self) -> bool:
        """Return True if the graph is strongly connected.

        Returns:
            True when every vertex can reach every other vertex.
        """
        if self.dfs():
            reversed_graph = self.reverse_graph()
            if reversed_graph.dfs():
                return True
        return False
