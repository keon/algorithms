"""
Validate Coordinates

Validate if given parameters are valid geographical coordinates.
Latitude must be between -90 and 90, longitude between -180 and 180.

Reference: https://en.wikipedia.org/wiki/Geographic_coordinate_system

Complexity:
    Time:  O(n) where n is the length of the coordinate string
    Space: O(1)
"""

from __future__ import annotations

import re


def is_valid_coordinates_0(coordinates: str) -> bool:
    """Validate coordinates by character checking and parsing.

    Args:
        coordinates: A string of the form "lat, lng".

    Returns:
        True if the coordinates are valid, False otherwise.

    Examples:
        >>> is_valid_coordinates_0("-23, 25")
        True
    """
    for char in coordinates:
        if not (char.isdigit() or char in ['-', '.', ',', ' ']):
            return False
    parts = coordinates.split(", ")
    if len(parts) != 2:
        return False
    try:
        latitude = float(parts[0])
        longitude = float(parts[1])
    except ValueError:
        return False
    return -90 <= latitude <= 90 and -180 <= longitude <= 180


def is_valid_coordinates_1(coordinates: str) -> bool:
    """Validate coordinates by splitting and converting to floats.

    Args:
        coordinates: A string of the form "lat, lng".

    Returns:
        True if the coordinates are valid, False otherwise.

    Examples:
        >>> is_valid_coordinates_1("43.91343345, 143")
        True
    """
    try:
        latitude, longitude = [
            abs(float(part))
            for part in coordinates.split(',')
            if 'e' not in part
        ]
    except ValueError:
        return False
    return latitude <= 90 and longitude <= 180


def is_valid_coordinates_regular_expression(coordinates: str) -> bool:
    """Validate coordinates using a regular expression.

    Args:
        coordinates: A string of the form "lat, lng".

    Returns:
        True if the coordinates are valid, False otherwise.

    Examples:
        >>> is_valid_coordinates_regular_expression("4, -3")
        True
    """
    return bool(
        re.match(
            r"-?(\d|[1-8]\d|90)\.?\d*, -?(\d|[1-9]\d|1[0-7]\d|180)\.?\d*$",
            coordinates,
        )
    )
