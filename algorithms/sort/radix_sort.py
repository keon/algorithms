"""
Radix Sort

Radix sort processes digits from least significant to most significant,
distributing elements into buckets for each digit and collecting them
back in order.

Reference: https://en.wikipedia.org/wiki/Radix_sort

Complexity:
    Time:  O(n * k) best / O(n * k) average / O(n * k) worst
    Space: O(n + k)   where k is the number of digits in the largest value
"""

from __future__ import annotations


def radix_sort(array: list[int]) -> list[int]:
    """Sort an array of non-negative integers using radix sort.

    Args:
        array: List of non-negative integers to sort.

    Returns:
        A sorted list.

    Examples:
        >>> radix_sort([170, 45, 75, 90, 802, 24, 2, 66])
        [2, 24, 45, 66, 75, 90, 170, 802]
    """
    position = 1
    max_number = max(array)

    while position <= max_number:
        buckets: list[list[int]] = [[] for _ in range(10)]

        for num in array:
            digit = num // position % 10
            buckets[digit].append(num)

        index = 0
        for bucket in buckets:
            for num in bucket:
                array[index] = num
                index += 1

        position *= 10

    return array
