"""
Next Greatest Letter

Given a sorted list of lowercase letters and a target letter, find the
smallest letter in the list that is larger than the target. Letters wrap
around, so if the target is greater than or equal to the last letter the
answer is the first letter.

Reference: https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

Complexity:
    next_greatest_letter        -- O(log n) time, O(1) space  (bisect)
    next_greatest_letter_v1     -- O(log n) time, O(1) space  (manual binary search)
    next_greatest_letter_v2     -- O(n) time, O(1) space      (brute force)
"""

from __future__ import annotations

import bisect


def next_greatest_letter(letters: list[str], target: str) -> str:
    """Find the smallest letter greater than *target* using ``bisect``.

    Args:
        letters: Sorted list of lowercase letters.
        target: The letter to exceed.

    Returns:
        The smallest letter in *letters* that is strictly greater than
        *target*, wrapping around if necessary.

    Examples:
        >>> next_greatest_letter(["c", "f", "j"], "a")
        'c'
        >>> next_greatest_letter(["c", "f", "j"], "c")
        'f'
    """
    index = bisect.bisect(letters, target)
    return letters[index % len(letters)]


def next_greatest_letter_v1(letters: list[str], target: str) -> str:
    """Find the smallest letter greater than *target* using binary search.

    Args:
        letters: Sorted list of lowercase letters.
        target: The letter to exceed.

    Returns:
        The smallest letter in *letters* that is strictly greater than
        *target*, wrapping around if necessary.

    Examples:
        >>> next_greatest_letter_v1(["c", "f", "j"], "d")
        'f'
    """
    if letters[0] > target:
        return letters[0]
    if letters[len(letters) - 1] <= target:
        return letters[0]
    left, right = 0, len(letters) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if letters[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return letters[left]


def next_greatest_letter_v2(letters: list[str], target: str) -> str:
    """Find the smallest letter greater than *target* using brute force.

    Args:
        letters: Sorted list of lowercase letters.
        target: The letter to exceed.

    Returns:
        The smallest letter in *letters* that is strictly greater than
        *target*, wrapping around if necessary.

    Examples:
        >>> next_greatest_letter_v2(["c", "f", "j"], "d")
        'f'
    """
    for letter in letters:
        if letter > target:
            return letter
    return letters[0]
