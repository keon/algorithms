"""
Pigeonhole Sort

Pigeonhole sort is suitable for sorting lists where the number of
elements and the range of possible key values are approximately equal.

Reference: https://en.wikipedia.org/wiki/Pigeonhole_sort

Complexity:
    Time:  O(n + range) best / O(n + range) average / O(n + range) worst
    Space: O(range)
"""

from __future__ import annotations


def pigeonhole_sort(array: list[int]) -> list[int]:
    """Sort an array in ascending order using pigeonhole sort.

    Args:
        array: List of integers to sort.

    Returns:
        A sorted list.

    Examples:
        >>> pigeonhole_sort([3, 1, 2])
        [1, 2, 3]
    """
    max_value = max(array)
    min_value = min(array)
    size = max_value - min_value + 1

    holes = [0] * size
    for value in array:
        holes[value - min_value] += 1

    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            array[i] = count + min_value
            i += 1
    return array
