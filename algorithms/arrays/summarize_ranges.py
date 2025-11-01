"""
Given a sorted integer array without duplicates,
return the summary of its ranges.

For example, given [0, 1, 2, 4, 5, 7], return [(0, 2), (4, 5), (7, 7)].
"""

from typing import List, Tuple


def summarize_ranges(array: List[int]) -> List[Tuple[int, ...]]:
    res = []
    if len(array) == 0:
        return []
    if len(array) == 1:
        return [(array[0], array[0])]
    it = iter(array)
    start = end = next(it)
    for num in it:
        if num - end == 1:
            end = num
        else:
            res.append((start, end))
            start = end = num
    res.append((start, end))
    return res
