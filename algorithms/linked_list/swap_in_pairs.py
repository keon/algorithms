"""
Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return the new head.
Only node links are changed, not node values.

Reference: https://leetcode.com/problems/swap-nodes-in-pairs/

Complexity:
    Time:  O(n)
    Space: O(1)
"""

from __future__ import annotations


class Node:
    def __init__(self, x: int) -> None:
        self.val = x
        self.next: Node | None = None


def swap_pairs(head: Node | None) -> Node | None:
    """Swap every two adjacent nodes in a linked list.

    Args:
        head: Head of the linked list.

    Returns:
        The new head after pairwise swapping.

    Examples:
        >>> a = Node(1); b = Node(2); a.next = b
        >>> result = swap_pairs(a)
        >>> result.val
        2
    """
    if not head:
        return head
    sentinel = Node(0)
    sentinel.next = head
    current = sentinel
    while current.next and current.next.next:
        first = current.next
        second = current.next.next
        first.next = second.next
        current.next = second
        current.next.next = first
        current = current.next.next
    return sentinel.next
