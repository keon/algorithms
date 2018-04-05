"""
Given a linked list, remove_range function accepts a starting and ending index
as parameters and removes the elements at those indexes (inclusive) from the list

For example:
List: [8, 13, 17, 4, 9, 12, 98, 41, 7, 23, 0, 92]
remove_range(list, 3, 8);
List becomes: [8, 13, 17, 23, 0, 92]

legal range of the list (0 < start index < end index < size of list).
"""

class Node:
    def __init__(self,x):
        self.val = x
        self.next = None

def remove_range(head, start, end):
    assert(start <= end)
    # Case: remove node at head
    if start == 0:
        for i in range(0, end+1):
            if head != None:
                head = head.next
    else:
        current = head
        # Move pointer to start position
        for i in range(0,start-1):
            current = current.next
        # Remove data until the end
        for i in range(0, end-start + 1):
            if current != None and current.next != None:
                current.next = current.next.next
    return head

if __name__ == "__main__":
    # Test case: middle case.
    head = Node(None)
    head = Node(0)
    head.next = Node(1)
    head.next.next = Node(2)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(4)
    result = remove_range(head,1,3)  # Expect output: 0 4
    # Test case: taking out the front node
    head = Node(None)
    head = Node(0)
    head.next = Node(1)
    head.next.next = Node(2)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(4)
    result = remove_range(head,0,1)  # Expect output: 2 3 4
    # Test case: removing all the nodes
    head = Node(None)
    head = Node(0)
    head.next = Node(1)
    head.next.next = Node(2)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(4)
    result = remove_range(head,0,7)  # Expect output: Null
