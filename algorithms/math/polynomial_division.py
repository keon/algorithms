"""Polynomial long division.

Divide polynomial *dividend* by *divisor* and return (quotient, remainder).
Polynomials are represented as lists of coefficients from highest to lowest
degree.  E.g. [1, -3, 2] represents x^2 - 3x + 2.

Inspired by PR #840 (KTH-Software-Engineering-DD2480).
"""

from __future__ import annotations


def polynomial_division(
    dividend: list[float], divisor: list[float]
) -> tuple[list[float], list[float]]:
    """Perform polynomial long division.

    Returns (quotient_coefficients, remainder_coefficients).

    >>> polynomial_division([1, -3, 2], [1, -1])
    ([1.0, -2.0], [0.0])
    >>> polynomial_division([1, 0, -4], [1, -2])
    ([1.0, 2.0], [0.0])
    """
    if not divisor or all(c == 0 for c in divisor):
        msg = "Cannot divide by zero polynomial"
        raise ZeroDivisionError(msg)
    dividend = [float(c) for c in dividend]
    divisor = [float(c) for c in divisor]
    remainder = list(dividend)
    quotient: list[float] = []
    divisor_lead = divisor[0]
    len_diff = len(dividend) - len(divisor)
    for i in range(len_diff + 1):
        coeff = remainder[i] / divisor_lead
        quotient.append(coeff)
        for j in range(len(divisor)):
            remainder[i + j] -= coeff * divisor[j]
    # The remainder is the tail of the array
    remainder = remainder[len_diff + 1 :]
    if not remainder:
        remainder = [0.0]
    return quotient, remainder
