"""
Algorithm: Kahn's Algorithm (Topological Sort using BFS)
Author: [Your Name]
Time Complexity: O(V + E)
"""
from collections import deque
from typing import List

class Solution:
    def topological_sort(self, V: int, adj: List[List[int]]) -> List[int]:
        in_degree = [0] * V
        for i in range(V):
            for neighbor in adj[i]:
                in_degree[neighbor] += 1
        
        queue = deque([i for i in range(V) if in_degree[i] == 0])
        topo_order = []
        
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(topo_order) != V:
            return [] # Cycle detected
            
        return topo_order