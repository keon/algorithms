"""
Return on Investment (ROI)

ROI measures the profitability of an investment relative to its cost,
expressed as a percentage.

Formula: ROI = (Gain - Cost) / Cost * 100

Reference: https://www.investopedia.com/terms/r/returnoninvestment.asp

Complexity:
    Time:  O(1)
    Space: O(1)
"""

from __future__ import annotations


def return_on_investment(
    gain_from_investment: float, cost_of_investment: float
) -> float:
    """
    Calculate return on investment as a percentage.

    Args:
        gain_from_investment: Total value gained from the investment.
        cost_of_investment: Total cost of the investment.

    Returns:
        ROI as a percentage.

    Raises:
        ValueError: If cost_of_investment is not positive.

    Examples:
        >>> return_on_investment(1000.0, 500.0)
        100.0
        >>> return_on_investment(500.0, 500.0)
        0.0
        >>> return_on_investment(200.0, 500.0)
        -60.0
        >>> return_on_investment(0.0, 500.0)
        -100.0
        >>> return_on_investment(1000.0, 0.0)
        Traceback (most recent call last):
            ...
        ValueError: cost_of_investment must be greater than 0
    """
    if cost_of_investment <= 0:
        raise ValueError("cost_of_investment must be greater than 0")
    return round(
        (gain_from_investment - cost_of_investment) / cost_of_investment * 100, 2
    )
