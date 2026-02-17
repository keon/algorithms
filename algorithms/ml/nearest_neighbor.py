"""
Nearest Neighbor Classifier

Classifies a query vector by finding the closest vector in a training set
(using Euclidean distance) and returning its label.

Reference: https://en.wikipedia.org/wiki/Nearest_neighbour_algorithm

Complexity:
    Time:  O(n * d) where n is training set size and d is dimensionality
    Space: O(1)
"""

from __future__ import annotations

import math


def distance(x: tuple[float, ...], y: tuple[float, ...]) -> float:
    """Compute the Euclidean distance between two vectors.

    Args:
        x: First vector.
        y: Second vector.

    Returns:
        The Euclidean distance.

    Raises:
        AssertionError: If the vectors have different lengths.
    """
    assert len(x) == len(y), "The vectors must have same length"
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(x, y)))


def nearest_neighbor(
    x: tuple[float, ...],
    training_set: dict[tuple[float, ...], int],
) -> int:
    """Classify a vector using the nearest neighbor algorithm.

    Args:
        x: The query vector.
        training_set: A dict mapping training vectors to their labels.

    Returns:
        The label of the nearest training vector.

    Examples:
        >>> nearest_neighbor((0, 0), {(1, 1): 1, (0, 0.5): 0})
        0
    """
    assert isinstance(x, tuple) and isinstance(training_set, dict)
    closest_key: tuple[float, ...] = ()
    min_dist = float("inf")
    for key in training_set:
        dist = distance(x, key)
        if dist < min_dist:
            min_dist = dist
            closest_key = key
    return training_set[closest_key]
