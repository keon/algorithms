"""
Defines the Union-Find (or Disjoint Set) data structure.

A disjoint set is made up of a number of elements contained within another
number of sets. Initially, elements are put in their own set, but sets may be
merged using the `unite` operation. We can check if two elements are in the
same seet by comparing their `root`s. If they are identical, the two elements
are in the same set. All operations can be completed in O(a(n)) where `n` is
the number of elements, and `a` the inverse ackermann function. a(n) grows so
slowly that it might as well be constant for any conceivable `n`.
"""

class Union:
    """
    A Union-Find data structure.

    Consider the following sequence of events:
    Starting with the elements 1, 2, 3, and 4:

        {1} {2} {3} {4}

    Initally they all live in their own sets, which means that `root(1) !=
    root(3)`, however, if we call `unite(1, 3)` we would then have the following:

        {1,3} {2} {4}

    Now we have `root(1) == root(3)`, but it is still the case that `root(1) != root(2)`.

    We may call `unite(2, 4)` and end up with:

        {1,3} {2,4}

    Again we have `root(1) != root(2)`. But after `unite(3, 4)` we end up with:

        {1,2,3,4}

    which results in `root(1) == root(2)`.
    """

    def __init__(self):
        self.parents = {}
        self.size = {}
        self.count = 0

    def add(self, element):
        """
        Add a new set containing the single element
        """

        self.parents[element] = element
        self.size[element] = 1
        self.count += 1

    def root(self, element):
        """
        Find the root element which represents the set of a given element.
        That is, all elements that are in the same set will return the same
        root element.
        """

        while element != self.parents[element]:
            self.parents[element] = self.parents[self.parents[element]]
            element = self.parents[element]
        return element

    def unite(self, element1, element2):
        """
        Finds the sets which contains the two elements and merges them into a
        single set.
        """

        root1, root2 = self.root(element1), self.root(element2)
        if root1 == root2:
            return
        if self.size[root1] > self.size[root2]:
            root1, root2 = root2, root1
        self.parents[root1] = root2
        self.size[root2] += self.size[root1]
        self.count -= 1

def num_islands(positions):
    """
    Given a list of positions to operate, count the number of islands
    after each addLand operation. An island is surrounded by water and is
    formed by connecting adjacent lands horizontally or vertically. You may
    assume all four edges of the grid are all surrounded by water.

    Given a 3x3 grid, positions = [[0,0], [0,1], [1,2], [2,1]].
    Initially, the 2d grid grid is filled with water.
    (Assume 0 represents water and 1 represents land).

    0 0 0
    0 0 0
    0 0 0
    Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

    1 0 0
    0 0 0   Number of islands = 1
    0 0 0
    Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

    1 1 0
    0 0 0   Number of islands = 1
    0 0 0
    Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

    1 1 0
    0 0 1   Number of islands = 2
    0 0 0
    Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

    1 1 0
    0 0 1   Number of islands = 3
    0 1 0
    """

    ans = []
    islands = Union()
    for position in map(tuple, positions):
        islands.add(position)
        for delta in (0, 1), (0, -1), (1, 0), (-1, 0):
            adjacent = (position[0] + delta[0], position[1] + delta[1])
            if adjacent in islands.parents:
                islands.unite(position, adjacent)
        ans += [islands.count]
    return ans
