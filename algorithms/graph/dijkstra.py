# from collections import namedtuple

# Dijkstra's Single-Source Shortest Paths algorithm
# NOTE: UNcomment Line 1, 14 and 40 to use a Named Tuple as Result (it will run slower though)


class Dijkstra:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = None
        self.v_distance = [float("inf")] * self.vertices
        self.shortest_path = [False] * self.vertices  # FAQ: Checks if a Vertices' shortest route has been found.
        #  self.ShortestPathTree = namedtuple('ShortestPathTree', ['V_' + str(V+1) for V in range(self.vertices)])

    def min_distance(self):
        check_node = float("inf")
        min_index = 0
        for v in range(self.vertices):
            if not self.v_distance[v]:
                continue
            elif self.v_distance[v] < check_node and not self.shortest_path[v]:
                check_node = self.v_distance[v]  # FAQ: Set min_dist to Current Dist[v]
                min_index = v
        return min_index

    def dijkstra(self, source):

        self.v_distance[source] = 0  # FAQ: Set Starting Node by Index as 0

        for idx, _ in enumerate(range(self.vertices)):
            if idx != 0:  # FAQ: Algorithm will always start at index 0 because the Graph is relative to source
                current = self.min_distance()  # -> Get the Index of Vertex with shortest route 
            else:
                current = idx
                self.shortest_path[idx] = True
            self.neighbour_path(current)


        # shortest_path = self.ShortestPathTree(*self.v_distance)
        return self.v_distance

    def neighbour_path(self, current):
        
        for v in range(self.vertices): # FAQ: Check neighbour Nodes and Update distance
            neighbour = self.graph[current][v]
            if neighbour <= 0:
                continue
            n_path = self.v_distance[current] + neighbour
            if v == current:  # FAQ: Skip himself in the check as it's always 0
                continue
            elif self.v_distance[v] > n_path:
                self.shortest_path[current] = True
                self.v_distance[v] = n_path
            else:
                continue


# NOTE: Dijkstra's single source shortest path algorithm complete traversal (Not A to B);
#  Spanning Tree = T
#  undirected graph = G
#  Shortest-path Tree Distance from root v to vertex u = shortest path
#  Map = Graph G
#  Road = Edge E
#  Intersection = Vertex V
