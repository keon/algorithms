"""
Given a stack, a function is_consecutive takes a stack as a parameter and that
returns whether or not the stack contains a sequence of consecutive integers
starting from the bottom of the stack (returning true if it does, returning
false if it does not).

For example:
bottom [3, 4, 5, 6, 7] top
Then the call of is_consecutive(s) should return true.
bottom [3, 4, 6, 7] top
Then the call of is_consecutive(s) should return false.
bottom [3, 2, 1] top
The function should return false due to reverse order.

Note: There are 2 solutions:
first_is_consecutive: it uses a single stack as auxiliary storage
second_is_consecutive: it uses a single queue as auxiliary storage
"""
import collections

def first_is_consecutive(stack):
    storage_stack = []
    for i in range(len(stack)):
        first_value = stack.pop()
        if len(stack) == 0:                # Case odd number of values in stack
            return True
        second_value = stack.pop()
        if first_value - second_value != 1: # Not consecutive
            return False
        stack.append(second_value)          # Backup second value
        storage_stack.append(first_value)

    # Back up stack from storage stack
    for i in range(len(storage_stack)):
        stack.append(storage_stack.pop())
    return True

def second_is_consecutive(stack):
    q = collections.deque()
    for i in range(len(stack)):
        first_value = stack.pop()
        if len(stack) == 0:                # Case odd number of values in stack
            return True
        second_value = stack.pop()
        if first_value - second_value != 1: # Not consecutive
            return False
        stack.append(second_value)          # Backup second value
        q.append(first_value)

    # Back up stack from queue
    for i in range(len(q)):
        stack.append(q.pop())
    for i in range(len(stack)):
        q.append(stack.pop())
    for i in range(len(q)):
        stack.append(q.pop())

    return True
