# 1135. Connecting Cities With Minimum Cost

from collections import defaultdict as dd
import heapq
# Prims solution
class Solution:
    def minimumCost(self, n, connections) -> int:
        if len(connections) < n - 1: return -1
        visited = set()

        # make neighbours dictionary
        neighbours = dd(list)
        for p1, p2, cost in connections:
            neighbours[p1].append((cost, p2))
            neighbours[p2].append((cost, p1))
        
        res = 0

        # start with the heap operations
        heap = [(0, connections[0][0])]
        while heap and len(visited) < n:
            cost, node = heapq.heappop(heap)
            # this pop means this node will now be connected
            if node not in visited:
                res += cost
                visited.add(node)
                for cost, nei in neighbours[node]:
                    heapq.heappush(heap, (cost, nei))
        return res if len(visited) == n else -1