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
from collections.abc import Iterable


def _l2_distance(vec: Iterable[float]) -> float:
    """Calculate the L2 (Euclidean) norm of a vector.

    Args:
        vec: Input vector as an iterable of numbers.

    Returns:
        The L2 norm of the vector.
    """
    return math.sqrt(math.fsum(element * element for element in vec))


def cosine_similarity(vec1: list[float], vec2: list[float]) -> float:
    """Calculate cosine similarity between two vectors.

    Scale each vector before multiplying components to avoid overflow and
    underflow for very large or very small finite inputs.

    Args:
        vec1: First vector.
        vec2: Second vector (must be same length as vec1).

    Returns:
        Cosine similarity value between -1 and 1.

    Raises:
        ValueError: If vectors have different lengths.

    Examples:
        >>> round(cosine_similarity([1, 1, 1], [1, 2, -1]), 15)
        0.471404520791032
    """
    if len(vec1) != len(vec2):
        raise ValueError(
            "The two vectors must be the same length. Got shape "
            + str(len(vec1))
            + " and "
            + str(len(vec2))
        )

    scale_a = max((abs(element) for element in vec1), default=1.0)
    scale_b = max((abs(element) for element in vec2), default=1.0)
    norm_a = _l2_distance(element / scale_a for element in vec1)
    norm_b = _l2_distance(element / scale_b for element in vec2)
    similarity = math.fsum(
        (left / scale_a) * (right / scale_b)
        for left, right in zip(vec1, vec2, strict=False)
    )
    return similarity / (norm_a * norm_b)
