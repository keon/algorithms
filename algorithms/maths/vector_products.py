def dot_product(vec1, vec2):
    """
    Calculates the dot product of two vectors.
    The vectors, vec1 and vec2 have to be passed as lists containing the direction ratios of each vectors.
    """
    dot_product = []
    for ratio in range(0, 3):
        dot_product.append(vec1[ratio] * vec2[ratio])
    return dot_product

def cross_product(vec1, vec2):
    """
    Calculates the dot product of two vectors.
    The vectors, vec1 and vec2 have to be passed as lists containing the direction ratios of each vectors.
    """
    cross_product = [
        (vec1[1] * vec2[2]) - (vec1[2] * vec2[1]),
        -((vec1[0] * vec2[2]) - (vec1[2] * vec2[0])),
        (vec1[0] * vec2[1]) - (vec1[1] * vec2[0])
    ]
    return cross_product


def magnitude(vec):
    """
    Calculates the magnitude of the given vector.
    The vector, vec have to be passed as list containing the direction ratio of the vector.
    """
    magnitude = ((vec[0] * vec[0]) + (vec[1] * vec[1]) + (vec[2] * vec[2])) ** 0.5
    return magnitude
