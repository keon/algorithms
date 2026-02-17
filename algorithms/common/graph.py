"""Graph type shared across all graph algorithms.

This module provides the universal Graph used by every graph algorithm
in this library. Using a single shared type means you can compose
algorithms: build a graph, run BFS to check connectivity, then run
Dijkstra for shortest paths — all on the same object.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Graph:
    """A weighted directed graph using adjacency dict representation.

    Supports weighted/unweighted and directed/undirected graphs. The
    graph is stored as ``{node: {neighbor: weight}}``. For unweighted
    graphs, use the :meth:`unweighted` factory or set weights to 1.

    Attributes:
        adj: Adjacency dict mapping each node to ``{neighbor: weight}``.
        directed: Whether this is a directed graph.

    Examples:
        >>> g = Graph({"a": {"b": 1, "c": 4}, "b": {"c": 2}})
        >>> g.adj["a"]
        {'b': 1, 'c': 4}

        >>> g = Graph.unweighted({"a": ["b", "c"], "b": ["c"]})
        >>> g.adj["a"]
        {'b': 1, 'c': 1}
    """

    adj: dict[str, dict[str, float]] = field(default_factory=dict)
    directed: bool = True

    @classmethod
    def unweighted(
        cls, adj: dict[str, list[str]], directed: bool = True
    ) -> Graph:
        """Create a graph from an unweighted adjacency list.

        Args:
            adj: Mapping of node to list of neighbors.
            directed: Whether edges are one-directional.

        Returns:
            A Graph with all edge weights set to 1.

        Examples:
            >>> g = Graph.unweighted({"a": ["b", "c"], "b": ["c"]})
            >>> g.adj["b"]
            {'c': 1}
        """
        weighted = {
            node: {neighbor: 1 for neighbor in neighbors}
            for node, neighbors in adj.items()
        }
        return cls(adj=weighted, directed=directed)

    def nodes(self) -> set[str]:
        """Return all nodes in the graph.

        Returns:
            Set of all node identifiers, including nodes that only
            appear as neighbors.

        Examples:
            >>> g = Graph({"a": {"b": 1}})
            >>> sorted(g.nodes())
            ['a', 'b']
        """
        all_nodes: set[str] = set(self.adj.keys())
        for neighbors in self.adj.values():
            all_nodes.update(neighbors.keys())
        return all_nodes

    def add_edge(self, source: str, target: str, weight: float = 1) -> None:
        """Add an edge to the graph.

        For undirected graphs, the reverse edge is also added.

        Args:
            source: Source node.
            target: Target node.
            weight: Edge weight (default 1).

        Examples:
            >>> g = Graph()
            >>> g.add_edge("a", "b", 5)
            >>> g.adj["a"]["b"]
            5
        """
        if source not in self.adj:
            self.adj[source] = {}
        self.adj[source][target] = weight
        if not self.directed:
            if target not in self.adj:
                self.adj[target] = {}
            self.adj[target][source] = weight
