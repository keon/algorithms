"""
Given a directed graph, check whether it contains a cycle.

Real-life scenario: deadlock detection in a system. Processes may be
represented by vertices, then and an edge A -> B could mean that process A is
waiting for B to release its lock on a resource.
"""
from enum import Enum


class TraversalState(Enum):
    """
    For a given node:
        - WHITE: has not been visited yet
        - GRAY: is currently being investigated for a cycle
        - BLACK: is not part of a cycle
    """
    WHITE = 0
    GRAY = 1
    BLACK = 2

def is_in_cycle(graph, traversal_states, vertex):
    """
    Determines if the given vertex is in a cycle.

    :param: traversal_states: for each vertex, the state it is in
    """
    if traversal_states[vertex] == TraversalState.GRAY:
        return True
    traversal_states[vertex] = TraversalState.GRAY
    for neighbor in graph[vertex]:
        if is_in_cycle(graph, traversal_states, neighbor):
            return True
    traversal_states[vertex] = TraversalState.BLACK
    return False


def contains_cycle(graph):
    """
    Determines if there is a cycle in the given graph.
    The graph should be given as a dictionary:

        graph = {'A': ['B', 'C'],
                 'B': ['D'],
                 'C': ['F'],
                 'D': ['E', 'F'],
                 'E': ['B'],
                 'F': []}
    """
    traversal_states = {vertex: TraversalState.WHITE for vertex in graph}
    for vertex, state in traversal_states.items():
        if (state == TraversalState.WHITE and
           is_in_cycle(graph, traversal_states, vertex)):
            return True
    return False
