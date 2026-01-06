"""
A* (A-star) Search Algorithm

Finds the shortest path in a weighted graph using a heuristic function.

Wikipedia reference: https://en.wikipedia.org/wiki/A*_search_algorithm
"""

import heapq

def a_star(graph, start, goal, h):
    """
    Performs A* search on a graph.

    :param graph: dict mapping node -> list of (neighbor, cost) pairs
    :param start: starting node
    :param goal: goal node
    :param h: heuristic function h(node) -> estimated cost to goal
    :return: tuple (path, total_cost)
    """
    open_set = []
    heapq.heappush(open_set, (h(start), 0, start, [start]))  # (f_score, g_score, node, path)
    visited = set()

    while open_set:
        f_score, g_score, current, path = heapq.heappop(open_set)
        if current == goal:
            return path, g_score

        if current in visited:
            continue
        visited.add(current)

        for neighbor, cost in graph.get(current, []):
            if neighbor not in visited:
                g = g_score + cost
                f = g + h(neighbor)
                heapq.heappush(open_set, (f, g, neighbor, path + [neighbor]))

    return None, float("inf")


if __name__ == "__main__":
    # Example graph as adjacency list with weights
    graph = {
        "A": [("B", 1), ("C", 3)],
        "B": [("A", 1), ("D", 2)],
        "C": [("A", 3), ("D", 1)],
        "D": [("B", 2), ("C", 1), ("E", 5)],
        "E": [("D", 5)]
    }

    # Simple heuristic: straight-line distance (example)
    h = lambda node: {
        "A": 7,
        "B": 6,
        "C": 2,
        "D": 1,
        "E": 0
    }[node]

    path, cost = a_star(graph, "A", "E", h)
    print(f"Shortest path: {path}, Total cost: {cost}")
