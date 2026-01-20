"""
Surface Area of a Torus

Reference:
https://en.wikipedia.org/wiki/Torus
"""

from math import pi


def surface_area_of_torus(major_radius: float, minor_radius: float) -> float:
    """
    Calculate the surface area of a torus.

    Formula:
        A = 4 * π² * R * r

    :param major_radius: Distance from the center of the tube to the center of the torus (R)
    :param minor_radius: Radius of the tube (r)
    :return: Surface area of the torus

    >>> surface_area_of_torus(3.0, 1.0)
    118.4352528130723
    >>> surface_area_of_torus(5.0, 2.0)
    789.5683520871487
    """
    if major_radius < 0 or minor_radius < 0:
        raise ValueError("Radii must be non-negative")

    return 4 * pi**2 * major_radius * minor_radius
