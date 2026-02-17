"""
Intersection of Two Linked Lists

Given two singly linked lists that converge at some node, find and return the
intersecting node. The node identity (not value) is the unique identifier.

Reference: https://leetcode.com/problems/intersection-of-two-linked-lists/

Complexity:
    Time:  O(m + n)
    Space: O(1)
"""

from __future__ import annotations


class Node:
    def __init__(self, val: object = None) -> None:
        self.val = val
        self.next: Node | None = None


def intersection(h1: Node, h2: Node) -> Node | None:
    """Find the intersection node of two linked lists.

    Args:
        h1: Head of the first linked list.
        h2: Head of the second linked list.

    Returns:
        The intersecting node, or None if the lists do not intersect.

    Examples:
        >>> shared = Node(7)
        >>> a = Node(1); a.next = shared
        >>> b = Node(2); b.next = shared
        >>> intersection(a, b).val
        7
    """
    count = 0
    flag = None
    h1_orig = h1
    h2_orig = h2

    while h1 or h2:
        count += 1

        if not flag and (h1.next is None or h2.next is None):
            flag = (count, h1.next, h2.next)

        if h1:
            h1 = h1.next
        if h2:
            h2 = h2.next

    long_len = count
    short_len = flag[0]

    if flag[1] is None:
        shorter = h1_orig
        longer = h2_orig
    elif flag[2] is None:
        shorter = h2_orig
        longer = h1_orig

    while longer and shorter:
        while long_len > short_len:
            longer = longer.next
            long_len -= 1

        if longer == shorter:
            return longer
        else:
            longer = longer.next
            shorter = shorter.next

    return None
