class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0 for _ in range(n + 1)]
    
    def update(self, idx, val):
        while idx <= self.n:
            self.tree[idx] += val
            idx += idx&(-idx)
    
    def query(self, idx):
        total = 0
        while idx > 0:
            total += self.tree[idx]
            idx -= idx&(-idx)
        return total