"""
Given a directed graph, check whether it contains a cycle.

Real-life scenario: deadlock detection in a system. Processes may be
represented by vertices, then and an edge A -> B could mean that process A is
waiting for B to release its lock on a resource.
"""
from enum import Enum


class TraversalState(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2


example_graph_with_cycle = {'A': ['B', 'C'],
                            'B': ['D'],
                            'C': ['F'],
                            'D': ['E', 'F'],
                            'E': ['B'],
                            'F': []}

example_graph_without_cycle = {'A': ['B', 'C'],
                               'B': ['D', 'E'],
                               'C': ['F'],
                               'D': ['E'],
                               'E': [],
                               'F': []}
                               

def is_in_cycle(graph, traversal_states, vertex):
    if traversal_states[vertex] == TraversalState.GRAY:
        return True
    traversal_states[vertex] = TraversalState.GRAY
    for neighbor in graph[vertex]:
        if is_in_cycle(graph, traversal_states, neighbor):
            return True
    traversal_states[vertex] = TraversalState.BLACK
    return False


def contains_cycle(graph):
    traversal_states = {vertex: TraversalState.WHITE for vertex in graph}
    for vertex, state in traversal_states.items():
        if (state == TraversalState.WHITE and
           is_in_cycle(graph, traversal_states, vertex)):
            return True
    return False

print(contains_cycle(example_graph_with_cycle))
print(contains_cycle(example_graph_without_cycle))
