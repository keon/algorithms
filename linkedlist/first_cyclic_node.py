"""
    Given a linked list, find the first node of a cycle in it.
    1 -> 2 -> 3 -> 4 -> 5 -> 1  => 1
    A -> B -> C -> D -> E -> C  => C

    Note: The solution is a direct implementation
          Floyd's cycle-finding algorithm (Floyd's Tortoise and Hare).
"""


def firstCyclicNode(head):
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
