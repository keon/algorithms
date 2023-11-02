# 1135. Connecting Cities With Minimum Cost

from collections import defaultdict as dd
import heapq
# Prims solution
class Solution:
    def minimumCost(self, n, cc) -> int:
        if len(cc) < n - 1: return -1
        visited = set()
        cc2 = dd(list)
        for p1, p2, cost in cc:
            cc2[p1].append((cost, p2))
            cc2[p2].append((cost, p1))
        res = 0
        heap = [(0, cc[0][0])]
        while heap and len(visited) < n:
            cost, node = heapq.heappop(heap)
            if node not in visited:
                res += cost
                visited.add(node)
                for cost, nei in cc2[node]:
                    heapq.heappushpop(heap, (cost, nei))
        return res if len(visited) == n else -1