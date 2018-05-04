def is_palindrome(head):
    if not head:
        return True
    # split the list to two parts
    fast, slow = head.next, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    second = slow.next
    slow.next = None  # Don't forget here! But forget still works!
    # reverse the second part
    node = None
    while second:
        nxt = second.next
        second.next = node
        node = second
        second = nxt
    # compare two parts
    # second part has the same or one less node
    while node:
        if node.val != head.val:
            return False
        node = node.next
        head = head.next
    return True


def is_palindrome_stack(head):
    if not head or not head.next:
        return True

    # 1. Get the midpoint (slow)
    slow = fast = cur = head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

    # 2. Push the second half into the stack
    stack = [slow.val]
    while slow.next:
        slow = slow.next
        stack.append(slow.val)

    # 3. Comparison
    while stack:
        if stack.pop() != cur.val:
            return False
        cur = cur.next

    return True


def is_palindrome_dict(head):
    """
    This function builds up a dictionary where the keys are the values of the list,
    and the values are the positions at which these values occur in the list.
    We then iterate over the dict and if there is more than one key with an odd
    number of occurrences, bail out and return False.
    Otherwise, we want to ensure that the positions of occurrence sum to the
    value of the length of the list - 1, working from the outside of the list inward.
    For example:
    Input: 1 -> 1 -> 2 -> 3 -> 2 -> 1 -> 1
    d = {1: [0,1,5,6], 2: [2,4], 3: [3]}
    '3' is the middle outlier, 2+4=6, 0+6=6 and 5+1=6 so we have a palindrome.
    """
    if not head or not head.next:
        return True
    d = {}
    pos = 0
    while head:
        if head.val in d.keys():
            d[head.val].append(pos)
        else:
            d[head.val] = [pos]
        head = head.next
        pos += 1
    checksum = pos - 1
    middle = 0
    for v in d.values():
        if len(v) % 2 != 0:
            middle += 1
        else:
            step = 0
            for i in range(0, len(v)):
                if v[i] + v[len(v) - 1 - step] != checksum:
                    return False
                step += 1
        if middle > 1:
            return False
    return True
