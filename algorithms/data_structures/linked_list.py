"""
Linked List Node Definitions

Basic node classes for singly and doubly linked lists, serving as foundational
building blocks for linked list algorithms.

Reference: https://en.wikipedia.org/wiki/Linked_list

Complexity:
    Time:  O(1) for node creation
    Space: O(1) per node
"""

from __future__ import annotations


class SinglyLinkedListNode:
    """A node in a singly linked list.

    Attributes:
        value: The value stored in the node.
        next: Reference to the next node, or None.
    """

    def __init__(self, value: object) -> None:
        self.value = value
        self.next: SinglyLinkedListNode | None = None


class DoublyLinkedListNode:
    """A node in a doubly linked list.

    Attributes:
        value: The value stored in the node.
        next: Reference to the next node, or None.
        prev: Reference to the previous node, or None.
    """

    def __init__(self, value: object) -> None:
        self.value = value
        self.next: DoublyLinkedListNode | None = None
        self.prev: DoublyLinkedListNode | None = None
