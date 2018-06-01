'''
Given a formula in conjunctive normal form (2-CNF), finds a way to assign
True/False values to all variables to satisfy all clauses, or reports there
is no solution.

https://en.wikipedia.org/wiki/2-satisfiability
'''


''' Format:
        - each clause is a pair of literals
        - each literal in the form (name, is_neg)
          where name is an arbitrary identifier,
          and is_neg is true if the literal is negated
'''
formula = [(('x', False), ('y', False)),
           (('y', True), ('y', True)),
           (('a', False), ('b', False)),
           (('a', True), ('c', True)),
           (('c', False), ('b', True))]


def dfs_transposed(v, graph, order, vis):
    vis[v] = True

    for u in graph[v]:
        if not vis[u]:
            dfs_transposed(u, graph, order, vis)

    order.append(v)


def dfs(v, current_comp, vertex_scc, graph, vis):
    vis[v] = True
    vertex_scc[v] = current_comp

    for u in graph[v]:
        if not vis[u]:
            dfs(u, current_comp, vertex_scc, graph, vis)


def add_edge(graph, vertex_from, vertex_to):
    if vertex_from not in graph:
        graph[vertex_from] = []

    graph[vertex_from].append(vertex_to)


def scc(graph):
    ''' Computes the strongly connected components of a graph '''
    order = []
    vis = {vertex: False for vertex in graph}

    graph_transposed = {vertex: [] for vertex in graph}

    for (v, neighbours) in graph.iteritems():
        for u in neighbours:
            add_edge(graph_transposed, u, v)

    for v in graph:
        if not vis[v]:
            dfs_transposed(v, graph_transposed, order, vis)

    vis = {vertex: False for vertex in graph}
    vertex_scc = {}

    current_comp = 0
    for v in reversed(order):
        if not vis[v]:
            # Each dfs will visit exactly one component
            dfs(v, current_comp, vertex_scc, graph, vis)
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


if __name__ == '__main__':
    result = solve_sat(formula)

    for (variable, assign) in result.iteritems():
        print("{}:{}".format(variable, assign))
