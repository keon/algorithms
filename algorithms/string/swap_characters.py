"""Swap characters — check if two strings can be made equal by one swap.

Given two strings of equal length, determine whether exactly one swap
of two characters in the first string can make it equal to the second.

Inspired by PR #890 (Thejas-1).
"""

from __future__ import annotations


def can_swap_to_equal(s: str, t: str) -> bool:
    """Return True if swapping exactly one pair in *s* yields *t*."""
    if len(s) != len(t):
        return False
    diffs = [(a, b) for a, b in zip(s, t, strict=False) if a != b]
    return len(diffs) == 2 and diffs[0] == diffs[1][::-1]
