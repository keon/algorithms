"""
Merge Two Sorted Lists

Merge two sorted linked lists into a single sorted list by splicing together
the nodes of the two input lists.

Reference: https://leetcode.com/problems/merge-two-sorted-lists/

Complexity:
    Time:  O(m + n)
    Space: O(1) iterative, O(m + n) recursive
"""

from __future__ import annotations


class Node:
    def __init__(self, x: int) -> None:
        self.val = x
        self.next: Node | None = None


def merge_two_list(l1: Node | None, l2: Node | None) -> Node | None:
    """Merge two sorted linked lists iteratively.

    Args:
        l1: Head of the first sorted list.
        l2: Head of the second sorted list.

    Returns:
        Head of the merged sorted list.

    Examples:
        >>> a = Node(1); a.next = Node(3)
        >>> b = Node(2); b.next = Node(4)
        >>> result = merge_two_list(a, b)
        >>> result.val
        1
    """
    sentinel = current = Node(0)
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    current.next = l1 or l2
    return sentinel.next


def merge_two_list_recur(l1: Node | None, l2: Node | None) -> Node | None:
    """Merge two sorted linked lists recursively.

    Args:
        l1: Head of the first sorted list.
        l2: Head of the second sorted list.

    Returns:
        Head of the merged sorted list.

    Examples:
        >>> a = Node(1); a.next = Node(3)
        >>> b = Node(2); b.next = Node(4)
        >>> result = merge_two_list_recur(a, b)
        >>> result.val
        1
    """
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = merge_two_list_recur(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_list_recur(l1, l2.next)
        return l2
