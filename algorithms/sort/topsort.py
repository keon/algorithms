"""
Given a list of system packages,
some packages cannot be installed until the other packages are installed.
Provide a valid sequence to install all of the packages.

e.g.
a relies on b
b relies on c

then a valid sequence is [c, b, a]
"""

depGraph = {

    "a": ["b"],
    "b": ["c"],
    "c": ['e'],
    'e': [],
    "d": [],
    "f": ["e", "d"]
}

given = ["b", "c", "a", "d", "e", "f"]


def ret_deps(visited, start):
    queue = []
    out = []
    queue.append(start)
    while queue:
        new_node = queue.pop(0)
        if new_node not in visited:
            visited.add(new_node)
        for child in depGraph[new_node]:
            queue.append(child)
            out.append(child)
    out.append(start)
    return out


def ret_dep_graph():
    visited = set()
    out = []
    # visited.add(given[0])
    for pac in given:
        if pac in visited:
            continue
        visited.add(pac)
        # out.append(pac)
        if pac in depGraph:
            # find all children
            for child in depGraph[pac]:
                if child in visited:
                    continue
                out.extend(ret_deps(visited, child))
        out.append(pac)
    print(out)


ret_dep_graph()
