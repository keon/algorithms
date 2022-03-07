"""
Determine if there is a path between nodes in a graph
"""

from collections import defaultdict


class Graph:
    """
    A directed graph
    """

    def __init__(self,vertex_count):
        self.vertex_count = vertex_count
        self.graph = defaultdict(list)
        self.has_path = False

    def add_edge(self,source,target):
        """
        Add a new directed edge to the graph
        """
        self.graph[source].append(target)

    def dfs(self,source,target):
        """
        Determine if there is a path from source to target using a depth first search
        """
        visited = [False] * self.vertex_count
        self.dfsutil(visited,source,target,)

    def dfsutil(self,visited,source,target):
        """
        Determine if there is a path from source to target using a depth first search.
        :param: visited should be an array of booleans determining if the
        corresponding vertex has been visited already
        """
        visited[source] = True
        for i in self.graph[source]:
            if target in self.graph[source]:
                self.has_path = True
                return
            if not visited[i]:
                self.dfsutil(visited,source,i)

    def is_reachable(self,source,target):
        """
        Determine if there is a path from source to target
        """
        self.has_path = False
        self.dfs(source,target)
        return self.has_path
