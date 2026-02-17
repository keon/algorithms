"""
Palindrome Linked List

Determine whether a singly linked list is a palindrome. Three approaches are
provided: reverse-half, stack-based, and dictionary-based.

Reference: https://leetcode.com/problems/palindrome-linked-list/

Complexity (reverse-half):
    Time:  O(n)
    Space: O(1)
"""

from __future__ import annotations


def is_palindrome(head: object | None) -> bool:
    """Check if a linked list is a palindrome by reversing the second half.

    Args:
        head: Head node of the linked list (must have .val and .next attrs).

    Returns:
        True if the list is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome(None)
        True
    """
    if not head:
        return True
    fast, slow = head.next, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    second = slow.next
    slow.next = None
    node = None
    while second:
        nxt = second.next
        second.next = node
        node = second
        second = nxt
    while node:
        if node.val != head.val:
            return False
        node = node.next
        head = head.next
    return True


def is_palindrome_stack(head: object | None) -> bool:
    """Check if a linked list is a palindrome using a stack.

    Args:
        head: Head node of the linked list.

    Returns:
        True if the list is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome_stack(None)
        True
    """
    if not head or not head.next:
        return True

    slow = fast = current = head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

    stack = [slow.val]
    while slow.next:
        slow = slow.next
        stack.append(slow.val)

    while stack:
        if stack.pop() != current.val:
            return False
        current = current.next

    return True


def is_palindrome_dict(head: object | None) -> bool:
    """Check if a linked list is a palindrome using a dictionary of positions.

    Builds a dictionary mapping each value to its list of positions, then
    verifies that positions are symmetric around the center.

    Args:
        head: Head node of the linked list.

    Returns:
        True if the list is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome_dict(None)
        True
    """
    if not head or not head.next:
        return True
    positions: dict[object, list[int]] = {}
    pos = 0
    current = head
    while current:
        if current.val in positions:
            positions[current.val].append(pos)
        else:
            positions[current.val] = [pos]
        current = current.next
        pos += 1
    checksum = pos - 1
    middle = 0
    for indices in positions.values():
        if len(indices) % 2 != 0:
            middle += 1
        else:
            step = 0
            for i in range(len(indices)):
                if indices[i] + indices[len(indices) - 1 - step] != checksum:
                    return False
                step += 1
        if middle > 1:
            return False
    return True
