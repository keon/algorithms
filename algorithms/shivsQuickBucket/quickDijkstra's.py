from heapq import heappop, heappush
from math import inf


class Dijkstra():
    def __init__(self):
        return
    
    @staticmethod
    def get_shortest_path(distances, src):
        n = len(distances)
        min_distance = [inf] * n
        heap = [(0, src)]
        min_distance[src] = 0
        visited = set()

        while heap:
            cost, node = heappop(heap)
            if node in visited: continue
            visited.add(node)
            for new_node, new_cost in distances[node]:
                total_cost = cost + new_cost
                if total_cost < min_distance[new_node]:
                    min_distance[new_node] = total_cost
                    heappush(heap, (total_cost, new_node))
        return min_distance