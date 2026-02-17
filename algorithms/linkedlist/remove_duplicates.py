"""
Remove Duplicates from Linked List

Remove duplicate values from an unsorted linked list. Two approaches are
provided: hash-set-based (O(n) time, O(n) space) and runner technique
(O(n^2) time, O(1) space).

Reference: https://en.wikipedia.org/wiki/Linked_list

Complexity (hash set):
    Time:  O(n)
    Space: O(n)
"""

from __future__ import annotations


class Node:
    def __init__(self, val: object = None) -> None:
        self.val = val
        self.next: Node | None = None


def remove_dups(head: Node | None) -> None:
    """Remove duplicates from an unsorted linked list using a hash set.

    Args:
        head: Head of the linked list. Modified in-place.

    Returns:
        None. The list is modified in-place.

    Examples:
        >>> a = Node(1); b = Node(2); c = Node(1)
        >>> a.next = b; b.next = c
        >>> remove_dups(a)
        >>> a.next.val
        2
    """
    seen: set[object] = set()
    prev = Node()
    while head:
        if head.val in seen:
            prev.next = head.next
        else:
            seen.add(head.val)
            prev = head
        head = head.next


def remove_dups_wothout_set(head: Node | None) -> None:
    """Remove duplicates from an unsorted linked list without extra space.

    Uses a runner pointer to check for duplicates of each node value.

    Args:
        head: Head of the linked list. Modified in-place.

    Returns:
        None. The list is modified in-place.

    Examples:
        >>> a = Node(1); b = Node(2); c = Node(1)
        >>> a.next = b; b.next = c
        >>> remove_dups_wothout_set(a)
        >>> a.next.val
        2
    """
    current = head
    while current:
        runner = current
        while runner.next:
            if runner.next.val == current.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
