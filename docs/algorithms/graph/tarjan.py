"""
Implements Tarjan's algorithm for finding strongly connected components
in a graph.
https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
"""
from algorithms.graph.graph import DirectedGraph


# pylint: disable=too-few-public-methods
class Tarjan:
    """
    A directed graph used for finding strongly connected components
    """
    def __init__(self, dict_graph):
        self.graph = DirectedGraph(dict_graph)
        self.index = 0
        self.stack = []

        # Runs Tarjan
        # Set all node index to None
        for vertex in self.graph.nodes:
            vertex.index = None

        self.sccs = []
        for vertex in self.graph.nodes:
            if vertex.index is None:
                self.strongconnect(vertex, self.sccs)

    def strongconnect(self, vertex, sccs):
        """
        Given a vertex, adds all successors of the given vertex to the same connected component
        """
        # Set the depth index for v to the smallest unused index
        vertex.index = self.index
        vertex.lowlink = self.index
        self.index += 1
        self.stack.append(vertex)
        vertex.on_stack = True

        # Consider successors of v
        for adjacent in self.graph.adjacency_list[vertex]:
            if adjacent.index is None:
                # Successor w has not yet been visited; recurse on it
                self.strongconnect(adjacent, sccs)
                vertex.lowlink = min(vertex.lowlink, adjacent.lowlink)
            elif adjacent.on_stack:
                # Successor w is in stack S and hence in the current SCC
                # If w is not on stack, then (v, w) is a cross-edge in the DFS
                # tree and must be ignored
                # Note: The next line may look odd - but is correct.
                # It says w.index not w.lowlink; that is deliberate and from the original paper
                vertex.lowlink = min(vertex.lowlink, adjacent.index)

        # If v is a root node, pop the stack and generate an SCC
        if vertex.lowlink == vertex.index:
            # start a new strongly connected component
            scc = []
            while True:
                adjacent = self.stack.pop()
                adjacent.on_stack = False
                scc.append(adjacent)
                if adjacent == vertex:
                    break
            scc.sort()
            sccs.append(scc)
