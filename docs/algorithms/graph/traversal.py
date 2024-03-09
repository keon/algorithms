"""
Different ways to traverse a graph
"""

# dfs and bfs are the ultimately same except that they are visiting nodes in
# different order. To simulate this ordering we would use stack for dfs and
# queue for bfs.
#

def dfs_traverse(graph, start):
    """
    Traversal by depth first search.
    """
    visited, stack = set(), [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for next_node in graph[node]:
                if next_node not in visited:
                    stack.append(next_node)
    return visited

def bfs_traverse(graph, start):
    """
    Traversal by breadth first search.
    """
    visited, queue = set(), [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            for next_node in graph[node]:
                if next_node not in visited:
                    queue.append(next_node)
    return visited

def dfs_traverse_recursive(graph, start, visited=None):
    """
    Traversal by recursive depth first search.
    """
    if visited is None:
        visited = set()
    visited.add(start)
    for next_node in graph[start]:
        if next_node not in visited:
            dfs_traverse_recursive(graph, next_node, visited)
    return visited
