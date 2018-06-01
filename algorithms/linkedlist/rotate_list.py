"""
Given a list, rotate the list to the right by k places,
where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def rotate_right(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if not head or not head.next:
        return head
    current = head
    length = 1
    # count length of the list
    while current.next:
        current = current.next
        length += 1
    # make it circular
    current.next = head
    k = k % length
    # rotate until length-k
    for i in range(length-k):
        current = current.next
    head = current.next
    current.next = None
    return head
