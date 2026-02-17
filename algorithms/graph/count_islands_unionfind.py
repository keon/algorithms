"""
Count Islands via Union-Find

Uses the Union-Find (Disjoint Set) data structure to solve the "Number of
Islands" problem. After each addLand operation, counts distinct connected
components of land cells.

Reference: https://en.wikipedia.org/wiki/Disjoint-set_data_structure

Complexity:
    Time:  O(m * alpha(m)) where m is number of positions
    Space: O(m)
"""

from __future__ import annotations

from algorithms.data_structures.union_find import Union


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
