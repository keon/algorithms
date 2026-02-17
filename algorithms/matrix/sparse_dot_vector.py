"""
Sparse Dot Vector

Compute the dot product of two large sparse vectors efficiently by
converting them to index-value pair representations and merging.

Reference: https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

Complexity:
    Time:  O(n) for conversion, O(k) for dot product where k = non-zero count
    Space: O(k)
"""

from __future__ import annotations


def vector_to_index_value_list(
    vector: list[float],
) -> list[tuple[int, float]]:
    """Convert a dense vector to a sparse index-value list.

    Args:
        vector: Dense vector of floats.

    Returns:
        List of (index, value) tuples for non-zero elements.

    Examples:
        >>> vector_to_index_value_list([0.0, 2.0, 0.0, 3.0])
        [(1, 2.0), (3, 3.0)]
    """
    return [(i, v) for i, v in enumerate(vector) if v != 0.0]


def dot_product(
    iv_list1: list[tuple[int, float]],
    iv_list2: list[tuple[int, float]],
) -> float:
    """Compute the dot product of two sparse index-value lists.

    Args:
        iv_list1: First sparse vector as index-value pairs.
        iv_list2: Second sparse vector as index-value pairs.

    Returns:
        Dot product of the two vectors.

    Examples:
        >>> dot_product([(0, 1.0), (1, 2.0), (2, 3.0)], [(1, 2.0), (2, 2.0)])
        10.0
    """
    product = 0
    p1 = len(iv_list1) - 1
    p2 = len(iv_list2) - 1

    while p1 >= 0 and p2 >= 0:
        i1, v1 = iv_list1[p1]
        i2, v2 = iv_list2[p2]

        if i1 < i2:
            p1 -= 1
        elif i2 < i1:
            p2 -= 1
        else:
            product += v1 * v2
            p1 -= 1
            p2 -= 1

    return product
