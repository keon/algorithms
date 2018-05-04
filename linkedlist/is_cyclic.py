"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""
class Node:

    def __init__(self, x):
        self.val = x
        self.next = None

def is_cyclic(head):
    """
    :type head: Node
    :rtype: bool
    """
    if not head:
        return False
    runner = head
    walker = head
    while runner.next and runner.next.next:
        runner = runner.next.next
        walker = walker.next
        if runner == walker:
            return True
    return False
