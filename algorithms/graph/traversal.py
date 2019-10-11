graph = {'A': set(['B', 'C', 'F']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['A', 'C', 'E'])}

# dfs and bfs are the ultimately same except that they are visiting nodes in
# different order. To simulate this ordering we would use stack for dfs and
# queue for bfs.
#

def dfs_traverse(graph, start):
    visited, stack = set(), [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for nextNode in graph[node]:
                if nextNode not in visited:
                    stack.append(nextNode)
    return visited

# print(dfs_traverse(graph, 'A'))


def bfs_traverse(graph, start):
    visited, queue = set(), [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            for nextNode in graph[node]:
                if nextNode not in visited:
                    queue.append(nextNode)
    return visited

# print(bfs_traverse(graph, 'A'))

def dfs_traverse_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for nextNode in graph[start]:
        if nextNode not in visited:
            dfs_traverse_recursive(graph, nextNode, visited)
    return visited

# print(dfs_traverse_recursive(graph, 'A'))

# def find_path(graph, start, end, visited=[]):
    # # basecase
    # visitied = visited + [start]
    # if start == end:
        # return visited
    # if start not in graph:
        # return None
    # for node in graph[start]:
        # if node not in visited:
            # new_visited = find_path(graph, node, end, visited)
            # return new_visited
    # return None

# print(find_path(graph, 'A', 'F'))


