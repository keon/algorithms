class DSU:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [1] * n
        self.count = 0

    def find(self, x):
        if self.root[x] == x: return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            if self.rank[rootx] >= self.rank[rooty]:
                self.root[rooty] = rootx
                self.rank[rootx] += self.rank[rooty]
            else:
                self.root[rootx] = rooty
                self.rank[rooty] += self.rank[rootx]
            self.count += 1
            return True
        else: return False