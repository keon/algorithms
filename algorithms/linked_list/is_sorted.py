"""
Is Sorted Linked List

Given a linked list, determine whether the list is sorted in non-decreasing
order. An empty list is considered sorted.

Reference: https://en.wikipedia.org/wiki/Linked_list

Complexity:
    Time:  O(n)
    Space: O(1)
"""

from __future__ import annotations


def is_sorted(head: object | None) -> bool:
    """Check if a linked list is sorted in non-decreasing order.

    Args:
        head: Head node of the linked list (must have .val and .next attrs).

    Returns:
        True if the list is sorted or empty, False otherwise.

    Examples:
        >>> is_sorted(None)
        True
    """
    if not head:
        return True
    current = head
    while current.next:
        if current.val > current.next.val:
            return False
        current = current.next
    return True
