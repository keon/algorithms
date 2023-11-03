# 1135. Connecting Cities With Minimum Cost

from collections import defaultdict as dd
import heapq
# Krushkal's solution
class Disset: #Disjoint Set Data Structure
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [0] * n
        self.cost = 0
        
    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, cost, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
                self.rank[rootx] += 1
            elif self.rank[rooty] > self.rank[rootx]:
                self.root[rootx] = rooty
                self.rank[rooty] += 1
            else:
                self.root[rootx] = rooty
                self.rank[rooty] += 1
            self.cost += cost
            return True
        return False

class Solution:
    def minimumCost(self, n, connections) -> int:
        if len(connections) < n - 1: return -1

        # Make Disjoint sets DS
        disset = Disset(n + 1)

        # Sort the edges based on cost
        for node in range(len(connections)):
            connections[node] = connections[node][::-1]
        connections.sort(reverse = True)

        # Keep choosing edges till we get to N - 1 edges
        edges = 0
        while connections and edges < n - 1:
            cost, p1, p2 = connections.pop()
            if disset.union(cost, p1, p2): edges += 1
        
        return disset.cost if edges == n - 1 else -1