"""
Path Between Two Vertices in a Directed Graph

Determines whether there is a directed path from a source vertex to a
target vertex using DFS.

Complexity:
    Time:  O(V + E)
    Space: O(V)
"""

from __future__ import annotations

from collections import defaultdict


class Graph:
    """A directed graph for reachability queries."""

    def __init__(self, vertex_count: int) -> None:
        """Create a graph with *vertex_count* vertices.

        Args:
            vertex_count: Number of vertices.
        """
        self.vertex_count = vertex_count
        self.graph: dict[int, list[int]] = defaultdict(list)
        self.has_path = False

    def add_edge(self, source: int, target: int) -> None:
        """Add a directed edge.

        Args:
            source: Source vertex.
            target: Target vertex.
        """
        self.graph[source].append(target)

    def _dfs(self, source: int, target: int) -> None:
        """Run DFS to determine reachability.

        Args:
            source: Source vertex.
            target: Target vertex.
        """
        visited = [False] * self.vertex_count
        self._dfs_util(visited, source, target)

    def _dfs_util(self, visited: list[bool], source: int, target: int) -> None:
        """Recursive DFS helper.

        Args:
            visited: Visited flags.
            source: Current vertex.
            target: Destination vertex.
        """
        visited[source] = True
        for i in self.graph[source]:
            if target in self.graph[source]:
                self.has_path = True
                return
            if not visited[i]:
                self._dfs_util(visited, source, i)

    def is_reachable(self, source: int, target: int) -> bool:
        """Return True if *target* is reachable from *source*.

        Args:
            source: Source vertex.
            target: Target vertex.

        Returns:
            True if a directed path exists.

        Examples:
            >>> g = Graph(2); g.add_edge(0, 1); g.is_reachable(0, 1)
            True
        """
        self.has_path = False
        self._dfs(source, target)
        return self.has_path
