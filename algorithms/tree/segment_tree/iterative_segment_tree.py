'''
Segment_tree creates a segment tree with a given array and function,
allowing queries to be done later in log(N) time
function takes 2 values and returns a same type value
'''


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
        l += self.size
        r += self.size
        ans = None
        while l <= r:
            if l % 2 == 1:
                ans = self.tree[l] if ans is None else self.fn(ans, self.tree[l])
            if r % 2 == 0:
                ans = self.tree[r] if ans is None else self.fn(ans, self.tree[r])
            l = (l + 1) // 2
            r = (r - 1) // 2
        return ans


'''
Example -
mytree = SegmentTree([2,4,5,3,4],max)
mytree.query(2,4)
mytree.query(0,3) ...

mytree = SegmentTree([4,5,2,3,4,43,3],sum)
mytree.query(1,8)
...

'''
