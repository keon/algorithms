"""
A*-pathfinding.

Similar to Dijkstra's algorithm, but uses a heuristic to faster guide its
search toward the optimal solution.

See the TestAstarPathfinding class in tests/test_graph.py for example usage.

Resource: https://en.wikipedia.org/wiki/A*_search_algorithm
"""

import heapq
from collections import defaultdict
from math import inf

def find_path(graph, source, target):
    """
    Find the shortest path from source to target in the given graph.

    The graph must implement two operations:

        def adjacent(self, node)
            # Get a list of nodes immediately reachable from the given node.
            # Each element of the list should be a tuple (NODE, DISTANCE) where
            # NODE is the neighbouring node and DISTANCE the distance between
            # them.

        def distance_heuristic(self, source, target)
            # An approximation of the distance between two arbitrary nodes. In
            # order guarantee that an optimal solution to be returned, this
            # heuristic must be "admissable", ie. the returned value should
            # never exceed the shortest possible path. For example, in a planar
            # graph, the euclidean distance between nodes is an admissable
            # heuristic.

    The heuristic helps guide the search by preferring searching nodes which
    are closer to the target node.
    """

    # Queue of nodes with the estimated cost required to reach target
    queue = [(graph.distance_heuristic(source, target), source)]

    # For each node: the cost required to reach that node from the source
    reach_cost = defaultdict(lambda: inf)
    reach_cost[source] = 0

    # For each node: the node that came before it on the path
    came_from = {}

    while len(queue) > 0:
        _, current = heapq.heappop(queue)

        if current == target:
            # We reached the end, assuming the heurisic is admissible, this
            # will be the shortest path.
            return reconstruct_path(came_from, target)
        
        for next, distance in graph.adjacent(current):
            cost = reach_cost[current] + distance
            if cost < reach_cost[next]:
                # We found a better path! Record it and add it to the queue.
                reach_cost[next] = cost
                came_from[next] = current

                total_cost_estimate = cost + graph.distance_heuristic(next, target)
                heapq.heappush(queue, (total_cost_estimate, next))

    # There was no path from source to target
    return None

def reconstruct_path(came_from, target):
    """
    Reconstruct a path leading to target.

    Each node in the came_from dictionary should be associated with the node
    that came before it on the optimal path.
    """
    path = [target]

    node = target
    while node in came_from:
        node = came_from[node]
        path.append(node)

    path.reverse()
    return path

