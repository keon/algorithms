"""
Add Two Numbers (Linked List)

Given two non-empty linked lists representing two non-negative integers with
digits stored in reverse order, add the two numbers and return the sum as a
linked list.

Reference: https://leetcode.com/problems/add-two-numbers/

Complexity:
    Time:  O(max(m, n))
    Space: O(max(m, n))
"""

from __future__ import annotations


class Node:
    def __init__(self, x: int) -> None:
        self.val = x
        self.next: Node | None = None


def add_two_numbers(left: Node, right: Node) -> Node:
    """Add two numbers represented as reversed linked lists.

    Args:
        left: Head of the first number's linked list.
        right: Head of the second number's linked list.

    Returns:
        Head of the resulting sum linked list.

    Examples:
        >>> # (2 -> 4 -> 3) + (5 -> 6 -> 4) = (7 -> 0 -> 8)
        >>> l1 = Node(2); l1.next = Node(4); l1.next.next = Node(3)
        >>> l2 = Node(5); l2.next = Node(6); l2.next.next = Node(4)
        >>> convert_to_str(add_two_numbers(l1, l2))
        '708'
    """
    head = Node(0)
    current = head
    carry = 0
    while left or right:
        carry //= 10
        if left:
            carry += left.val
            left = left.next
        if right:
            carry += right.val
            right = right.next
        current.next = Node(carry % 10)
        current = current.next
    if carry // 10 == 1:
        current.next = Node(1)
    return head.next


def convert_to_list(number: int) -> Node | None:
    """Convert a non-negative integer into a reversed linked list.

    Args:
        number: A non-negative integer to convert.

    Returns:
        Head of the reversed linked list, or None if number is negative.

    Examples:
        >>> convert_to_str(convert_to_list(112))
        '211'
    """
    if number < 0:
        return None
    head = Node(0)
    current = head
    remainder = number % 10
    quotient = number // 10

    while quotient != 0:
        current.next = Node(remainder)
        current = current.next
        remainder = quotient % 10
        quotient //= 10
    current.next = Node(remainder)
    return head.next


def convert_to_str(node: Node | None) -> str:
    """Convert a linked list of digits to a string.

    Args:
        node: Head of the linked list.

    Returns:
        String representation of the linked list values.

    Examples:
        >>> n = Node(2); n.next = Node(4); n.next.next = Node(3)
        >>> convert_to_str(n)
        '243'
    """
    result = ""
    while node:
        result += str(node.val)
        node = node.next
    return result
