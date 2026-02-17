"""
Reverse Linked List

Reverse a singly linked list. Both iterative and recursive solutions are
provided.

Reference: https://leetcode.com/problems/reverse-linked-list/

Complexity:
    Time:  O(n)
    Space: O(1) iterative, O(n) recursive
"""

from __future__ import annotations


def reverse_list(head: object | None) -> object | None:
    """Reverse a singly linked list iteratively.

    Args:
        head: Head node of the linked list (must have .next attr).

    Returns:
        The new head of the reversed list.

    Examples:
        >>> reverse_list(None) is None
        True
    """
    if not head or not head.next:
        return head
    prev = None
    while head:
        current = head
        head = head.next
        current.next = prev
        prev = current
    return prev


def reverse_list_recursive(head: object | None) -> object | None:
    """Reverse a singly linked list recursively.

    Args:
        head: Head node of the linked list (must have .next attr).

    Returns:
        The new head of the reversed list.

    Examples:
        >>> reverse_list_recursive(None) is None
        True
    """
    if head is None or head.next is None:
        return head
    rest = head.next
    head.next = None
    reversed_rest = reverse_list_recursive(rest)
    rest.next = head
    return reversed_rest
