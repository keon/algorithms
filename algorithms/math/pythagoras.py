"""
Pythagorean Theorem

Given the lengths of two sides of a right-angled triangle, compute the
length of the third side using the Pythagorean theorem.

Reference: https://en.wikipedia.org/wiki/Pythagorean_theorem

Complexity:
    Time:  O(1)
    Space: O(1)
"""

from __future__ import annotations


def pythagoras(
    opposite: float | str, adjacent: float | str, hypotenuse: float | str
) -> str:
    """Compute the unknown side of a right triangle.

    Pass "?" as the unknown side to calculate it from the other two.

    Args:
        opposite: Length of the opposite side, or "?" if unknown.
        adjacent: Length of the adjacent side, or "?" if unknown.
        hypotenuse: Length of the hypotenuse, or "?" if unknown.

    Returns:
        A string describing the computed side and its value.

    Raises:
        ValueError: If the arguments are invalid.

    Examples:
        >>> pythagoras(3, 4, "?")
        'Hypotenuse = 5.0'
    """
    try:
        if opposite == "?":
            return "Opposite = " + str(((hypotenuse**2) - (adjacent**2)) ** 0.5)
        if adjacent == "?":
            return "Adjacent = " + str(((hypotenuse**2) - (opposite**2)) ** 0.5)
        if hypotenuse == "?":
            return "Hypotenuse = " + str(((opposite**2) + (adjacent**2)) ** 0.5)
        return "You already know the answer!"
    except Exception as err:
        raise ValueError("invalid argument(s) were given.") from err
