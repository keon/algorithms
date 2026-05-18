"""Geometric mean — the nth root of the product of n numbers.

The geometric mean is useful for data that grows exponentially
(like investment returns, population growth, etc.) and for
finding the central tendency when dealing with ratios or rates.

Formula: GM = (x₁ × x₂ × ... × xₙ)^(1/n)
"""

from __future__ import annotations

import math


def geometric_mean(numbers: list[float]) -> float:
    """Return the geometric mean of a list of numbers.

    The geometric mean is the nth root of the product of n numbers.
    All numbers must be positive.

    Args:
        numbers: A list of positive numbers

    Returns:
        The geometric mean as a float

    Raises:
        ValueError: If the list is empty, has fewer than 1 element,
                   or contains non-positive numbers

    >>> round(geometric_mean([1, 2, 3, 4, 5]), 4)
    2.6052
    >>> round(geometric_mean([2, 8]), 4)
    4.0
    >>> round(geometric_mean([1, 1, 1]), 4)
    1.0
    >>> round(geometric_mean([100, 100, 100]), 4)
    100.0
    """
    if not numbers:
        msg = "List cannot be empty"
        raise ValueError(msg)

    if any(num <= 0 for num in numbers):
        msg = "All numbers must be positive"
        raise ValueError(msg)

    n = len(numbers)
    product = 1.0
    for num in numbers:
        product *= num

    return product ** (1 / n)


def geometric_mean_logarithm(numbers: list[float]) -> float:
    """Return the geometric mean using logarithms (more numerically stable).

    This method avoids overflow/underflow for very large or very small numbers
    by using the property: GM = exp((ln(x₁) + ln(x₂) + ... + ln(xₙ)) / n)

    Args:
        numbers: A list of positive numbers

    Returns:
        The geometric mean as a float

    Raises:
        ValueError: If the list is empty or contains non-positive numbers

    >>> round(geometric_mean_logarithm([2, 8]), 4)
    4.0
    >>> round(geometric_mean_logarithm([1, 2, 3, 4, 5]), 4)
    2.6052
    """
    if not numbers:
        msg = "List cannot be empty"
        raise ValueError(msg)

    if any(num <= 0 for num in numbers):
        msg = "All numbers must be positive"
        raise ValueError(msg)

    log_sum = sum(math.log(num) for num in numbers)
    return math.exp(log_sum / len(numbers))
