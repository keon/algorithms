"""
Delete Node in a Linked List

Given only access to a node (not the tail) in a singly linked list, delete
that node by copying the next node's value and skipping over it.

Reference: https://leetcode.com/problems/delete-node-in-a-linked-list/

Complexity:
    Time:  O(1)
    Space: O(1)
"""

from __future__ import annotations


class Node:
    def __init__(self, x: int) -> None:
        self.val = x
        self.next: Node | None = None


def delete_node(node: Node | None) -> None:
    """Delete the given node from a singly linked list in-place.

    The node must not be the tail node. The deletion is performed by copying
    the value from the next node and then skipping the next node.

    Args:
        node: The node to delete (must not be None or the tail).

    Raises:
        ValueError: If node is None or is the tail node.

    Examples:
        >>> head = Node(1); head.next = Node(2); head.next.next = Node(3)
        >>> delete_node(head.next)
        >>> head.next.val
        3
    """
    if node is None or node.next is None:
        raise ValueError
    node.val = node.next.val
    node.next = node.next.next
