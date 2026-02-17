from collections import deque, defaultdict

def topological_sort(vertices, edges):
    """
    Kahn’s Algorithm provides a clear and efficient way to perform topological ordering while also offering built-in cycle detection and avoiding recursion-depth issues.
    Uses collections, for O(1) implementation.

    Args:
        vertices (_type_): int
        edges (_type_): list[tuple[int, int]]

    Vertices are the number of vertices, from 0 to vertices-1
    Edges are directed edges (u, v), where u -> v

    Returns:
        list: Topological ordering of vertices

    Raises:
        ValueError: If a cycle is detected
    """

    # Adjacency list
    graph = defaultdict(list)

    # In-degree array
    in_degree = [0] * vertices

    # Build the graph and compute in-degrees
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # Queue of all vertices with in-degree 0
    queue = deque()
    for i in range(vertices):
        if in_degree[i] == 0:
            queue.append(i)

    sorted = []
    processed = 0

    # BFS
    while queue:
        node = queue.popleft()
        sorted.append(node)
        processed += 1

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Cycle detection
    if processed != vertices:
        raise ValueError("Cycle detected, topolical sort failed")

    return sorted