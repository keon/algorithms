"""
Given a linked list, is_sort function returns true if the list is in sorted
(increasing) order and return false otherwise. An empty list is considered
to be sorted.

For example:
Null :List is sorted
1 2 3 4 :List is sorted
1 2 -1 3 :List is not sorted
"""

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def is_sort(head):
    if not head:
        return True
    current = head
    while current.next:
        if current.val > current.next.val:
            return False
        current = current.next
    return True

if __name__ == "__main__":
    n = Node(None)
    # Test case: 1 2 3 4 : List is sorted
    n = Node(1)
    n.next = Node(2)
    n.next.next = Node(3)
    n.next.next.next = Node(4)
    if is_sort(n) == True:
        print("List is sorted\n")
    else:
        print("List is not sorted\n")
    # Test case: 1 2 -1 3 : List is not sorted
    n = Node(1)
    n.next = Node(2)
    n.next.next = Node(-1)
    n.next.next.next = Node(3)
    if is_sort(n) == True:
        print("List is sorted\n")
    else:
        print("List is not sorted\n")
