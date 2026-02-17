"""
Surface Area of a Torus

Calculate the surface area of a torus given its major and minor radii
using the formula A = 4 * pi^2 * R * r.

Reference: https://en.wikipedia.org/wiki/Torus

Complexity:
    Time:  O(1)
    Space: O(1)
"""

from __future__ import annotations

from math import pi


def surface_area_of_torus(major_radius: float, minor_radius: float) -> float:
    """Calculate the surface area of a torus.

    Args:
        major_radius: Distance from the center of the tube to the center
            of the torus (R).
        minor_radius: Radius of the tube (r).

    Returns:
        The surface area of the torus.

    Raises:
        ValueError: If either radius is negative.

    Examples:
        >>> surface_area_of_torus(3.0, 1.0)
        118.4352528130723
    """
    if major_radius < 0 or minor_radius < 0:
        raise ValueError("Radii must be non-negative")

    return 4 * pi**2 * major_radius * minor_radius
