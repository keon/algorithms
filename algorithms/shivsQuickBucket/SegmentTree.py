"""
SegmentTree creates a segment tree with a given array and a "commutative" function,
this non-recursive version uses less memory than the recursive version and include:
1. range queries in log(N) time
2. update an element in log(N) time
the function should be commutative and takes 2 values and returns the same type value

Examples -
mytree = SegmentTree([2, 4, 5, 3, 4],max)
print(mytree.query(2, 4))
mytree.update(3, 6)
print(mytree.query(0, 3)) ...

mytree = SegmentTree([4, 5, 2, 3, 4, 43, 3], lambda a, b: a + b)
print(mytree.query(0, 6))
mytree.update(2, -10)
print(mytree.query(0, 6)) ...

mytree = SegmentTree([(1, 2), (4, 6), (4, 5)], lambda a, b: (a[0] + b[0], a[1] + b[1]))
print(mytree.query(0, 2))
mytree.update(2, (-1, 2))
print(mytree.query(0, 2)) ...
"""


class SEG:
    def __init__(self, arr, function):
        self.n = len(arr)
        self.tree = [0 for _ in range(self.n)] + arr
        self.fn = function
        self.build_tree(self.n)

    def build_tree(self, n):
        for i in range(n - 1, 0, -1):
            self.tree[i] = self.fn(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, idx, value):
        idx += self.n
        self.tree[idx] = value
        while idx > 1:
            idx >>= 1
            self.tree[idx] = self.fn(self.tree[2 * idx], self.tree[2 * idx + 1])

    def query(self, l, r):
        l, r = l + self.n, r + self.n
        res = None
        while l <= r:
            if l & 1:
                res = self.tree[l] if res is None else self.fn(res, self.tree[l])
            if not (r & 1):
                res = self.tree[r] if res is None else self.fn(res, self.tree[r])
            l, r = (l + 1) >> 1, (r - 1) >> 1
        return res
