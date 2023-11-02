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
    def minimumCost(self, n, cc) -> int:
        if len(cc) < n - 1: return -1
        for pp in range(len(cc)):
            cc[pp] = cc[pp][::-1]
        
        heapq.heapify(cc)
        disset = Disset(n + 1)
        count = 0
        while cc and count < n - 1:
            cost, p1, p2 = heapq.heappop(cc)
            if disset.union(cost, p1, p2): count += 1
        
        return disset.cost if count == n - 1 else -1