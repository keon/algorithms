"""
First Cyclic Node

Given a linked list, find the first node of a cycle in it using Floyd's
cycle-finding algorithm (Tortoise and Hare).

Reference: https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_tortoise_and_hare

Complexity:
    Time:  O(n)
    Space: O(1)
"""

from __future__ import annotations


class Node:
    def __init__(self, x: object) -> None:
        self.val = x
        self.next: Node | None = None


def first_cyclic_node(head: Node | None) -> Node | None:
    """Find the first node of a cycle in the linked list.

    Args:
        head: Head of the linked list.

    Returns:
        The first node in the cycle, or None if there is no cycle.

    Examples:
        >>> a = Node(1); b = Node(2); c = Node(3)
        >>> a.next = b; b.next = c; c.next = b
        >>> first_cyclic_node(a).val
        2
    """
    runner = walker = head
    while runner and runner.next:
        runner = runner.next.next
        walker = walker.next
        if runner is walker:
            break

    if runner is None or runner.next is None:
        return None

    walker = head
    while runner is not walker:
        runner, walker = runner.next, walker.next
    return runner
