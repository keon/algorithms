"""
Implements Tarjan's algorithm for finding strongly connected components
in a graph.
https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
"""

class Node(object):
    def __init__(self, name):
        self.name = name
    
    def __eq__(self, obj):
        if isinstance(obj, Node):
            return obj.name == self.name
        elif isinstance(obj, str):
            return obj == self.name
        return False

    def __repr__(self):
        return self.name
    
    def __hash__(self):
        return hash(self.name)

class DirectedEdge(object):
    def __init__(self, node_from, node_to):
        self.nf = node_from
        self.nt = node_to

    def __eq__(self, obj):
        if isinstance(obj, DirectedEdge):
            return obj.nf == self.nf and obj.nt == self.nt
        return False
    
    def __repr__(self):
        return '({0} -> {1})'.format(self.nf, self.nt)

class DirectedGraph(object):
    def __init__(self, load_dict={}):
        self.nodes = []
        self.edges = []
        self.adjmt = {}

        if load_dict and type(load_dict) == dict:
            for v in load_dict:
                node_from = self.add_node(v)
                self.adjmt[node_from] = []
                for w in load_dict[v]:
                    node_to = self.add_node(w)
                    self.adjmt[node_from].append(node_to)
                    self.add_edge(v, w)

    def add_node(self, node_name):
        try:
            return self.nodes[self.nodes.index(node_name)]
        except ValueError:
            node = Node(node_name)
            self.nodes.append(node)
            return node
    
    def add_edge(self, node_name_from, node_name_to):
        try:
            node_from = self.nodes[self.nodes.index(node_name_from)]
            node_to = self.nodes[self.nodes.index(node_name_to)]
            self.edges.append(DirectedEdge(node_from, node_to))
        except ValueError:
            pass
            



INDEX = 0
STACK = []

def strongconnect(graph, v, sccs):
    global INDEX, STACK
    # Set the depth index for v to the smallest unused index
    v.index = INDEX
    v.lowlink = INDEX
    INDEX += 1
    STACK.append(v)
    v.on_stack = True

    # Consider successors of v
    for w in graph.adjmt[v]:
        if w.index == None:
            # Successor w has not yet been visited; recurse on it
            strongconnect(graph, w, sccs)
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
            w = STACK.pop()
            w.on_stack = False
            scc.append(w)
            if w == v:
                break
        sccs.append(scc)


def tarjan(graph):
    # Set all node index to None
    for v in graph.nodes:
        v.index = None

    sccs = []
    for v in graph.nodes:
        if v.index == None:
            strongconnect(graph, v, sccs)
    
    return sccs


if __name__ == '__main__':
    # Graph from https://en.wikipedia.org/wiki/File:Scc.png
    example = {
        'A': ['B'],
        'B': ['C', 'E', 'F'],
        'C': ['D', 'G'],
        'D': ['C', 'H'],
        'E': ['A', 'F'],
        'F': ['G'],
        'G': ['F'],
        'H': ['D', 'G']
    }

    g = DirectedGraph(example)
    print(tarjan(g))

    # Graph from https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm#/media/File:Tarjan%27s_Algorithm_Animation.gif
    example = {
        'A': ['E'],
        'B': ['A'],
        'C': ['B', 'D'],
        'D': ['C'],
        'E': ['B'],
        'F': ['B', 'E', 'G'],
        'G': ['F', 'C'],
        'H': ['G', 'H', 'D']
    }

    g = DirectedGraph(example)
    print(tarjan(g))

    