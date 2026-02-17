"""
Kth to Last Element

Find the kth to last element of a singly linked list. Three approaches are
provided: eval-based, dictionary-based, and two-pointer iterative.

Reference: https://en.wikipedia.org/wiki/Linked_list

Complexity (two-pointer):
    Time:  O(n)
    Space: O(1)
"""

from __future__ import annotations


class Node:
    def __init__(self, val: object = None) -> None:
        self.val = val
        self.next: Node | None = None


def kth_to_last_eval(head: Node, k: int) -> Node | bool:
    """Find the kth to last element using eval (not safe for user input).

    Args:
        head: Head of the linked list.
        k: Position from the end (1-indexed).

    Returns:
        The kth to last node, or False if k is invalid.

    Examples:
        >>> a = Node(1); b = Node(2); a.next = b
        >>> kth_to_last_eval(a, 1).val
        2
    """
    if not isinstance(k, int) or not head.val:
        return False

    nexts = '.'.join(['next' for _ in range(1, k + 1)])
    seeker = '.'.join(['head', nexts])

    while head:
        if eval(seeker) is None:  # noqa: S307
            return head
        else:
            head = head.next

    return False


def kth_to_last_dict(head: Node | None, k: int) -> Node | bool:
    """Find the kth to last element using a dictionary.

    Args:
        head: Head of the linked list.
        k: Position from the end (1-indexed).

    Returns:
        The kth to last node, or False if k is invalid.

    Examples:
        >>> a = Node(1); b = Node(2); a.next = b
        >>> kth_to_last_dict(a, 1).val
        2
    """
    if not (head and k > -1):
        return False
    index_map: dict[int, Node] = {}
    count = 0
    while head:
        index_map[count] = head
        head = head.next
        count += 1
    return len(index_map) - k in index_map and index_map[len(index_map) - k]


def kth_to_last(head: Node | None, k: int) -> Node | bool:
    """Find the kth to last element using two pointers.

    Advances the first pointer k steps ahead, then moves both pointers
    together until the first pointer reaches the end.

    Args:
        head: Head of the linked list.
        k: Position from the end (1-indexed).

    Returns:
        The kth to last node, or False if the list is empty.

    Raises:
        IndexError: If k exceeds the length of the list.

    Examples:
        >>> a = Node(1); b = Node(2); a.next = b
        >>> kth_to_last(a, 1).val
        2
    """
    if not (head or k > -1):
        return False
    ahead = head
    behind = head
    for _ in range(1, k + 1):
        if ahead is None:
            raise IndexError
        ahead = ahead.next
    while ahead:
        ahead = ahead.next
        behind = behind.next
    return behind
