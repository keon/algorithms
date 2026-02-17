"""
Cycle Sort

Cycle sort decomposes the permutation into cycles and rotates each cycle
to produce a sorted result.  It minimises the number of writes to the
array, making it useful when writes are expensive.

Reference: https://en.wikipedia.org/wiki/Cycle_sort

Complexity:
    Time:  O(n^2) best / O(n^2) average / O(n^2) worst
    Space: O(1)
"""

from __future__ import annotations


def cycle_sort(array: list[int]) -> list[int]:
    """Sort an array in ascending order using cycle sort.

    Args:
        array: List of integers to sort.

    Returns:
        A sorted list.

    Examples:
        >>> cycle_sort([3, 1, 2])
        [1, 2, 3]
    """
    length = len(array)

    for start in range(length - 1):
        item = array[start]

        # Count how many elements are smaller to find the correct position
        position = start
        for i in range(start + 1, length):
            if array[i] < item:
                position += 1

        # No cycle needed for this element
        if position == start:
            continue

        # Skip duplicates
        while item == array[position]:
            position += 1
        array[position], item = item, array[position]

        # Rotate the rest of the cycle
        while position != start:
            position = start
            for i in range(start + 1, length):
                if array[i] < item:
                    position += 1

            while item == array[position]:
                position += 1
            array[position], item = item, array[position]

    return array
