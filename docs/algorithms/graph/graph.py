"""
These are classes to represent a Graph and its elements.
It can be shared across graph algorithms.
"""

class Node:
    """
    A node/vertex in a graph.
    """

    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_name(obj):
        """
        Return the name of the node
        """
        if isinstance(obj, Node):
            return obj.name
        if isinstance(obj, str):
            return obj
        return''

    def __eq__(self, obj):
        return self.name == self.get_name(obj)

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __ne__(self, obj):
        return self.name != self.get_name(obj)

    def __lt__(self, obj):
        return self.name < self.get_name(obj)

    def __le__(self, obj):
        return self.name <= self.get_name(obj)

    def __gt__(self, obj):
        return self.name > self.get_name(obj)

    def __ge__(self, obj):
        return self.name >= self.get_name(obj)

    def __bool__(self):
        return self.name

class DirectedEdge:
    """
    A directed edge in a directed graph.
    Stores the source and target node of the edge.
    """

    def __init__(self, node_from, node_to):
        self.source = node_from
        self.target = node_to

    def __eq__(self, obj):
        if isinstance(obj, DirectedEdge):
            return obj.source == self.source and obj.target == self.target
        return False

    def __repr__(self):
        return f"({self.source} -> {self.target})"

class DirectedGraph:
    """
    A directed graph.
    Stores a set of nodes, edges and adjacency matrix.
    """

    # pylint: disable=dangerous-default-value
    def __init__(self, load_dict={}):
        self.nodes = []
        self.edges = []
        self.adjacency_list = {}

        if load_dict and isinstance(load_dict, dict):
            for vertex in load_dict:
                node_from = self.add_node(vertex)
                self.adjacency_list[node_from] = []
                for neighbor in load_dict[vertex]:
                    node_to = self.add_node(neighbor)
                    self.adjacency_list[node_from].append(node_to)
                    self.add_edge(vertex, neighbor)

    def add_node(self, node_name):
        """
        Add a new named node to the graph.
        """
        try:
            return self.nodes[self.nodes.index(node_name)]
        except ValueError:
            node = Node(node_name)
            self.nodes.append(node)
            return node

    def add_edge(self, node_name_from, node_name_to):
        """
        Add a new edge to the graph between two nodes.
        """
        try:
            node_from = self.nodes[self.nodes.index(node_name_from)]
            node_to = self.nodes[self.nodes.index(node_name_to)]
            self.edges.append(DirectedEdge(node_from, node_to))
        except ValueError:
            pass
