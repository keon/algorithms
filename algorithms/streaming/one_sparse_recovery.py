"""
Non-negative 1-Sparse Recovery

Determines whether a dynamic stream of (value, sign) tuples is 1-sparse,
meaning all values cancel out except for a single unique number. If so,
returns that number; otherwise returns None.

Reference: https://en.wikipedia.org/wiki/Sparse_recovery

Complexity:
    Time:  O(n * b) where n is stream length and b is bit width (32)
    Space: O(b)
"""

from __future__ import annotations


def one_sparse(array: list[tuple[int, str]]) -> int | None:
    """Recover the unique element from a 1-sparse stream.

    Args:
        array: A list of (value, sign) tuples where sign is '+' or '-'.

    Returns:
        The unique element if the stream is 1-sparse, otherwise None.

    Examples:
        >>> one_sparse([(4, '+'), (2, '+'), (2, '-'), (4, '+'), (3, '+'), (3, '-')])
        4
        >>> one_sparse([(2, '+'), (2, '+'), (2, '+'),
        ...            (2, '+'), (2, '+'), (2, '+'), (1, '+')])
    """
    sum_signs = 0
    bitsum: list[int] = [0] * 32
    sum_values = 0

    for val, sign in array:
        if sign == "+":
            sum_signs += 1
            sum_values += val
        else:
            sum_signs -= 1
            sum_values -= val
        _update_bit_sum(bitsum, val, sign)

    if sum_signs > 0 and _check_bit_sum_consistency(bitsum, sum_signs):
        return int(sum_values / sum_signs)
    return None


def _check_bit_sum_consistency(bitsum: list[int], sum_signs: int) -> bool:
    """Check that every entry is either 0 or equal to sum_signs.

    Args:
        bitsum: The accumulated bit sums.
        sum_signs: The expected non-zero value.

    Returns:
        True if the bitsum is consistent with a 1-sparse stream.
    """
    return all(val == 0 or val == sum_signs for val in bitsum)


def _update_bit_sum(bitsum: list[int], val: int, sign: str) -> None:
    """Add or subtract the bit representation of val to the bitsum array.

    Args:
        bitsum: The accumulated bit sums to update in place.
        val: The integer value whose bits to process.
        sign: '+' to add or '-' to subtract.
    """
    idx = 0
    if sign == "+":
        while val:
            bitsum[idx] += val & 1
            idx += 1
            val >>= 1
    else:
        while val:
            bitsum[idx] -= val & 1
            idx += 1
            val >>= 1
