"""
Transitive Closure via DFS

Computes the transitive closure of a directed graph using depth-first
search.

Reference: https://en.wikipedia.org/wiki/Transitive_closure#In_graph_theory

Complexity:
    Time:  O(V * (V + E))
    Space: O(V^2)
"""

from __future__ import annotations


class Graph:
    """A directed graph for transitive closure computation."""

    def __init__(self, vertices: int) -> None:
        """Create a graph with *vertices* vertices.

        Args:
            vertices: Number of vertices.
        """
        self.vertex_count = vertices
        self.graph: dict[int, list[int]] = {}
        self.closure = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, source: int, target: int) -> None:
        """Add a directed edge.

        Args:
            source: Source vertex.
            target: Target vertex.
        """
        if source in self.graph:
            self.graph[source].append(target)
        else:
            self.graph[source] = [target]

    def _dfs_util(self, source: int, target: int) -> None:
        """Recursive DFS marking reachability from *source* through *target*.

        Args:
            source: Origin vertex.
            target: Current vertex being explored.
        """
        self.closure[source][target] = 1

        for adjacent in self.graph[target]:
            if self.closure[source][adjacent] == 0:
                self._dfs_util(source, adjacent)

    def transitive_closure(self) -> list[list[int]]:
        """Compute and return the transitive closure matrix.

        Returns:
            An n*n matrix where entry [i][j] is 1 if j is reachable from i.

        Examples:
            >>> g = Graph(2); g.add_edge(0, 1); g.transitive_closure()
            [[1, 1], [0, 1]]
        """
        for i in range(self.vertex_count):
            self._dfs_util(i, i)

        return self.closure
