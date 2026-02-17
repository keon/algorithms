"""
Strongly Connected Components (Kosaraju's Algorithm)

Counts the number of strongly connected components in a directed graph
using two DFS passes.

Reference: https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm

Complexity:
    Time:  O(V + E)
    Space: O(V + E)
"""

from __future__ import annotations


class Kosaraju:
    """Kosaraju's algorithm for counting SCCs."""

    def dfs(
        self,
        i: int,
        vertices: int,
        adj: list[list[int]],
        visited: list[int],
        stk: list[int],
    ) -> None:
        """DFS that records vertices in finish-time order.

        Args:
            i: Current vertex.
            vertices: Number of vertices.
            adj: Adjacency list.
            visited: Visited flags (-1 = unvisited).
            stk: Stack recording finish order.
        """
        visited[i] = 1

        for x in adj[i]:
            if visited[x] == -1:
                self.dfs(x, vertices, adj, visited, stk)

        stk.append(i)

    def kosaraju(self, vertices: int, adj: list[list[int]]) -> int:
        """Return the number of strongly connected components.

        Args:
            vertices: Number of vertices.
            adj: Adjacency list.

        Returns:
            Count of SCCs.

        Examples:
            >>> Kosaraju().kosaraju(3, [[1], [2], [0]])
            1
        """
        stk: list[int] = []
        visited = [-1] * (vertices + 1)

        for i in range(vertices):
            if visited[i] == -1:
                self.dfs(i, vertices, adj, visited, stk)

        stk.reverse()
        res = stk.copy()

        ans = 0
        visited1 = [-1] * (vertices + 1)

        adj1: list[list[int]] = [[] for _ in range(vertices)]

        for i in range(len(adj)):
            for x in adj[i]:
                adj1[x].append(i)

        for i in range(len(res)):
            if visited1[res[i]] == -1:
                ans += 1
                self.dfs(res[i], vertices, adj1, visited1, stk)

        return ans
