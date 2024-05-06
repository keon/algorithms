class SEG:
    def __init__(self, n, fn, query_fn):
        self.n = n
        self.H = 1
        while 1 << self.H < n:
            self.H += 1

        self.fn = fn
        self.query_fn = query_fn
        self.tree = [0] * (2 * n)
        self.lazy = [0] * n

    def _apply(self, idx, val):
        self.tree[idx] = self.fn(self.tree[idx], val)
        if idx < self.n: # checking so we do not apply lazy to leaf nodes (our original array)
            self.lazy[idx] = self.fn(self.lazy[idx], val)

    def _pull(self, idx):
        while idx > 1:
            idx >>= 1
            self.tree[idx] = self.fn(self.lazy[idx], self.query_fn(self.tree[idx*2], self.tree[idx*2 + 1]))

    def _push(self, idx):
        for h in range(self.H, 0, -1):
            y = idx >> h
            if self.lazy[y]:
                self._apply(y * 2, self.lazy[y])
                self._apply(y * 2+ 1, self.lazy[y])
                self.lazy[y] = 0

    def update(self, l, r, val):
        l, r = l + self.n, r + self.n
        L, R = l, r
        while l <= r:
            if l & 1:
                self._apply(l, val)
            if not r & 1:
                self._apply(r, val)
            l, r = (l + 1) >> 1, (r - 1) >> 1
        self._pull(L); self._pull(R)

    def query(self, l, r):
        l, r = l + self.n, r + self.n
        self._push(l); self._push(r)
        res = None
        while l <= r:
            if l & 1:
                res = self.tree[l] if res is None else self.query_fn(res, self.tree[l])
            if not r & 1:
                res = self.tree[r] if res is None else self.query_fn(res, self.tree[r])
            l, r = (l + 1) >> 1, (r - 1) >> 1
        return res