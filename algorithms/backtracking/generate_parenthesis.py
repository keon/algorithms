"""
Generate Parentheses

Given n pairs of parentheses, generate all combinations of well-formed
parentheses.

Reference: https://leetcode.com/problems/generate-parentheses/

Complexity:
    Time:  O(4^n / sqrt(n)) — the n-th Catalan number
    Space: O(n) recursion depth
"""

from __future__ import annotations


def generate_parenthesis_v1(count: int) -> list[str]:
    """Generate all valid parenthesis combinations (right-first variant).

    Builds combinations by tracking remaining left and right parentheses,
    trying to add a closing paren before an opening one.

    Args:
        count: The number of parenthesis pairs.

    Returns:
        A list of all valid parenthesis strings.

    Examples:
        >>> generate_parenthesis_v1(2)
        ['()()', '(())']
    """
    result: list[str] = []
    _add_pair_v1(result, "", count, 0)
    return result


def _add_pair_v1(
    result: list[str],
    current: str,
    left: int,
    right: int,
) -> None:
    """Recursive helper for v1: tries closing before opening."""
    if left == 0 and right == 0:
        result.append(current)
        return
    if right > 0:
        _add_pair_v1(result, current + ")", left, right - 1)
    if left > 0:
        _add_pair_v1(result, current + "(", left - 1, right + 1)


def generate_parenthesis_v2(count: int) -> list[str]:
    """Generate all valid parenthesis combinations (left-first variant).

    Builds combinations by tracking remaining left and right parentheses,
    trying to add an opening paren before a closing one.

    Args:
        count: The number of parenthesis pairs.

    Returns:
        A list of all valid parenthesis strings.

    Examples:
        >>> generate_parenthesis_v2(2)
        ['(())', '()()']
    """
    result: list[str] = []
    _add_pair_v2(result, "", count, count)
    return result


def _add_pair_v2(
    result: list[str],
    current: str,
    left: int,
    right: int,
) -> None:
    """Recursive helper for v2: tries opening before closing."""
    if left == 0 and right == 0:
        result.append(current)
    if left > 0:
        _add_pair_v2(result, current + "(", left - 1, right)
    if right > 0 and left < right:
        _add_pair_v2(result, current + ")", left, right - 1)
