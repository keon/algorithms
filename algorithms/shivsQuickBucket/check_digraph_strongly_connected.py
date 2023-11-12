from collections import defaultdict as dd

# n: No. of nodes


class Graph:
    def __init__(self, n):
        self.n = n
        self.graph = dd(list)

    def add_edge(self, source, target):
        self.graph[source].append(target)

    def dfs(self):
        visited = [False] * self.n
        orderStack = []
        self.dfs_util(0, visited, orderStack)
        return visited == [True] * self.n

    def dfs_util(self, source, visited, stack):
        visited[source] = True
        for adjacent in self.graph[source]:
            if not visited[adjacent]:
                self.dfs_util(adjacent, visited, stack)
        stack.append(source)

    def reverse_graph(self):
        reversedGraph = Graph(self.n)
        for source, adjacent in self.graph.items():
            for target in adjacent:
                reversedGraph.add_edge(target, source)
        return reversedGraph

    def is_strongly_connected(self):
        if self.dfs():
            reversedGraph = self.reverse_graph()
            if reversedGraph.dfs():
                return True
        return False
