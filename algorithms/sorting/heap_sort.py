"""
Heap Sort

Heap sort builds a heap from the data and repeatedly extracts the
extreme element to produce a sorted array.  Two variants are provided:
max-heap sort and min-heap sort.

Reference: https://en.wikipedia.org/wiki/Heapsort

Complexity:
    Time:  O(n log n) best / O(n log n) average / O(n log n) worst
    Space: O(1)
"""

from __future__ import annotations


def max_heap_sort(array: list[int]) -> list[int]:
    """Sort an array in ascending order using a max-heap.

    Args:
        array: List of integers to sort.

    Returns:
        A sorted list.

    Examples:
        >>> max_heap_sort([3, 1, 2])
        [1, 2, 3]
    """
    for i in range(len(array) - 1, 0, -1):
        _max_heapify(array, i)
    return array


def _max_heapify(array: list[int], end: int) -> None:
    """Build a max-heap on *array[0..end]* and swap the root to *end*."""
    last_parent = (end - 1) // 2

    for parent in range(last_parent, -1, -1):
        current = parent
        while current <= last_parent:
            child = 2 * current + 1
            if child + 1 <= end and array[child] < array[child + 1]:
                child += 1
            if array[child] > array[current]:
                array[current], array[child] = array[child], array[current]
                current = child
            else:
                break

    array[0], array[end] = array[end], array[0]


def min_heap_sort(array: list[int]) -> list[int]:
    """Sort an array in ascending order using a min-heap.

    Args:
        array: List of integers to sort.

    Returns:
        A sorted list.

    Examples:
        >>> min_heap_sort([3, 1, 2])
        [1, 2, 3]
    """
    for i in range(len(array) - 1):
        _min_heapify(array, i)
    return array


def _min_heapify(array: list[int], start: int) -> None:
    """Build a min-heap on *array[start..]* and place the minimum at *start*."""
    end = len(array) - 1
    last_parent = (end - start - 1) // 2

    for parent in range(last_parent, -1, -1):
        current = parent
        while current <= last_parent:
            child = 2 * current + 1
            if (
                child + 1 <= end - start
                and array[child + start] > array[child + 1 + start]
            ):
                child += 1
            if array[child + start] < array[current + start]:
                array[current + start], array[child + start] = (
                    array[child + start],
                    array[current + start],
                )
                current = child
            else:
                break
