class BIT:
    def __init__(self, n):
        self.n = n + 1
        self.tree = [0 for _ in range(self.n)]
    
    def update(self, idx, val):
        idx += 1
        while idx < self.n:
            self.tree[idx] += val
            idx += idx&-idx
    
    def query(self, idx):
        idx += 1
        total = 0
        while idx:
            total += self.tree[idx]
            idx -= idx&-idx
        return total
    
    # finding kth smallest element
    def find(self, k):
        l, r = 1, self.n
        while l <= r:
            m = (l + r) >> 1
            if self.query(m) >= k:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res