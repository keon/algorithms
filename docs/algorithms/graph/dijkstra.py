"""
Dijkstra's single-source shortest-path algorithm
"""

class Dijkstra():
    """
    A fully connected directed graph with edge weights
    """

    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.graph = [[0 for _ in range(vertex_count)] for _ in range(vertex_count)]

    def min_distance(self, dist, min_dist_set):
        """
        Find the vertex that is closest to the visited set
        """
        min_dist = float("inf")
        for target in range(self.vertex_count):
            if min_dist_set[target]:
                continue
            if dist[target] < min_dist:
                min_dist = dist[target]
                min_index = target
        return min_index

    def dijkstra(self, src):
        """
        Given a node, returns the shortest distance to every other node
        """
        dist = [float("inf")] * self.vertex_count
        dist[src] = 0
        min_dist_set = [False] * self.vertex_count

        for _ in range(self.vertex_count):
            #minimum distance vertex that is not processed
            source = self.min_distance(dist, min_dist_set)

            #put minimum distance vertex in shortest tree
            min_dist_set[source] = True

            #Update dist value of the adjacent vertices
            for target in range(self.vertex_count):
                if self.graph[source][target] <= 0 or min_dist_set[target]:
                    continue
                if dist[target] > dist[source] + self.graph[source][target]:
                    dist[target] = dist[source] + self.graph[source][target]

        return dist
