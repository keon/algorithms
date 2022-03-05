"""
Given a stack, stutter takes a stack as a parameter and  replaces every value
in the stack with two occurrences of that value.

For example, suppose the stack stores these values:
bottom [3, 7, 1, 14, 9] top
Then the stack should store these values after the method terminates:
bottom [3, 3, 7, 7, 1, 1, 14, 14, 9, 9] top

Note: There are 2 solutions:
first_stutter: it uses a single stack as auxiliary storage
second_stutter: it uses a single queue as auxiliary storage
"""
import collections


def first_stutter(stack):
    storage_stack = []
    for i in range(len(stack)):
        storage_stack.append(stack.pop())
    for i in range(len(storage_stack)):
        val = storage_stack.pop()
        stack.append(val)
        stack.append(val)

    return stack


def second_stutter(stack):
    q = collections.deque()
    # Put all values into queue from stack
    for i in range(len(stack)):
        q.append(stack.pop())
    # Put values back into stack from queue
    for i in range(len(q)):
        stack.append(q.pop())
    # Now, stack is reverse, put all values into queue from stack
    for i in range(len(stack)):
        q.append(stack.pop())
    # Put 2 times value into stack from queue
    for i in range(len(q)):
        val = q.pop()
        stack.append(val)
        stack.append(val)

    return stack
