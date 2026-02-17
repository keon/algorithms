"""
Tarjan's Strongly Connected Components Algorithm

Finds all strongly connected components in a directed graph.

Reference: https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm

Complexity:
    Time:  O(V + E)
    Space: O(V)
"""

from __future__ import annotations

from algorithms.graph.graph import DirectedGraph


class Tarjan:
    """Find SCCs via Tarjan's algorithm."""

    def __init__(self, dict_graph: dict[str, list[str]]) -> None:
        """Build the graph and compute all SCCs.

        Args:
            dict_graph: Adjacency dict ``{vertex: [neighbours]}``.
        """
        self.graph = DirectedGraph(dict_graph)
        self.index = 0
        self.stack: list = []

        for vertex in self.graph.nodes:
            vertex.index = None

        self.sccs: list[list] = []
        for vertex in self.graph.nodes:
            if vertex.index is None:
                self._strongconnect(vertex, self.sccs)

    def _strongconnect(self, vertex: object, sccs: list[list]) -> None:
        """Process *vertex* and discover its SCC.

        Args:
            vertex: Current vertex node.
            sccs: Accumulated list of SCCs.
        """
        vertex.index = self.index
        vertex.lowlink = self.index
        self.index += 1
        self.stack.append(vertex)
        vertex.on_stack = True

        for adjacent in self.graph.adjacency_list[vertex]:
            if adjacent.index is None:
                self._strongconnect(adjacent, sccs)
                vertex.lowlink = min(vertex.lowlink, adjacent.lowlink)
            elif adjacent.on_stack:
                vertex.lowlink = min(vertex.lowlink, adjacent.index)

        if vertex.lowlink == vertex.index:
            scc: list = []
            while True:
                adjacent = self.stack.pop()
                adjacent.on_stack = False
                scc.append(adjacent)
                if adjacent == vertex:
                    break
            scc.sort()
            sccs.append(scc)
