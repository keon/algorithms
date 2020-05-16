'''program to find the count of
nodes(including itself) in the subtree of a particular node.
Answer in the form of a list where each index contains the
number of nodes in the subtree of that index

for example:

INPUT : [[], [7, 6, 2], [1], [7, 8], [5], [7, 4], [1], [5, 1, 3], [3]]
a nested list(0-indexed) where each index contains the nodes which share
an edge with that index

OUTPUT  :  [8, 1, 2, 1, 2, 1, 5, 1]  '''




def subtree_counter(graph):
    treecount = [0] * (len(graph))
    OBSERVE = 0
    CHECK = 1
    stack = [(OBSERVE, 1, 0)]
    while len(stack):
        state, vertex, parent = stack.pop()
        if state == OBSERVE:
            stack.append((CHECK, vertex, parent))
            treecount[vertex]=1
            for child in graph[vertex]:
                if child != parent:
                    stack.append((OBSERVE, child, vertex))
        else:
            for child in graph[vertex]:
                if child != parent:
                    treecount[vertex]+=treecount[child]
    return(treecount[1:])
