"""
Rotate List

Given a linked list, rotate the list to the right by k places, where k is
non-negative.

Reference: https://leetcode.com/problems/rotate-list/

Complexity:
    Time:  O(n)
    Space: O(1)
"""

from __future__ import annotations


def rotate_right(head: object | None, k: int) -> object | None:
    """Rotate a linked list to the right by k positions.

    Args:
        head: Head node of the linked list (must have .val and .next attrs).
        k: Number of positions to rotate right (non-negative).

    Returns:
        The new head of the rotated list.

    Examples:
        >>> rotate_right(None, 5) is None
        True
    """
    if not head or not head.next:
        return head
    current = head
    length = 1
    while current.next:
        current = current.next
        length += 1
    current.next = head
    k = k % length
    for _ in range(length - k):
        current = current.next
    head = current.next
    current.next = None
    return head
