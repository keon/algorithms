"""
Union-Find (Count Islands)

Implements Union-Find (Disjoint Set) data structure and uses it to solve the
"Number of Islands" problem. Supports union by size and path compression,
yielding nearly O(1) amortized operations.

Reference: https://en.wikipedia.org/wiki/Disjoint-set_data_structure

Complexity:
    Union/Find operations:
        Time:  O(alpha(n)) amortized (inverse Ackermann)
        Space: O(n)
    num_islands:
        Time:  O(m * alpha(m)) where m is number of positions
        Space: O(m)
"""

from __future__ import annotations


class Union:
    """A Union-Find (Disjoint Set) data structure.

    Supports adding elements, finding set representatives, and merging sets.
    Uses union by size and path compression for near-constant amortized time.

    Examples:
        >>> uf = Union()
        >>> uf.add(1); uf.add(2); uf.add(3)
        >>> uf.unite(1, 2)
        >>> uf.root(1) == uf.root(2)
        True
        >>> uf.root(1) == uf.root(3)
        False
    """

    def __init__(self) -> None:
        self.parents: dict[object, object] = {}
        self.size: dict[object, int] = {}
        self.count: int = 0

    def add(self, element: object) -> None:
        """Add a new singleton set containing the given element.

        Args:
            element: The element to add.
        """
        self.parents[element] = element
        self.size[element] = 1
        self.count += 1

    def root(self, element: object) -> object:
        """Find the root representative of the set containing element.

        Args:
            element: The element whose root to find.

        Returns:
            The root representative of the element's set.
        """
        while element != self.parents[element]:
            self.parents[element] = self.parents[self.parents[element]]
            element = self.parents[element]
        return element

    def unite(self, element1: object, element2: object) -> None:
        """Merge the sets containing the two elements.

        Args:
            element1: An element in the first set.
            element2: An element in the second set.
        """
        root1, root2 = self.root(element1), self.root(element2)
        if root1 == root2:
            return
        if self.size[root1] > self.size[root2]:
            root1, root2 = root2, root1
        self.parents[root1] = root2
        self.size[root2] += self.size[root1]
        self.count -= 1


def num_islands(positions: list[list[int]]) -> list[int]:
    """Count islands after each addLand operation.

    Given a sequence of positions on a 2D grid, each operation turns a water
    cell into land. After each operation, count the number of distinct islands
    (connected components of land cells).

    Args:
        positions: A list of [row, col] pairs indicating land additions.

    Returns:
        A list of island counts, one per operation.

    Examples:
        >>> num_islands([[0, 0], [0, 1], [1, 2], [2, 1]])
        [1, 1, 2, 3]
    """
    result: list[int] = []
    islands = Union()
    for position in map(tuple, positions):
        islands.add(position)
        for delta in (0, 1), (0, -1), (1, 0), (-1, 0):
            adjacent = (position[0] + delta[0], position[1] + delta[1])
            if adjacent in islands.parents:
                islands.unite(position, adjacent)
        result.append(islands.count)
    return result
