"""
Calculate cosine similarity between given two 1d list.
Two list must have the same length.

Example:
cosine_similarity([1, 1, 1], [1, 2, -1])  # output : 0.47140452079103173
"""
import math


def _l2_distance(vec):
    """
    Calculate l2 distance from two given vectors.
    """
    norm = 0.
    for e in vec:
        norm += e * e
    norm = math.sqrt(norm)
    return norm


def cosine_similarity(a, b):
    """
    Calculate cosine similarity between given two vectors
    :type a: list
    :type b: list
    """
    if len(a) != len(b):
        raise ValueError("The two vectors must be the same length. Got shape " + str(len(a)) + " and " + str(len(b)))

    norm_a = _l2_distance(a)
    norm_b = _l2_distance(b)

    similarity = 0.

    # Calculate the dot product of two vectors
    for ae, be in zip(a, b):
        similarity += ae * be

    similarity /= (norm_a * norm_b)

    return similarity
