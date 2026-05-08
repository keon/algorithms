def chebyshev_distance(point1, point2):
    """
    Calculate the Chebyshev distance between two points.

    The Chebyshev distance is defined as the maximum absolute difference
    between the coordinates of the points.

    Parameters:
    point1 (list or tuple): The first point as a list or tuple of coordinates.
    point2 (list or tuple): The second point as a list or tuple of coordinates.

    Returns:
    float: The Chebyshev distance between the two points.
    """
    if len(point1) != len(point2):
        raise ValueError("Points must have the same number of dimensions.")
    
    return max(abs(a - b) for a, b in zip(point1, point2))
