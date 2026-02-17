"""
Minimum Spanning Tree (Kruskal's Algorithm)

Finds the MST of an undirected graph using Kruskal's algorithm with a
disjoint-set (union-find) data structure.

Reference: https://en.wikipedia.org/wiki/Kruskal%27s_algorithm

Complexity:
    Time:  O(E log E)
    Space: O(V)
"""

from __future__ import annotations


class Edge:
    """An edge of an undirected weighted graph."""

    def __init__(self, source: int, target: int, weight: int) -> None:
        self.source = source
        self.target = target
        self.weight = weight


class DisjointSet:
    """Union-Find data structure with path compression and union by size."""

    def __init__(self, size: int) -> None:
        """Create *size* singleton sets.

        Args:
            size: Number of elements.
        """
        self.parent = list(range(size))
        self.size = [1] * size

    def merge_set(self, node1: int, node2: int) -> None:
        """Merge the sets containing *node1* and *node2*.

        Args:
            node1: First element.
            node2: Second element.
        """
        node1 = self.find_set(node1)
        node2 = self.find_set(node2)

        if self.size[node1] < self.size[node2]:
            self.parent[node1] = node2
            self.size[node2] += self.size[node1]
        else:
            self.parent[node2] = node1
            self.size[node1] += self.size[node2]

    def find_set(self, node: int) -> int:
        """Return the root representative of the set containing *node*.

        Args:
            node: Element to look up.

        Returns:
            Root representative.
        """
        if self.parent[node] != node:
            self.parent[node] = self.find_set(self.parent[node])
        return self.parent[node]


def kruskal(vertex_count: int, edges: list[Edge], forest: DisjointSet) -> int:
    """Return the total weight of the MST computed by Kruskal's algorithm.

    Args:
        vertex_count: Number of vertices.
        edges: List of weighted edges.
        forest: Disjoint-set instance for the vertices.

    Returns:
        Sum of weights in the minimum spanning tree.

    Examples:
        >>> e = [Edge(0, 1, 1), Edge(1, 2, 2), Edge(0, 2, 3)]
        >>> kruskal(3, e, DisjointSet(3))
        3
    """
    edges.sort(key=lambda edge: edge.weight)

    mst: list[Edge] = []

    for edge in edges:
        set_u = forest.find_set(edge.source)
        set_v = forest.find_set(edge.target)
        if set_u != set_v:
            forest.merge_set(set_u, set_v)
            mst.append(edge)
            if len(mst) == vertex_count - 1:
                break

    return sum(edge.weight for edge in mst)
