"""
Van Emde Boas Tree (vEB Tree) / van Emde Boas priority queue

Reference: https://en.wikipedia.org/wiki/Van_Emde_Boas_tree

A van Emde Boas tree is a recursive data structure for storing integers
from a fixed universe [0, u - 1], where u is a power of 2.

Core idea:
    Recursively split the universe of size u into:
        - sqrt(u) clusters of size sqrt(u)
        - a summary structure tracking which clusters are non-empty

Each node stores:
    - min: smallest element
    - max: largest element
    - summary: vEB tree over cluster indices
    - cluster[]: array of vEB trees for subranges

Operations work by:
    - Decomposing a key x into:
          high(x) -> cluster index
          low(x)  -> position within cluster
    - Recursing into the appropriate cluster
    - Using the summary to find the next non-empty cluster when needed

Time complexity:
    insert      : O(log log u)
    delete      : O(log log u)
    successor   : O(log log u)
    member      : O(log log u)
    min / max   : O(1)

Space complexity:
    O(u)

Where:
    u = universe size (must be a power of 2)

Strength:
    Extremely fast operations for integer keys.

Weakness:
    High memory usage proportional to universe size.
"""


import math

class VEBTree:
    def __init__(self, universe_size):
        if not isinstance(universe_size, int):
            raise TypeError("universe_size must be an integer.")
        if not universe_size > 0:
            raise ValueError("universe_size must be greater than 0.")
        if not (universe_size & (universe_size - 1)) == 0:
            raise ValueError("universe_size must be a power of 2.")

        self.u = universe_size
        self.min = None
        self.max = None
        
        if universe_size <= 2:
            self.summary = None
            self.cluster = None
        else:
            self.lower_sqrt = 2 ** (math.floor(math.log2(universe_size) / 2))
            self.upper_sqrt = 2 ** (math.ceil(math.log2(universe_size) / 2))
            
            self.summary = VEBTree(self.upper_sqrt)
            self.cluster = [VEBTree(self.lower_sqrt) for _ in range(self.upper_sqrt)]

    def _validate_key(self, x):
        if not (0 <= x < self.u):
            raise ValueError(f"Key {x} out of universe range [0, {self.u - 1}]")

    def high(self, x):
        return x // self.lower_sqrt

    def low(self, x):
        return x % self.lower_sqrt

    def index(self, high, low):
        return high * self.lower_sqrt + low

    def empty_insert(self, x):
        self.min = self.max = x

    def insert(self, x):
        self._validate_key(x)
        if self.min is None:
            self.empty_insert(x)
            return
        
        if x < self.min:
            x, self.min = self.min, x
        
        if self.u > 2:
            h = self.high(x)
            l = self.low(x)
            
            if self.cluster[h].min is None:
                self.summary.insert(h)
                self.cluster[h].empty_insert(l)
            else:
                self.cluster[h].insert(l)
        
        if x > self.max:
            self.max = x

    def member(self, x):
        self._validate_key(x)
        if x == self.min or x == self.max:
            return True
        elif self.u == 2:
            return False
        else:
            return self.cluster[self.high(x)].member(self.low(x))

    def successor(self, x):
        self._validate_key(x)
        if self.u == 2:
            if x == 0 and self.max == 1:
                return 1
            return None
        
        if self.min is not None and x < self.min:
            return self.min
        
        h = self.high(x)
        l = self.low(x)
        
        max_low = self.cluster[h].max
        
        if max_low is not None and l < max_low:
            offset = self.cluster[h].successor(l)
            return self.index(h, offset)
        else:
            succ_cluster = self.summary.successor(h)
            if succ_cluster is None:
                return None
            offset = self.cluster[succ_cluster].min
            return self.index(succ_cluster, offset)

    def delete(self, x):
        self._validate_key(x)
        if self.min == self.max:
            self.min = self.max = None
            return
        
        if self.u == 2:
            if x == 0:
                self.min = 1
            else:
                self.min = 0
            self.max = self.min
            return
        
        if x == self.min:
            first_cluster = self.summary.min
            x = self.index(first_cluster, self.cluster[first_cluster].min)
            self.min = x
        
        h = self.high(x)
        l = self.low(x)
        self.cluster[h].delete(l)
        
        if self.cluster[h].min is None:
            self.summary.delete(h)
            
            if x == self.max:
                summary_max = self.summary.max
                if summary_max is None:
                    self.max = self.min
                else:
                    self.max = self.index(
                        summary_max,
                        self.cluster[summary_max].max
                    )
        elif x == self.max:
            self.max = self.index(h, self.cluster[h].max)

    def minimum(self):
        return self.min

    def maximum(self):
        return self.max