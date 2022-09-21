class SEG:
    def __init__(self, n, fn):
        self.n = n
        self.fn = fn
        self.tree = [0] * 2 * self.n
       
    def query(self, l, r):
        l += self.n
        r += self.n
        ans = 0
        while l < r:
            if l & 1:
                ans = self.fn(ans, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                ans = self.fn(ans, self.tree[r])
            l >>= 1
            r >>= 1
        return ans
    
    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = self.fn(self.tree[i * 2], self.tree[i * 2 + 1])