import math



def _l2_distance(vec):
    """
    Calculate the L2 distance(Euclidean distance) from two given vectors.
    """
    norm = 0.
    for e in vec:
        norm += e * e
    norm = math.sqrt(norm)
    return norm


def cosine_similarity(a, b):
    if len(a) != len(b):
        raise ValueError("The two vectors must be the same length. Got " + str(len(a)) +  " and " + str(len(b)))
    
    norm_a = _l2_distance(a)
    norm_b = _l2_distance(b)

    similarity = 0.

    # Calculate the dot product of two normalized vectors
    for ae, be in zip(a, b):
        similarity += ae * be
    
    similarity /= (norm_a * norm_b)

    return similarity
