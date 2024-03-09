"""
Given a formula in conjunctive normal form (2-CNF), finds a way to assign
True/False values to all variables to satisfy all clauses, or reports there
is no solution.

https://en.wikipedia.org/wiki/2-satisfiability


Format:
        - each clause is a pair of literals
        - each literal in the form (name, is_neg)
          where name is an arbitrary identifier,
          and is_neg is true if the literal is negated
"""

def dfs_transposed(vertex, graph, order, visited):
    """
    Perform a depth first search traversal of the graph starting at the given vertex.
    Stores the order in which nodes were visited to the list, in transposed order.
    """
    visited[vertex] = True

    for adjacent in graph[vertex]:
        if not visited[adjacent]:
            dfs_transposed(adjacent, graph, order, visited)

    order.append(vertex)


def dfs(vertex, current_comp, vertex_scc, graph, visited):
    """
    Perform a depth first search traversal of the graph starting at the given vertex.
    Records all visited nodes as being of a certain strongly connected component.
    """
    visited[vertex] = True
    vertex_scc[vertex] = current_comp

    for adjacent in graph[vertex]:
        if not visited[adjacent]:
            dfs(adjacent, current_comp, vertex_scc, graph, visited)


def add_edge(graph, vertex_from, vertex_to):
    """
    Add a directed edge to the graph.
    """
    if vertex_from not in graph:
        graph[vertex_from] = []

    graph[vertex_from].append(vertex_to)


def scc(graph):
    ''' Computes the strongly connected components of a graph '''
    order = []
    visited = {vertex: False for vertex in graph}

    graph_transposed = {vertex: [] for vertex in graph}

    for (source, neighbours) in graph.iteritems():
        for target in neighbours:
            add_edge(graph_transposed, target, source)

    for vertex in graph:
        if not visited[vertex]:
            dfs_transposed(vertex, graph_transposed, order, visited)

    visited = {vertex: False for vertex in graph}
    vertex_scc = {}

    current_comp = 0
    for vertex in reversed(order):
        if not visited[vertex]:
            # Each dfs will visit exactly one component
            dfs(vertex, current_comp, vertex_scc, graph, visited)
            current_comp += 1

    return vertex_scc


def build_graph(formula):
    ''' Builds the implication graph from the formula '''
    graph = {}

    for clause in formula:
        for (lit, _) in clause:
            for neg in [False, True]:
                graph[(lit, neg)] = []

    for ((a_lit, a_neg), (b_lit, b_neg)) in formula:
        add_edge(graph, (a_lit, a_neg), (b_lit, not b_neg))
        add_edge(graph, (b_lit, b_neg), (a_lit, not a_neg))

    return graph


def solve_sat(formula):
    """
    Solves the 2-SAT problem
    """
    graph = build_graph(formula)
    vertex_scc = scc(graph)

    for (var, _) in graph:
        if vertex_scc[(var, False)] == vertex_scc[(var, True)]:
            return None  # The formula is contradictory

    comp_repr = {}  # An arbitrary representant from each component

    for vertex in graph:
        if not vertex_scc[vertex] in comp_repr:
            comp_repr[vertex_scc[vertex]] = vertex

    comp_value = {}  # True/False value for each strongly connected component
    components = sorted(vertex_scc.values())

    for comp in components:
        if comp not in comp_value:
            comp_value[comp] = False

            (lit, neg) = comp_repr[comp]
            comp_value[vertex_scc[(lit, not neg)]] = True

    value = {var: comp_value[vertex_scc[(var, False)]] for (var, _) in graph}

    return value


def main():
    """
    Entry point for testing
    """
    formula = [(('x', False), ('y', False)),
               (('y', True), ('y', True)),
               (('a', False), ('b', False)),
               (('a', True), ('c', True)),
               (('c', False), ('b', True))]

    result = solve_sat(formula)

    for (variable, assign) in result.items():
        print(f"{variable}:{assign}")

if __name__ == '__main__':
    main()
