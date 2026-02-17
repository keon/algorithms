"""
Reverse String

Reverse a string using four different approaches: recursive, iterative,
pythonic (using reversed), and ultra-pythonic (using slicing).

Reference: https://en.wikipedia.org/wiki/String_(computer_science)#Reversal

Complexity:
    Time:  O(n) for all approaches
    Space: O(n) for all approaches, O(log n) stack for recursive
"""

from __future__ import annotations


def recursive(text: str) -> str:
    """Reverse a string using a recursive divide-and-conquer approach.

    Args:
        text: The string to reverse.

    Returns:
        The reversed string.

    Examples:
        >>> recursive("hello there")
        'ereht olleh'
    """
    length = len(text)
    if length < 2:
        return text
    return recursive(text[length // 2:]) + recursive(text[:length // 2])


def iterative(text: str) -> str:
    """Reverse a string using iterative character swapping.

    Args:
        text: The string to reverse.

    Returns:
        The reversed string.

    Examples:
        >>> iterative("hello there")
        'ereht olleh'
    """
    characters = list(text)
    left, right = 0, len(text) - 1
    while left < right:
        characters[left], characters[right] = (
            characters[right],
            characters[left],
        )
        left += 1
        right -= 1
    return "".join(characters)


def pythonic(text: str) -> str:
    """Reverse a string using the built-in reversed function.

    Args:
        text: The string to reverse.

    Returns:
        The reversed string.

    Examples:
        >>> pythonic("hello there")
        'ereht olleh'
    """
    characters = list(reversed(text))
    return "".join(characters)


def ultra_pythonic(text: str) -> str:
    """Reverse a string using slice notation.

    Args:
        text: The string to reverse.

    Returns:
        The reversed string.

    Examples:
        >>> ultra_pythonic("hello there")
        'ereht olleh'
    """
    return text[::-1]
