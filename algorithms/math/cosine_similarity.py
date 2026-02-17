"""
Cosine Similarity

Calculate the cosine similarity between two vectors, which measures the
cosine of the angle between them. Values range from -1 (opposite) to 1
(identical direction).

Reference: https://en.wikipedia.org/wiki/Cosine_similarity

Complexity:
    Time:  O(n)
    Space: O(1)
"""

from __future__ import annotations

import math


def _l2_distance(vec: list[float]) -> float:
    """Calculate the L2 (Euclidean) norm of a vector.

    Args:
        vec: Input vector as a list of numbers.

    Returns:
        The L2 norm of the vector.
    """
    norm = 0.0
    for element in vec:
        norm += element * element
    norm = math.sqrt(norm)
    return norm


def cosine_similarity(vec1: list[float], vec2: list[float]) -> float:
    """Calculate cosine similarity between two vectors.

    Args:
        vec1: First vector.
        vec2: Second vector (must be same length as vec1).

    Returns:
        Cosine similarity value between -1 and 1.

    Raises:
        ValueError: If vectors have different lengths.

    Examples:
        >>> cosine_similarity([1, 1, 1], [1, 2, -1])
        0.4714045207910317
    """
    if len(vec1) != len(vec2):
        raise ValueError(
            "The two vectors must be the same length. Got shape "
            + str(len(vec1))
            + " and "
            + str(len(vec2))
        )

    norm_a = _l2_distance(vec1)
    norm_b = _l2_distance(vec2)

    similarity = 0.0

    for vec1_element, vec2_element in zip(vec1, vec2, strict=False):
        similarity += vec1_element * vec2_element

    similarity /= norm_a * norm_b

    return similarity
