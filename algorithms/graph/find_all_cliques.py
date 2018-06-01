# takes dict of sets
# each key is a vertex
# value is set of all edges connected to vertex
# returns list of lists (each sub list is a maximal clique)
# implementation of the basic algorithm described in:
# Bron, Coen; Kerbosch, Joep (1973), "Algorithm 457: finding all cliques of an undirected graph",


def find_all_cliques(edges):
    def expand_clique(candidates, nays):
        nonlocal compsub
        if not candidates and not nays:
            nonlocal solutions
            solutions.append(compsub.copy())
        else:
            for selected in candidates.copy():
                candidates.remove(selected)
                candidates_temp = get_connected(selected, candidates)
                nays_temp = get_connected(selected, nays)
                compsub.append(selected)
                expand_clique(candidates_temp, nays_temp)
                nays.add(compsub.pop())

    def get_connected(vertex, old_set):
        new_set = set()
        for neighbor in edges[str(vertex)]:
            if neighbor in old_set:
                new_set.add(neighbor)
        return new_set

    compsub = []
    solutions = []
    possibles = set(edges.keys())
    expand_clique(possibles, set())
    return solutions
