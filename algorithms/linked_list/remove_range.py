"""
Remove Range from Linked List

Given a linked list and a start and end index, remove the elements at those
indexes (inclusive) from the list.

Reference: https://en.wikipedia.org/wiki/Linked_list

Complexity:
    Time:  O(n)
    Space: O(1)
"""

from __future__ import annotations


def remove_range(head: object | None, start: int, end: int) -> object | None:
    """Remove nodes from index start to end (inclusive) from a linked list.

    Args:
        head: Head node of the linked list (must have .next attr).
        start: Starting index of the range to remove.
        end: Ending index of the range to remove (inclusive).

    Returns:
        The (possibly new) head of the modified list.

    Examples:
        >>> remove_range(None, 0, 0) is None
        True
    """
    assert start <= end
    if start == 0:
        for _ in range(end + 1):
            if head is not None:
                head = head.next
    else:
        current = head
        for _ in range(start - 1):
            current = current.next
        for _ in range(end - start + 1):
            if current is not None and current.next is not None:
                current.next = current.next.next
    return head
