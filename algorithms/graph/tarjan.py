"""
Implements Tarjan's algorithm for finding strongly connected components
in a graph.
https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
"""
from algorithms.graph.graph import DirectedGraph


class Tarjan(object):
    def __init__(self, dict_graph):
        self.graph = DirectedGraph(dict_graph)
        self.index = 0
        self.stack = []

        # Runs Tarjan
        # Set all node index to None
        for v in self.graph.nodes:
            v.index = None

        self.sccs = []
        for v in self.graph.nodes:
            if v.index is None:
                self.strongconnect(v, self.sccs)

    def strongconnect(self, v, sccs):
        # Set the depth index for v to the smallest unused index
        v.index = self.index
        v.lowlink = self.index
        self.index += 1
        self.stack.append(v)
        v.on_stack = True

        # Consider successors of v
        for w in self.graph.adjmt[v]:
            if w.index is None:
                # Successor w has not yet been visited; recurse on it
                self.strongconnect(w, sccs)
                v.lowlink = min(v.lowlink, w.lowlink)
            elif w.on_stack:
                # Successor w is in stack S and hence in the current SCC
                # If w is not on stack, then (v, w) is a cross-edge in the DFS tree and must be ignored
                # Note: The next line may look odd - but is correct.
                # It says w.index not w.lowlink; that is deliberate and from the original paper
                v.lowlink = min(v.lowlink, w.index)

        # If v is a root node, pop the stack and generate an SCC
        if v.lowlink == v.index:
            # start a new strongly connected component
            scc = []
            while True:
                w = self.stack.pop()
                w.on_stack = False
                scc.append(w)
                if w == v:
                    break
            scc.sort()
            sccs.append(scc)
