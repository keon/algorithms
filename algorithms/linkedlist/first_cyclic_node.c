"""
    Given a linked list, find the first node of a cycle in it.
    1 -> 2 -> 3 -> 4 -> 5 -> 1  => 1
    A -> B -> C -> D -> E -> C  => C

    Note: The solution is a direct implementation
          Floyd's cycle-finding algorithm (Floyd's Tortoise and Hare).
"""
import unittest


class Node:

    def __init__(self, x):
        self.val = x
        self.next = None


def first_cyclic_node(head):
    """
    :type head: Node
    :rtype: Node
    """
    runner = walker = head
    while runner and runner.next:
        runner = runner.next.next
        walker = walker.next
        if runner is walker:
            break

    if runner is None or runner.next is None:
        return None

    walker = head
    while runner is not walker:
        runner, walker = runner.next, walker.next
    return runner


class TestSuite(unittest.TestCase):

    def test_first_cyclic_node(self):

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

        self.assertEqual('C', first_cyclic_node(head).val)


if __name__ == '__main__':

    unittest.main()
