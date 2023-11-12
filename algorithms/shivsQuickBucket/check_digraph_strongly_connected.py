# 1192. Critical Connections in a Network
# Tarjan's Algorithm

# tin -> Time of insertion
# low -> lowest time of insertion that can be reached

from collections import defaultdict as dd


class Solution:
    def criticalConnections(self, n: int, connections):
        graph = dd(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        visited = set([0])
        tin = [0] * n
        low = [0] * n
        res = []

        def recursion(node, parent, timer):
            tin[node] = low[node] = timer
            timer += 1
            for nei in graph[node]:
                if nei == parent:
                    continue
                if nei not in visited:
                    visited.add(node)
                    recursion(nei, node, timer + 1)
                    low[node] = min(low[node], low[nei])
                    if low[nei] > tin[node]:
                        res.append([node, nei])
                else:
                    low[node] = min(low[node], low[nei])

        recursion(0, 0, 1)
        return res
