from math import log2


class BIT:
    def __init__(self, n):
        self.n = n + 1
        self.tree = [0 for _ in range(self.n)]
    
    def update(self, idx, val=1):
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
    
    # finding kth smallest element Upper Bound with Time - O(logN ^ 2)
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
    
    # Upper bound Kth smallest -- O(logN) using binary lifting
    def find_BL(self, k):
        pos = rs = 0
        nn = int(log2(self.n))

        for i in reversed(range(nn + 1)):
            if pos + (1 << i) < self.n and rs + self.tree[pos + (1 << i)] < k:
                pos += (1 << i)
                rs += self.tree[pos]
        return pos + 1
    

# Note - 
# This BIT is for 1, 10 ** 5 scenarios
# For 0-indexed cases just make everything + 1 shift the system by 1 on the right