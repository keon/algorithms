"""
Merge K Sorted Linked Lists

Merge k sorted linked lists into one sorted linked list using a heap
for efficient minimum extraction.

Reference: https://leetcode.com/problems/merge-k-sorted-lists/

Complexity:
    Time:  O(n log k) where n is total elements and k is number of lists
    Space: O(k)
"""

from __future__ import annotations

from heapq import heappop, heapreplace, heapify


class ListNode:
    """Singly linked list node.

    Args:
        val: The node value.
    """

    def __init__(self, val: int) -> None:
        self.val = val
        self.next: ListNode | None = None


def merge_k_lists(lists: list[ListNode | None]) -> ListNode | None:
    """Merge k sorted linked lists into a single sorted linked list.

    Args:
        lists: A list of head nodes of sorted linked lists.

    Returns:
        Head of the merged sorted linked list, or None if all are empty.

    Examples:
        >>> n1 = ListNode(1)
        >>> n2 = ListNode(2)
        >>> result = merge_k_lists([n1, n2])
        >>> result.val
        1
    """
    dummy = node = ListNode(0)
    heap: list[tuple[int, int, ListNode]] = []
    for idx, head in enumerate(lists):
        if head:
            heap.append((head.val, idx, head))
    heapify(heap)
    while heap:
        val, idx, n_val = heap[0]
        if n_val.next is None:
            heappop(heap)
        else:
            heapreplace(heap, (n_val.next.val, idx, n_val.next))
        node.next = n_val
        node = node.next

    return dummy.next
