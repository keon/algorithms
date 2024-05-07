from collections import Counter


class SEG:
    def __init__(self):
        self.tree = Counter()
        self.lazy = Counter()

    def update(self, s, e, l=0, r=10**9, idx=1):
        if s > r or e < l: return

        if s <= l <= r <= e:
            self.tree[idx] += 1
            self.lazy[idx] += 1
        else:
            m = (l + r) >> 1
            self.update(s, e, l, m, idx * 2)
            self.update(s, e, m + 1, r, idx * 2 + 1)
            self.tree[idx] = self.lazy[idx] + self.fn(self.tree[2 * idx], self.tree[2 * idx + 1])
    
    def query(self, s, e, l=0, r=10**9, idx=1):
        if s > r or e < l: return

        if s <= l <= r <= e:
            return self.tree[idx]
        else:
            m = (l + r) >> 1
            A = self.query(s, e, l, m, idx * 2)
            B = self.query(s, e, m + 1, r, idx * 2 + 1)
            return self.fn(A, B)
