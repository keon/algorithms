"""Simple linear regression — fit a line to (x, y) data.

Computes the ordinary least-squares regression line y = mx + b
without external libraries.

Inspired by PR #871 (MakanFar).
"""

from __future__ import annotations

import math


def linear_regression(x: list[float], y: list[float]) -> tuple[float, float]:
    """Return (slope, intercept) for the best-fit line.

    Center observations before computing sums of products to avoid cancellation
    when x or y have a large common offset.

    >>> m, b = linear_regression([1, 2, 3, 4, 5], [2, 4, 5, 4, 5])
    >>> round(m, 4)
    0.6
    >>> round(b, 4)
    2.2
    """
    n = len(x)
    if n != len(y) or n < 2:
        msg = "x and y must have at least 2 equal-length elements"
        raise ValueError(msg)
    x_mean = math.fsum(x) / n
    y_mean = math.fsum(y) / n
    denom = math.fsum((xi - x_mean) ** 2 for xi in x)
    if denom == 0:
        msg = "Vertical line — slope is undefined"
        raise ValueError(msg)
    numerator = math.fsum(
        (xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y, strict=False)
    )
    slope = numerator / denom
    intercept = y_mean - slope * x_mean
    return slope, intercept


def r_squared(x: list[float], y: list[float]) -> float:
    """Return the R-squared (coefficient of determination) for the fit."""
    slope, intercept = linear_regression(x, y)
    y_mean = sum(y) / len(y)
    ss_tot = sum((yi - y_mean) ** 2 for yi in y)
    ss_res = sum(
        (yi - (slope * xi + intercept)) ** 2 for xi, yi in zip(x, y, strict=False)
    )
    if ss_tot == 0:
        return 1.0
    return 1.0 - ss_res / ss_tot


def rmse(x: list[float], y: list[float]) -> float:
    """Return the root mean squared error for the fit."""
    slope, intercept = linear_regression(x, y)
    n = len(y)
    return math.sqrt(
        sum((yi - (slope * xi + intercept)) ** 2 for xi, yi in zip(x, y, strict=False))
        / n
    )
