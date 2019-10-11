"""
Given a linked list, swap every two adjacent nodes
and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space.
You may not modify the values in the list,
only nodes itself can be changed.
"""
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def swap_pairs(head):
    if not head:
        return head
    start = Node(0)
    start.next = head
    current = start
    while current.next and current.next.next:
        first = current.next
        second = current.next.next
        first.next = second.next
        current.next = second
        current.next.next = first
        current = current.next.next
    return start.next
