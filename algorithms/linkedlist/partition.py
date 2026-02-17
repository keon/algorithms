"""
Partition Linked List

Partition a linked list around a value x so that all nodes with values less
than x come before nodes with values greater than or equal to x.

Reference: https://leetcode.com/problems/partition-list/

Complexity:
    Time:  O(n)
    Space: O(1)
"""

from __future__ import annotations


class Node:
    def __init__(self, val: object = None) -> None:
        self.val = int(val)
        self.next: Node | None = None


def partition(head: Node | None, x: int) -> None:
    """Partition a linked list in-place around value x.

    Rearranges nodes so that all nodes with values less than x appear before
    nodes with values greater than or equal to x.

    Args:
        head: Head of the linked list.
        x: The partition value.

    Returns:
        None. The list is modified in-place.

    Examples:
        >>> a = Node(3); b = Node(5); c = Node(1)
        >>> a.next = b; b.next = c
        >>> partition(a, 5)
    """
    left = None
    right = None
    prev = None
    current = head
    while current:
        if int(current.val) >= x:
            if not right:
                right = current
        else:
            if not left:
                left = current
            else:
                prev.next = current.next
                left.next = current
                left = current
                left.next = right
        if prev and prev.next is None:
            break
        prev = current
        current = current.next
