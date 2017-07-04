def detect_loop(head):
    """
    Given a circular linked list, implement an algorithm which returns the node
        at the beginning of the loop.
    * DEFINITION
    * Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.
    * EXAMPLE
    * Input: A->B->C->D->E->C [the same C as earlier]
    * Output: C
    """
    if not (head and head.next):
        return None
    seen = []
    while head:
        if head in seen and head.next in seen:
            return head
        else:
            seen.append(head)
        head = head.next
    return None


class Node(object):
  def __init__(self, val=None):
    self.val = val
    self.next = None


def test():

    # A->B->C->D->E->C [the same C as earlier]

    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = c

    # We do not print the list itself, because it will run forever!
    print detect_loop(a)
    assert detect_loop(a).val == c.val

if __name__ == '__main__':
    test()
