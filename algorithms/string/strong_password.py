"""
Strong Password Checker

Given a password string, determine the minimum number of characters that
must be added to make it strong. A strong password has at least 6 characters,
a digit, a lowercase letter, an uppercase letter, and a special character.

Reference: https://www.hackerrank.com/challenges/strong-password/problem

Complexity:
    Time:  O(n) where n is the length of the password
    Space: O(1)
"""

from __future__ import annotations


def strong_password(length: int, password: str) -> int:
    """Calculate minimum characters to add for a strong password.

    Args:
        length: The current length of the password.
        password: The password string to evaluate.

    Returns:
        The minimum number of characters to add.

    Examples:
        >>> strong_password(3, "Ab1")
        3
    """
    missing_types = 0
    if not any(char.isdigit() for char in password):
        missing_types += 1
    if not any(char.islower() for char in password):
        missing_types += 1
    if not any(char.isupper() for char in password):
        missing_types += 1
    if not any(char in "!@#$%^&*()-+" for char in password):
        missing_types += 1
    return max(missing_types, 6 - length)
