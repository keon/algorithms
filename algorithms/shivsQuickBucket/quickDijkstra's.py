from heapq import heappop, heappush
from math import inf


class Dijkstra():
    def __init__(self):
        return
    
    @staticmethod
    def get_shortest_path(adj, src):
        n = len(adj)
        min_d = [inf] * n
        heap = [(0, src)]
        min_d[src] = 0

        while heap:
            cost, node = heappop(heap)
            if cost > min_d[node]: continue
            for new_node, new_cost in adj[node]:
                total_cost = cost + new_cost
                if total_cost < min_d[new_node]:
                    min_d[new_node] = total_cost
                    heappush(heap, (total_cost, new_node))
        return min_d