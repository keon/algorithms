"""
Generate Strobogrammatic Numbers

A strobogrammatic number looks the same when rotated 180 degrees. Generate
all strobogrammatic numbers of a given length or count them within a range.

Reference: https://en.wikipedia.org/wiki/Strobogrammatic_number

Complexity:
    Time:  O(5^(n/2)) for generation
    Space: O(5^(n/2))
"""

from __future__ import annotations


def gen_strobogrammatic(n: int) -> list[str]:
    """Generate all strobogrammatic numbers of length n.

    Args:
        n: The desired length of strobogrammatic numbers.

    Returns:
        List of strobogrammatic number strings.

    Examples:
        >>> gen_strobogrammatic(2)
        ['88', '11', '96', '69']
    """
    return _helper(n, n)


def _helper(n: int, length: int) -> list[str]:
    """Recursively build strobogrammatic numbers of length n.

    Args:
        n: Remaining length to fill.
        length: Original target length.

    Returns:
        List of strobogrammatic number strings.
    """
    if n == 0:
        return [""]
    if n == 1:
        return ["1", "0", "8"]
    middles = _helper(n - 2, length)
    result = []
    for middle in middles:
        if n != length:
            result.append("0" + middle + "0")
        result.append("8" + middle + "8")
        result.append("1" + middle + "1")
        result.append("9" + middle + "6")
        result.append("6" + middle + "9")
    return result


def strobogrammatic_in_range(low: str, high: str) -> int:
    """Count strobogrammatic numbers within the given range [low, high].

    Args:
        low: Lower bound as a string.
        high: Upper bound as a string.

    Returns:
        Count of strobogrammatic numbers in the range.

    Examples:
        >>> strobogrammatic_in_range("10", "100")
        4
    """
    res: list[str] = []
    count = 0
    low_len = len(low)
    high_len = len(high)
    for i in range(low_len, high_len + 1):
        res.extend(_helper2(i, i))
    for perm in res:
        if len(perm) == low_len and int(perm) < int(low):
            continue
        if len(perm) == high_len and int(perm) > int(high):
            continue
        count += 1
    return count


def _helper2(n: int, length: int) -> list[str]:
    """Recursively build strobogrammatic numbers including leading zeros.

    Args:
        n: Remaining length to fill.
        length: Original target length.

    Returns:
        List of strobogrammatic number strings.
    """
    if n == 0:
        return [""]
    if n == 1:
        return ["0", "8", "1"]
    mids = _helper(n - 2, length)
    res = []
    for mid in mids:
        if n != length:
            res.append("0" + mid + "0")
        res.append("1" + mid + "1")
        res.append("6" + mid + "9")
        res.append("9" + mid + "6")
        res.append("8" + mid + "8")
    return res
