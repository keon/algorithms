"""
Reverse a singly linked list.
"""


def reverse_list(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next:
        return head
    prev = None
    while head:
        current = head
        head = head.next
        current.next = prev
        prev = current
    return prev
