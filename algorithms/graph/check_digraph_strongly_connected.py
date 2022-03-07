"""
In a directed graph, a strongly connected component is a set of vertices such
that for any pairs of vertices u and v there exists a path (u-...-v) that
connects them. A graph is strongly connected if it is a single strongly
connected component.
"""

from collections import defaultdict

class Graph:
    """
    A directed graph where edges are one-way (a two-way edge can be represented by using two edges).
    """

    def __init__(self,vertex_count):
        """
        Create a new graph with vertex_count vertices.
        """

        self.vertex_count = vertex_count
        self.graph = defaultdict(list)

    def add_edge(self,source,target):
        """
        Add an edge going from source to target
        """
        self.graph[source].append(target)

    def dfs(self):
        """
        Determine if all nodes are reachable from node 0
        """
        visited = [False] * self.vertex_count
        self.dfs_util(0,visited)
        if visited == [True]*self.vertex_count:
            return True
        return False

    def dfs_util(self,source,visited):
        """
        Determine if all nodes are reachable from the given node
        """
        visited[source] = True
        for adjacent in self.graph[source]:
            if not visited[adjacent]:
                self.dfs_util(adjacent,visited)

    def reverse_graph(self):
        """
        Create a new graph where every edge a->b is replaced with an edge b->a
        """
        reverse_graph = Graph(self.vertex_count)
        for source, adjacent in self.graph.items():
            for target in adjacent:
                # Note: we reverse the order of arguments
                # pylint: disable=arguments-out-of-order
                reverse_graph.add_edge(target,source)
        return reverse_graph


    def is_strongly_connected(self):
        """
        Determine if the graph is strongly connected.
        """
        if self.dfs():
            reversed_graph = self.reverse_graph()
            if reversed_graph.dfs():
                return True
        return False
