"""
Van Emde Boas Tree (vEB Tree) / van Emde Boas priority queue

Reference: https://en.wikipedia.org/wiki/Van_Emde_Boas_tree

A van Emde Boas tree is a recursive data structure for storing integers
from a fixed universe [0, u - 1], where u is a power of 2.

Time complexity:
    insert / delete / successor / member : O(log log u)
    min / max                            : O(1)

Space complexity:
    O(u)
"""

import math


class VEBTree:
    """
    Van Emde Boas tree supporting fast predecessor/successor queries.

    Attributes:
        u (int): Universe size (power of 2)
        min (int | None): Minimum element in the tree
        max (int | None): Maximum element in the tree
        summary (VEBTree | None): Summary tree
        cluster (list[VEBTree] | None): Array of clusters
    """

    def __init__(self, universe_size):
        """
        Initialize a Van Emde Boas tree.

        Args:
            universe_size (int): Size of the universe; must be a power of 2 and > 0.

        Raises:
            TypeError: If universe_size is not an integer.
            ValueError: If universe_size <= 0 or not a power of 2.
        """
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
        """
        Check if x is within the universe range.

        Args:
            x (int): Element to validate.

        Raises:
            ValueError: If x is not in the range [0, u-1].
        """
        if not (0 <= x < self.u):
            raise ValueError(f"Key {x} out of universe range [0, {self.u - 1}]")

    def high(self, x):
        """
        Return the high part (cluster index) of element x.

        Args:
            x (int): Element to split.

        Returns:
            int: Cluster index corresponding to x.
        """
        return x // self.lower_sqrt

    def low(self, x):
        """
        Return the low part (position within cluster) of element x.

        Args:
            x (int): Element to split.

        Returns:
            int: Position within cluster corresponding to x.
        """
        return x % self.lower_sqrt

    def index(self, high, low):
        """
        Combine high and low parts to get original element.

        Args:
            high (int): Cluster index.
            low (int): Position within cluster.

        Returns:
            int: Original element corresponding to high and low.
        """
        return high * self.lower_sqrt + low

    def empty_insert(self, x):
        """
        Insert x into an empty vEB tree (sets min and max).

        Args:
            x (int): Element to insert.
        """
        self.min = self.max = x

    def insert(self, x):
        """
        Insert an element into the Van Emde Boas tree.

        Args:
            x (int): Element to insert; must be in the universe [0, u-1].

        Raises:
            ValueError: If x is outside the universe.
        """
        self._validate_key(x)
        if self.min is None:
            self.empty_insert(x)
            return

        if x < self.min:
            x, self.min = self.min, x

        if self.u > 2:
            high = self.high(x)
            low = self.low(x)

            if self.cluster[high].min is None:
                self.summary.insert(high)
                self.cluster[high].empty_insert(low)
            else:
                self.cluster[high].insert(low)

        if x > self.max:
            self.max = x

    def member(self, x):
        """
        Check whether element x exists in the tree.

        Args:
            x (int): Element to check.

        Returns:
            bool: True if x exists, False otherwise.

        Raises:
            ValueError: If x is outside the universe.
        """
        self._validate_key(x)
        if x == self.min or x == self.max:
            return True
        elif self.u == 2:
            return False
        else:
            return self.cluster[self.high(x)].member(self.low(x))

    def successor(self, x):
        """
        Return the smallest element greater than x in the tree.

        Args:
            x (int): Element to find successor for.

        Returns:
            int | None: Successor of x if exists, otherwise None.

        Raises:
            ValueError: If x is outside the universe.
        """
        self._validate_key(x)
        if self.u == 2:
            if x == 0 and self.max == 1:
                return 1
            return None

        if self.min is not None and x < self.min:
            return self.min

        high = self.high(x)
        low = self.low(x)

        max_low = self.cluster[high].max

        if max_low is not None and low < max_low:
            offset = self.cluster[high].successor(low)
            return self.index(high, offset)
        else:
            succ_cluster = self.summary.successor(high)
            if succ_cluster is None:
                return None
            offset = self.cluster[succ_cluster].min
            return self.index(succ_cluster, offset)

    def delete(self, x):
        """
        Remove element x from the Van Emde Boas tree.

        Args:
            x (int): Element to delete.

        Raises:
            ValueError: If x is outside the universe.
        """
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

        high = self.high(x)
        low = self.low(x)
        self.cluster[high].delete(low)

        if self.cluster[high].min is None:
            self.summary.delete(high)

            if x == self.max:
                summary_max = self.summary.max
                if summary_max is None:
                    self.max = self.min
                else:
                    self.max = self.index(summary_max, self.cluster[summary_max].max)
        elif x == self.max:
            self.max = self.index(high, self.cluster[high].max)

    def minimum(self):
        """
        Get the minimum element in the tree.

        Returns:
            int | None: Minimum element, or None if tree is empty.
        """
        return self.min

    def maximum(self):
        """
        Get the maximum element in the tree.

        Returns:
            int | None: Maximum element, or None if tree is empty.
        """
        return self.max
