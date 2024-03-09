"""
Given a sorted integer array without duplicates,
return the summary of its ranges.

For example, given [0, 1, 2, 4, 5, 7], return [(0, 2), (4, 5), (7, 7)].
"""


from typing import List

def summarize_ranges(array: List[int]) -> List[str]:
    res = []
    if len(array) == 1:
        return [str(array[0])]
    it = iter(array)
    start = end = next(it)
    for num in it:
        if num - end == 1:
            end = num
        else:
            res.append((start, end) if start != end else (start,))
            start = end = num
    res.append((start, end) if start != end else (start,))
    return [f"{r[0]}-{r[1]}" if len(r) > 1 else str(r[0]) for r in res]

