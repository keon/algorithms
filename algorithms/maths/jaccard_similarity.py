"""
Calculate jaccard similarity between given two 1d list(or set).

Example:
jaccard_similarity([1, 1, 1], [1, 2, -1])  # output : 0.3333333333333333
"""


def jaccard_similarity(a, b):
    """
    Calculate jaccard similarity between given two vectors(or sets)
    :type a: list or set
    :type b: list or set
    """

    a, b = set(a), set(b)
    similarity =  len(a & b) / len(a.union(b))
    return similarity
