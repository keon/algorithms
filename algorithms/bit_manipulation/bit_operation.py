"""
Fundamental Bit Operations

Basic bit manipulation operations: get, set, clear, and update individual
bits at a specific position in an integer.

Reference: https://en.wikipedia.org/wiki/Bit_manipulation

Complexity:
    Time:  O(1) for all operations
    Space: O(1)
"""

from __future__ import annotations


def get_bit(number: int, position: int) -> int:
    """Get the bit value at a specific position.

    Shifts 1 over by *position* bits and ANDs with *number* to isolate
    the target bit.

    Args:
        number: The integer to inspect.
        position: Zero-based bit index (0 is the least significant bit).

    Returns:
        1 if the bit at *position* is set, 0 otherwise.

    Examples:
        >>> get_bit(22, 2)
        1
        >>> get_bit(22, 3)
        0
    """
    return (number & (1 << position)) != 0


def set_bit(number: int, position: int) -> int:
    """Set the bit at a specific position to 1.

    Shifts 1 over by *position* bits and ORs with *number* so that only
    the bit at *position* is turned on.

    Args:
        number: The integer to modify.
        position: Zero-based bit index to set.

    Returns:
        The integer with the bit at *position* set to 1.

    Examples:
        >>> set_bit(22, 3)
        30
    """
    return number | (1 << position)


def clear_bit(number: int, position: int) -> int:
    """Clear the bit at a specific position to 0.

    Creates a mask with all bits set except at *position*, then ANDs
    with *number*.

    Args:
        number: The integer to modify.
        position: Zero-based bit index to clear.

    Returns:
        The integer with the bit at *position* cleared to 0.

    Examples:
        >>> clear_bit(22, 2)
        18
    """
    mask = ~(1 << position)
    return number & mask


def update_bit(number: int, position: int, bit: int) -> int:
    """Update the bit at a specific position to a given value.

    First clears the bit at *position*, then ORs in the new *bit* value
    shifted to that position.

    Args:
        number: The integer to modify.
        position: Zero-based bit index to update.
        bit: The new bit value (0 or 1).

    Returns:
        The integer with the bit at *position* set to *bit*.

    Examples:
        >>> update_bit(22, 3, 1)
        30
        >>> update_bit(22, 2, 0)
        18
    """
    mask = ~(1 << position)
    return (number & mask) | (bit << position)
