"""
Given a linked list, swap every two adjacent nodes
and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space.
You may not modify the values in the list,
only nodes itself can be changed.
"""


class Node:
    def __init__(self, x=0):
        self.val = x
        self.next = None


def swap_pairs(head:"Node")->"Node":
    if not head:
        return head
    start = Node()
    pre = start
    pre.next = head
    while pre.next and pre.next.next:
        a = pre.next
        b = pre.next.next
        pre.next, a.next, b.next = b, b.next, a
        pre = a
    return start.next


if __name__ == "__main__":
    n = Node(1)
    n.next = Node(2)
    n.next.next = Node(3)
    n.next.next.next = Node(4)
    res = swap_pairs(n)

    while res:
        print(res.val, end=" ")
        res = res.next
    print("should be 2 1 4 3 ")

