"""
Expression Add Operators

Given a string of digits and a target value, return all possibilities to
insert binary operators (+, -, *) between the digits so they evaluate to
the target value.

Reference: https://leetcode.com/problems/expression-add-operators/

Complexity:
    Time:  O(4^n) worst
    Space: O(n) recursion depth
"""

from __future__ import annotations


def add_operators(digits: str, target: int) -> list[str]:
    """Return all expressions formed by inserting +, -, * that equal target.

    Args:
        digits: A string containing only digits 0-9.
        target: The target integer value.

    Returns:
        A list of valid expression strings.

    Examples:
        >>> add_operators("123", 6)
        ['1+2+3', '1*2*3']
    """
    result: list[str] = []
    if not digits:
        return result
    _dfs(result, "", digits, target, 0, 0, 0)
    return result


def _dfs(
    result: list[str],
    path: str,
    digits: str,
    target: int,
    position: int,
    evaluated: int,
    multed: int,
) -> None:
    """Depth-first search helper that builds expressions recursively."""
    if position == len(digits):
        if target == evaluated:
            result.append(path)
        return
    for i in range(position, len(digits)):
        if i != position and digits[position] == "0":
            break
        current = int(digits[position : i + 1])
        if position == 0:
            _dfs(result, path + str(current), digits, target,
                 i + 1, current, current)
        else:
            _dfs(result, path + "+" + str(current), digits, target,
                 i + 1, evaluated + current, current)
            _dfs(result, path + "-" + str(current), digits, target,
                 i + 1, evaluated - current, -current)
            _dfs(result, path + "*" + str(current), digits, target,
                 i + 1, evaluated - multed + multed * current,
                 multed * current)
