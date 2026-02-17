"""
Graph Data Structures

Reusable classes for representing nodes, directed edges and directed graphs.
These can be shared across graph algorithms.
"""

from __future__ import annotations


class Node:
    """A node (vertex) in a graph."""

    def __init__(self, name: str) -> None:
        self.name = name

    @staticmethod
    def get_name(obj: object) -> str:
        """Return the name of *obj* whether it is a Node or a string.

        Args:
            obj: A Node instance or a string.

        Returns:
            The string name.
        """
        if isinstance(obj, Node):
            return obj.name
        if isinstance(obj, str):
            return obj
        return ""

    def __eq__(self, obj: object) -> bool:
        return self.name == self.get_name(obj)

    def __repr__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __ne__(self, obj: object) -> bool:
        return self.name != self.get_name(obj)

    def __lt__(self, obj: object) -> bool:
        return self.name < self.get_name(obj)

    def __le__(self, obj: object) -> bool:
        return self.name <= self.get_name(obj)

    def __gt__(self, obj: object) -> bool:
        return self.name > self.get_name(obj)

    def __ge__(self, obj: object) -> bool:
        return self.name >= self.get_name(obj)

    def __bool__(self) -> bool:
        return bool(self.name)


class DirectedEdge:
    """A directed edge connecting two nodes."""

    def __init__(self, node_from: Node, node_to: Node) -> None:
        self.source = node_from
        self.target = node_to

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, DirectedEdge):
            return obj.source == self.source and obj.target == self.target
        return False

    def __repr__(self) -> str:
        return f"({self.source} -> {self.target})"


class DirectedGraph:
    """A directed graph storing nodes, edges and an adjacency list."""

    def __init__(self, load_dict: dict[str, list[str]] | None = None) -> None:
        """Build a directed graph, optionally from a dictionary.

        Args:
            load_dict: Optional adjacency dict ``{vertex: [neighbours]}``.
        """
        if load_dict is None:
            load_dict = {}
        self.nodes: list[Node] = []
        self.edges: list[DirectedEdge] = []
        self.adjacency_list: dict[Node, list[Node]] = {}

        if load_dict and isinstance(load_dict, dict):
            for vertex in load_dict:
                node_from = self.add_node(vertex)
                self.adjacency_list[node_from] = []
                for neighbor in load_dict[vertex]:
                    node_to = self.add_node(neighbor)
                    self.adjacency_list[node_from].append(node_to)
                    self.add_edge(vertex, neighbor)

    def add_node(self, node_name: str) -> Node:
        """Add a named node (or return it if it already exists).

        Args:
            node_name: Name of the node.

        Returns:
            The Node instance.
        """
        try:
            return self.nodes[self.nodes.index(node_name)]
        except ValueError:
            node = Node(node_name)
            self.nodes.append(node)
            return node

    def add_edge(self, node_name_from: str, node_name_to: str) -> None:
        """Add a directed edge between two named nodes.

        Args:
            node_name_from: Source node name.
            node_name_to: Target node name.
        """
        try:
            node_from = self.nodes[self.nodes.index(node_name_from)]
            node_to = self.nodes[self.nodes.index(node_name_to)]
            self.edges.append(DirectedEdge(node_from, node_to))
        except ValueError:
            pass
