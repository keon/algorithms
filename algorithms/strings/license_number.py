"""
License Key Formatting

Given a license key string and a group size k, reformat the key so that each
group contains exactly k characters, separated by dashes.

Reference: https://leetcode.com/problems/license-key-formatting/

Complexity:
    Time:  O(n) where n is the length of the key
    Space: O(n)
"""

from __future__ import annotations


def license_number(key: str, group_size: int) -> str:
    """Reformat a license key string into groups of a given size.

    Args:
        key: The license key string with dashes.
        group_size: The desired size of each group.

    Returns:
        The reformatted license key with groups separated by dashes.

    Examples:
        >>> license_number("a-bc-dfd-df", 2)
        'ab-cd-fd-df'
    """
    result: list[str] = []
    alphanumeric: list[str] = []
    for char in key:
        if char != "-":
            alphanumeric.append(char)
    for index, char in enumerate(reversed(alphanumeric)):
        result.append(char)
        if (index + 1) % group_size == 0 and index != len(alphanumeric) - 1:
            result.append("-")
    return "".join(result[::-1])
