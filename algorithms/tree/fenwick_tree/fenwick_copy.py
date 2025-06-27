"""
Fenwick Tree / Binary Indexed Tree

Consider we have an array arr[0 . . . n-1]. We would like to
1. Compute the sum of the first i elements.
2. Modify the value of a specified element of the array arr[i] = x where 0 <= i <= n-1.

A simple solution is to run a loop from 0 to i-1 and calculate the sum of the elements. To update a value, simply do arr[i] = x.
The first operation takes O(n) time and the second operation takes O(1) time.
Another simple solution is to create an extra array and store the sum of the first i-th elements at the i-th index in this new array.
The sum of a given range can now be calculated in O(1) time, but the update operation takes O(n) time now.
This works well if there are a large number of query operations but a very few number of update operations.


There are two solutions that can perform both the query and update operations in O(logn) time.
1. Fenwick Tree
2. Segment Tree

Compared with Segment Tree, Binary Indexed Tree requires less space and is easier to implement.
"""

class Fenwick_Tree(object):
    def __init__(self, freq):
        self.arr = freq
        self.n = len(freq)
    def get_sum(self, bit_tree, i):
        s = 0
        i = i+1
        while i > 0:
            s += bit_tree[i]
            i -= i & (-i) 
        return s
    def update_bit(self, bit_tree, i, v):
        i += 1
        while i <= self.n:
            bit_tree[i] += v
            i += i & (-i)
    def construct(self):
        bit_tree = [0]*(self.n+1)
        for i in range(self.n):
            self.update_bit(bit_tree, i, self.arr[i])
        return bit_tree