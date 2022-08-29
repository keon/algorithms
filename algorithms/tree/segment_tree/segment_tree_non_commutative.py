from math import ceil, log2
class SegmentTree:
    def __init__(self, arr, n):
        arr, n = self.correct_arr(arr, n)
        self.tree = [None] * n + arr
        self.n = n
        self.op = lambda x, y: x + y
        self.build_tree()
    
    def correct_arr(self, arr, n):
        new_size = 2 ** ceil(log2(n))
        arr += ['0'] * (new_size - n)
        n = new_size
        return arr, n

    def build_tree(self):
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.op(self.tree[2 * i], self.tree[(2 * i) + 1])
    
    def update(self, p):
        p += self.n
        if self.tree[p] == '0':
            self.tree[p] = '1'
            while p > 1:
                p //= 2
                self.tree[p] = self.op(self.tree[2 * p], self.tree[(2 * p) + 1])
    
    def query(self,l, r):
        l += self.n
        r += self.n
        resl, resr = None, None
        while l <= r:
            if l & 1:
                resl = self.tree[l] if resl is None else self.op(resl, self.tree[l])
            if not (r & 1):
                resr = self.tree[r] if resr is None else self.op(self.tree[r], resr)
            l, r = (l + 1) // 2, (r - 1) // 2
        if resl and resr: return resl + resr
        elif resl and not resr: return resl
        else: return resr