"""
Given a linked list, remove_range function accepts a starting and ending index
as parameters and removes the elements at those indexes (inclusive) from the list

For example:
List: [8, 13, 17, 4, 9, 12, 98, 41, 7, 23, 0, 92]
remove_range(list, 3, 8);
List becomes: [8, 13, 17, 23, 0, 92]

legal range of the list (0 < start index < end index < size of list).
"""
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
