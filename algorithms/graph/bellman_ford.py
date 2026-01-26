"""
Bellman-Ford Algorithm for Single-Source Shortest Path

This algorithm finds the shortest paths from a source vertex to all other
vertices in a weighted directed graph. Unlike Dijkstra's algorithm, it can
handle graphs with negative edge weights.

Key Properties:
- Time Complexity: O(V * E) where V = vertices, E = edges
- Space Complexity: O(V)
- Can detect negative-weight cycles (returns False if one exists)
"""


def bellman_ford(graph, source):
    """
    Computes shortest paths from source to all reachable vertices.

    Args:
        graph: A dictionary representing the weighted directed graph.
               Format: {node: {neighbor: edge_weight, ...}, ...}
               Example:
               graph = {
                   'a': {'b': 6, 'e': 7},
                   'b': {'c': 5, 'd': -4, 'e': 8},
                   'c': {'b': -2},
                   'd': {'a': 2, 'c': 7},
                   'e': {'b': -3}
               }
        source: The starting vertex for shortest path computation.

    Returns:
        True if shortest paths were computed successfully (no negative cycle).
        False if a negative-weight cycle is reachable from the source,
        meaning no valid shortest paths exist.
    """
    # distance[node] = shortest known distance from source to node
    distance = {}
    # predecessor[node] = previous node in the shortest path to node
    predecessor = {}

    # Step 1: Initialize distances to infinity, source distance to 0
    initialize_single_source(graph, source, distance, predecessor)

    # Step 2: Relax all edges (V-1) times
    # After i iterations, we have the shortest paths using at most i edges.
    # Since the shortest path can have at most (V-1) edges, we need (V-1) iterations.
    num_vertices = len(graph)
    for _ in range(1, num_vertices):
        for current_node in graph:
            for neighbor in graph[current_node]:
                edge_weight = graph[current_node][neighbor]
                # Relaxation: If we found a shorter path to neighbor via current_node
                if distance[neighbor] > distance[current_node] + edge_weight:
                    distance[neighbor] = distance[current_node] + edge_weight
                    predecessor[neighbor] = current_node

    # Step 3: Check for negative-weight cycles
    # If we can still relax any edge after (V-1) iterations,
    # then there exists a negative-weight cycle.
    for current_node in graph:
        for neighbor in graph[current_node]:
            edge_weight = graph[current_node][neighbor]
            if distance[neighbor] > distance[current_node] + edge_weight:
                # Negative cycle detected - no valid shortest paths exist
                return False

    # No negative cycle found - shortest paths are valid
    return True


def initialize_single_source(graph, source, distance, predecessor):
    """
    Initialize the distance and predecessor data structures.

    Sets all distances to infinity (unreachable) except the source which is 0.
    Sets all predecessors to None (no path known yet).

    Args:
        graph: The weighted directed graph dictionary.
        source: The source vertex.
        distance: Dictionary to store shortest distances (modified in place).
        predecessor: Dictionary to store path predecessors (modified in place).
    """
    for node in graph:
        # Initially, all nodes are unreachable (infinite distance)
        distance[node] = float('inf')
        # No predecessor known yet
        predecessor[node] = None

    # Distance from source to itself is always 0
    distance[source] = 0
