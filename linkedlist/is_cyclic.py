"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""
import unittest


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


class TestSuite(unittest.TestCase):

    def test_is_cyclic(self):

        # create linked list => A -> B -> C -> D -> E -> C
        head = Node('A')
        head.next = Node('B')
        curr = head.next

        cyclic_node = Node('C')
        curr.next = cyclic_node

        curr = curr.next
        curr.next = Node('D')
        curr = curr.next
        curr.next = Node('E')
        curr = curr.next
        curr.next = cyclic_node

        self.assertTrue(is_cyclic(head))

        # create linked list 1 -> 2 -> 3 -> 4
        head = Node(1)
        curr = head
        for i in range(2, 6):
            curr.next = Node(i)
            curr = curr.next

        self.assertFalse(is_cyclic(head))


if __name__ == '__main__':

    unittest.main()
