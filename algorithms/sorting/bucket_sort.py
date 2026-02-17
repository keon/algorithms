"""
Bucket Sort

Bucket sort distributes elements into a number of buckets, sorts each
bucket individually (here using insertion sort), and then concatenates
all buckets.

Reference: https://en.wikipedia.org/wiki/Bucket_sort

Complexity:
    Time:  O(n + k) best / O(n + k) average / O(n^2) worst
    Space: O(n + k)
"""

from __future__ import annotations


def bucket_sort(array: list[int]) -> list[int]:
    """Sort an array in ascending order using bucket sort.

    Args:
        array: List of non-negative integers to sort.

    Returns:
        A sorted list.

    Examples:
        >>> bucket_sort([3, 1, 2, 4])
        [1, 2, 3, 4]
    """
    num_buckets = len(array)
    buckets: list[list[int]] = [[] for _ in range(num_buckets)]

    max_value = max(array) + 1
    for value in array:
        index = value * num_buckets // max_value
        buckets[index].append(value)

    sorted_list: list[int] = []
    for bucket in buckets:
        sorted_list.extend(_insertion_sort(bucket))
    return sorted_list


def _insertion_sort(array: list[int]) -> list[int]:
    """Sort *array* in-place using insertion sort and return it."""
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array
