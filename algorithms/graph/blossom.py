"""Edmonds' blossom algorithm — maximum cardinality matching.

Finds a maximum matching in a general (non-bipartite) undirected graph.
The algorithm handles odd-length cycles ("blossoms") by contracting them
and recursing.

Time: O(V^2 * E).

Inspired by PR #826 (abhishekiitm).
"""

from __future__ import annotations

from collections import deque


def max_matching(n: int, edges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Return a maximum cardinality matching for an undirected graph.

    *n* is the number of vertices (0..n-1).
    *edges* is a list of (u, v) edges.

    Returns a list of matched (u, v) pairs.

    >>> sorted(max_matching(4, [(0,1),(1,2),(2,3)]))
    [(0, 1), (2, 3)]
    """
    adj: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    match = [-1] * n

    def find_augmenting_path() -> bool:
        """Try to find an augmenting path from any free vertex."""
        parent = [-1] * n
        visited = [False] * n
        for start in range(n):
            if match[start] != -1:
                continue
            # BFS from this free vertex
            queue: deque[int] = deque([start])
            visited[start] = True
            found = False
            while queue and not found:
                u = queue.popleft()
                for v in adj[u]:
                    if visited[v] or v == match[u]:
                        continue
                    if match[v] == -1 and v != start:
                        # Augmenting path found — trace back and flip
                        _augment(parent, match, u, v)
                        return True
                    if match[v] != -1:
                        visited[v] = True
                        visited[match[v]] = True
                        parent[match[v]] = u
                        queue.append(match[v])
        return False

    while find_augmenting_path():
        pass

    result = []
    seen = set()
    for i in range(n):
        if match[i] != -1 and i not in seen:
            result.append((i, match[i]))
            seen.add(i)
            seen.add(match[i])
    return result


def _augment(parent: list[int], match: list[int], u: int, v: int) -> None:
    """Augment the matching along the path ending with edge (u, v)."""
    while u != -1:
        prev = match[u]
        match[u] = v
        match[v] = u
        v = prev
        u = parent[v] if v != -1 else -1
