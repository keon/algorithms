class Node():
    def __init__(self, val=None):
        self.val = val
        self.next = None


def kth_to_last_eval(head, k):
    """
    This is a suboptimal, hacky method using eval(), which is not
     safe for user input. We guard against danger by ensuring k in an int
    """
    if not isinstance(k, int) or not head.val:
        return False

    nexts = '.'.join(['next' for n in range(1, k+1)])
    seeker = str('.'.join(['head', nexts]))

    while head:
        if eval(seeker) is None:
            return head
        else:
            head = head.next

    return False


def kth_to_last_dict(head, k):
    """
    This is a brute force method where we keep a dict the size of the list
    Then we check it for the value we need. If the key is not in the dict,
    our and statement will short circuit and return False
    """
    if not (head and k > -1):
        return False
    d = dict()
    count = 0
    while head:
        d[count] = head
        head = head.next
        count += 1
    return len(d)-k in d and d[len(d)-k]


def kth_to_last(head, k):
    """
    This is an optimal method using iteration.
    We move p1 k steps ahead into the list.
    Then we move p1 and p2 together until p1 hits the end.
    """
    if not (head or k > -1):
        return False
    p1 = head
    p2 = head
    for i in range(1, k+1):
        if p1 is None:
            # Went too far, k is not valid
            raise IndexError
        p1 = p1.next
    while p1:
        p1 = p1.next
        p2 = p2.next
    return p2


def print_linked_list(head):
    string = ""
    while head.next:
        string += head.val + " -> "
        head = head.next
    string += head.val
    print(string)


def test():
    # def make_test_li
    # A A B C D C F G
    a1 = Node("A")
    a2 = Node("A")
    b = Node("B")
    c1 = Node("C")
    d = Node("D")
    c2 = Node("C")
    f = Node("F")
    g = Node("G")
    a1.next = a2
    a2.next = b
    b.next = c1
    c1.next = d
    d.next = c2
    c2.next = f
    f.next = g
    print_linked_list(a1)

    # test kth_to_last_eval
    kth = kth_to_last_eval(a1, 4)
    try:
        assert kth.val == "D"
    except AssertionError as e:
        e.args += ("Expecting D, got %s" % kth.val,)
        raise

    # test kth_to_last_dict
    kth = kth_to_last_dict(a1, 4)
    try:
        assert kth.val == "D"
    except AssertionError as e:
        e.args += ("Expecting D, got %s" % kth.val,)
        raise

    # test kth_to_last
    kth = kth_to_last(a1, 4)
    try:
        assert kth.val == "D"
    except AssertionError as e:
        e.args += ("Expecting D, got %s" % kth.val,)
        raise
    print("all passed.")

if __name__ == '__main__':
    test()
