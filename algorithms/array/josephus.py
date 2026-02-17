"""
Josephus Problem

People sit in a circular fashion; every k-th person is eliminated until
everyone has been removed. Yield the elimination order.

Reference: https://en.wikipedia.org/wiki/Josephus_problem

Complexity:
    Time:  O(n^2) due to list.pop at arbitrary index
    Space: O(1) auxiliary (yields in-place)
"""

from __future__ import annotations

from collections.abc import Generator
from typing import Any


def josephus(items: list[Any], skip: int) -> Generator[Any, None, None]:
    """Yield elements eliminated in Josephus-problem order.

    Args:
        items: List of participants arranged in a circle.
        skip: Every *skip*-th person is eliminated each round.

    Returns:
        A generator yielding eliminated elements in order.

    Examples:
        >>> list(josephus([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
        [3, 6, 9, 4, 8, 5, 2, 7, 1]
    """
    skip = skip - 1
    index = 0
    remaining = len(items)
    while remaining > 0:
        index = (skip + index) % remaining
        yield items.pop(index)
        remaining -= 1
