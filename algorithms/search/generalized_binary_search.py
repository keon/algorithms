"""
Generalized Binary Search

This module provides a generalized binary search implementation that
operates over a numeric range using a monotonic boolean predicate.

Instead of searching for a specific value in an array, this version
returns the smallest value in a given range for which the predicate
function evaluates to True.

This abstraction allows the same binary search logic to be reused
across multiple problem domains.
"""

from typing import Callable, Optional


def binary_search_first_true(
    low: int,
    high: int,
    predicate: Callable[[int], bool]
) -> Optional[int]:
    """
    Finds the smallest value x in the range [low, high] such that
    predicate(x) returns True.

    Assumptions:
        The predicate function must be monotonic:
        False False False True True True

    Time Complexity:
        O(log N)

    Space Complexity:
        O(1)

    Args:
        low (int): Lower bound of the search range (inclusive)
        high (int): Upper bound of the search range (inclusive)
        predicate (Callable[[int], bool]): A monotonic boolean function

    Returns:
        Optional[int]: The smallest x for which predicate(x) is True,
                       or None if no such value exists in the range.
    """

    result = None

    while low <= high:
        mid = low + (high - low) // 2

        if predicate(mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result


# -----------------------------
# Example Use Cases
# -----------------------------

if __name__ == "__main__":
    # Example 1: Find smallest x such that x >= 7
    print(binary_search_first_true(0, 10, lambda x: x >= 7))  # Output: 7

    # Example 2: Find smallest x such that x^2 >= 25
    print(binary_search_first_true(0, 10, lambda x: x * x >= 25))  # Output: 5

    # Example 3: No value satisfies the predicate
    print(binary_search_first_true(0, 5, lambda x: x > 10))  # Output: None
