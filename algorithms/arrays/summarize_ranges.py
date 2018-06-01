"""
Given a sorted integer array without duplicates,
return the summary of its ranges.

For example, given [0, 1, 2, 4, 5, 7], return [(0, 2), (4, 5), (7, 7)].
"""


def summarize_ranges(array):
    """
    :type array: List[int]
    :rtype: List[]
    """
    res = []
    if len(array) == 1:
        return [str(array[0])]
    i = 0
    while i < len(array):
        num = array[i]
        while i + 1 < len(array) and array[i + 1] - array[i] == 1:
            i += 1
        if array[i] != num:
            res.append((num, array[i]))
        else:
            res.append((num, num))
        i += 1
    return res
