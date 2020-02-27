# Dijkstra's single source shortest path algorithm
from algorithms.heap import BinaryHeap, FibonacciHeap


class Dijkstra:
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

            # minimum distance vertex that is not processed
            u = self.min_distance(dist, min_dist_set)

            # put minimum distance vertex in shortest tree
            min_dist_set[u] = True

            # Update dist value of the adjacent vertices
            for v in range(self.vertices):
                if (
                    self.graph[u][v] > 0
                    and min_dist_set[v] == False
                    and dist[v] > dist[u] + self.graph[u][v]
                ):
                    dist[v] = dist[u] + self.graph[u][v]

        return dist

    def dijkstra_using_heap(self, src):
        if self.vertices == 0:
            return []

        heap = BinaryHeap()
        dist = [float("inf")] * self.vertices

        tuple = (0, src)
        heap.insert(tuple)
        dist[src] = 0

        while heap.currentSize > 0:
            u = heap.remove_min()
            curWeight = u[0]
            curNode = u[1]

            # go over all vertices adjacent to u
            for v in range(self.vertices):
                if (
                    self.graph[curNode][v] > 0
                    and dist[v] > dist[curNode] + self.graph[curNode][v]
                ):
                    dist[v] = dist[curNode] + self.graph[curNode][v]
                    t = (dist[v], v)
                    heap.insert(t)
        return dist

    def dijkstra_fib_heap(self, src):
        """
        Dijkstra's using a Fibonacci heap. Theoretically reduces
        the time complexity of the algorithm. In practice Fib heaps
        have high constants and is therefore sometimes slower than
        a normal binomial heap.
        """
        if self.vertices == 0:
            return []

        heap = FibonacciHeap()

        dist = [float("inf")] * self.vertices
        nodes = []

        source = heap.insert((0, src))
        nodes.append(source)

        for v in range(1, self.vertices):
            inserted_node = heap.insert((dist[v], v))
            nodes.append(inserted_node)

        dist[src] = 0

        for v in range(self.vertices):
            node = heap.extract_min_node()
            distance, node_id = node.key

            # go over all vertices adjacent to u
            for u in range(self.vertices):
                if (
                    self.graph[node_id][u] > 0
                    and dist[u] > distance + self.graph[node_id][u]
                ):
                    dist[u] = dist[node_id] + self.graph[node_id][u]
                    heap.decrease_key(nodes[u], (dist[u], u))
        return dist
