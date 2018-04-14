"""
Implements Tarjan's algorithm for finding strongly connected components
in a graph.
https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
"""
from graph import DirectedGraph

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

    