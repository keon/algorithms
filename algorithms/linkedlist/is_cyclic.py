"""
Linked List Cycle Detection

Given a linked list, determine if it has a cycle using Floyd's Tortoise and
Hare algorithm without extra space.

Reference: https://leetcode.com/problems/linked-list-cycle/

Complexity:
    Time:  O(n)
    Space: O(1)
"""

from __future__ import annotations


class Node:
    def __init__(self, x: object) -> None:
        self.val = x
        self.next: Node | None = None


def is_cyclic(head: Node | None) -> bool:
    """Determine whether a linked list contains a cycle.

    Args:
        head: Head of the linked list.

    Returns:
        True if the list has a cycle, False otherwise.

    Examples:
        >>> a = Node(1); b = Node(2); a.next = b; b.next = a
        >>> is_cyclic(a)
        True
        >>> c = Node(3); c.next = Node(4)
        >>> is_cyclic(c)
        False
    """
    if not head:
        return False
    runner = head
    walker = head
    while runner.next and runner.next.next:
        runner = runner.next.next
        walker = walker.next
        if runner == walker:
            return True
    return False
