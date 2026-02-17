"""
Copy List with Random Pointer

Given a linked list where each node contains an additional random pointer that
could point to any node in the list or null, return a deep copy of the list.

Reference: https://leetcode.com/problems/copy-list-with-random-pointer/

Complexity:
    Time:  O(n)
    Space: O(n)
"""

from __future__ import annotations

from collections import defaultdict


class RandomListNode:
    """Node with next and random pointers for deep-copy problem."""

    def __init__(self, label: int) -> None:
        self.label = label
        self.next: RandomListNode | None = None
        self.random: RandomListNode | None = None


def copy_random_pointer_v1(head: RandomListNode | None) -> RandomListNode | None:
    """Deep-copy a linked list with random pointers using a dictionary.

    Args:
        head: Head of the original list.

    Returns:
        Head of the deep-copied list.

    Examples:
        >>> node = RandomListNode(1)
        >>> node.random = node
        >>> copied = copy_random_pointer_v1(node)
        >>> copied.label == 1 and copied.random is copied
        True
    """
    node_map: dict[RandomListNode, RandomListNode] = {}
    current = head
    while current:
        node_map[current] = RandomListNode(current.label)
        current = current.next
    current = head
    while current:
        node_map[current].next = node_map.get(current.next)
        node_map[current].random = node_map.get(current.random)
        current = current.next
    return node_map.get(head)


def copy_random_pointer_v2(head: RandomListNode | None) -> RandomListNode | None:
    """Deep-copy a linked list with random pointers using defaultdict.

    Args:
        head: Head of the original list.

    Returns:
        Head of the deep-copied list.

    Examples:
        >>> node = RandomListNode(1)
        >>> node.random = node
        >>> copied = copy_random_pointer_v2(node)
        >>> copied.label == 1 and copied.random is copied
        True
    """
    copy: defaultdict[RandomListNode | None, RandomListNode | None] = defaultdict(
        lambda: RandomListNode(0)
    )
    copy[None] = None
    node = head
    while node:
        copy[node].label = node.label
        copy[node].next = copy[node.next]
        copy[node].random = copy[node.random]
        node = node.next
    return copy[head]
