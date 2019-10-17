#Dijkstra's single source shortest path algorithm

class Dijkstra():

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def min_distance(self, dist, min_dist_set):
        min_dist = float("inf")
        for v in range(self.vertices):
            if dist[v] < min_dist and min_dist_set[v] == False:
                min_dist = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):

        dist = [float("inf")] * self.vertices
        dist[src] = 0
        min_dist_set = [False] * self.vertices

        for count in range(self.vertices):

            #minimum distance vertex that is not processed
            u = self.min_distance(dist, min_dist_set)

            #put minimum distance vertex in shortest tree
            min_dist_set[u] = True

            #Update dist value of the adjacent vertices
            for v in range(self.vertices):
                if self.graph[u][v] > 0 and min_dist_set[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        return dist
