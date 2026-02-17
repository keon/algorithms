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


class SegmentTree:
    def __init__(self, arr, function):
        self.tree = [None for _ in range(len(arr))] + arr
        self.size = len(arr)
        self.fn = function
        self.build_tree()

    def build_tree(self):
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.fn(self.tree[i * 2], self.tree[i * 2 + 1])

    def update(self, p, v):
        p += self.size
        self.tree[p] = v
        while p > 1:
            p = p // 2
            self.tree[p] = self.fn(self.tree[p * 2], self.tree[p * 2 + 1])

    def query(self, l, r):
        l, r = l + self.size, r + self.size
        res = None
        while l <= r:
            if l % 2 == 1:
                res = self.tree[l] if res is None else self.fn(res, self.tree[l])
            if r % 2 == 0:
                res = self.tree[r] if res is None else self.fn(res, self.tree[r])
            l, r = (l + 1) // 2, (r - 1) // 2
        return res
