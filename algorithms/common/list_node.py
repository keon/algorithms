"""Singly linked list node shared across all linked list algorithms.

This module provides the universal ListNode used by every linked list
algorithm in this library. Using a single shared type means you can
compose algorithms: merge two lists, reverse the result, check if
it's a palindrome.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ListNode:
    """A node in a singly linked list.

    Attributes:
        val: The value stored in this node.
        next: Reference to the next node.

    Examples:
        >>> head = ListNode(1, ListNode(2, ListNode(3)))
        >>> head.val
        1
        >>> head.next.val
        2
    """

    val: int = 0
    next: ListNode | None = None
