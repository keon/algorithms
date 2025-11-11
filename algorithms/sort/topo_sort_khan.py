from collections import defaultdict, deque

def topological_sort(num_vertices, edges):
    """
    Perform Topological Sorting using Kahn's Algorithm.

    Parameters:
    -----------
    num_vertices : int
        Number of vertices in the graph (vertices labeled 0 to num_vertices - 1)
    edges : list of tuple
        List of directed edges represented as (u, v) meaning u → v

    Returns:
    --------
    list
        A list representing the topological order of vertices.
        If the graph has a cycle, returns an empty list.
    """

    # Step 1: Build adjacency list and compute in-degree
    graph = defaultdict(list)
    in_degree = [0] * num_vertices

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # Step 2: Initialize queue with vertices having in-degree 0
    queue = deque([i for i in range(num_vertices) if in_degree[i] == 0])
    topo_order = []

    # Step 3: Process the queue
    while queue:
        u = queue.popleft()
        topo_order.append(u)

        # Decrease in-degree of neighbors
        for neighbor in graph[u]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: Check for cycle
    if len(topo_order) != num_vertices:
        print("Cycle detected: Topological sort not possible.")
        return []

    return topo_order


# Example Usage
if __name__ == "__main__":
    vertices = 6
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    order = topological_sort(vertices, edges)
    print("Topological Sort:", order)
