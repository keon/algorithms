"""
Flatten Arrays

Given an array that may contain nested arrays, produce a single
flat resultant array.

Reference: https://en.wikipedia.org/wiki/Flatten_(higher-order_function)

Complexity:
    Time:  O(n) where n is the total number of elements
    Space: O(n)
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any, Generator


def flatten(input_arr: Iterable[Any], output_arr: list[Any] | None = None) -> list[Any]:
    """Recursively flatten a nested iterable into a single list.

    Args:
        input_arr: A potentially nested iterable to flatten.
        output_arr: Accumulator list for recursive calls (internal use).

    Returns:
        A flat list containing all leaf elements.

    Examples:
        >>> flatten([2, 1, [3, [4, 5], 6], 7, [8]])
        [2, 1, 3, 4, 5, 6, 7, 8]
    """
    if output_arr is None:
        output_arr = []
    for element in input_arr:
        if not isinstance(element, str) and isinstance(element, Iterable):
            flatten(element, output_arr)
        else:
            output_arr.append(element)
    return output_arr


def flatten_iter(iterable: Iterable[Any]) -> Generator[Any, None, None]:
    """Lazily flatten a nested iterable, yielding one element at a time.

    Args:
        iterable: A potentially nested iterable to flatten.

    Returns:
        A generator producing one-dimensional output.

    Examples:
        >>> list(flatten_iter([2, 1, [3, [4, 5], 6], 7, [8]]))
        [2, 1, 3, 4, 5, 6, 7, 8]
    """
    for element in iterable:
        if not isinstance(element, str) and isinstance(element, Iterable):
            yield from flatten_iter(element)
        else:
            yield element
