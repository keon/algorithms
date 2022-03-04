"""
Given a stack, switch_pairs function takes a stack as a parameter and that
switches successive pairs of numbers starting at the bottom of the stack.

For example, if the stack initially stores these values:
bottom [3, 8, 17, 9, 1, 10] top
Your function should switch the first pair (3, 8),
the second pair (17, 9), ...:
bottom [8, 3, 9, 17, 10, 1] top

if there are an odd number of values in the stack, the value at the top of the
stack is not moved: For example:
bottom [3, 8, 17, 9, 1] top
It would again switch pairs of values, but the value at the
top of the stack (1)
would not be moved
bottom [8, 3, 9, 17, 1] top

Note: There are 2 solutions:
first_switch_pairs: it uses a single stack as auxiliary storage
second_switch_pairs: it uses a single queue as auxiliary storage
"""
import collections


def first_switch_pairs(stack):
    storage_stack = []
    for i in range(len(stack)):
        storage_stack.append(stack.pop())
    for i in range(len(storage_stack)):
        if len(storage_stack) == 0:
            break
        first = storage_stack.pop()
        if len(storage_stack) == 0:    # case: odd number of values in stack
            stack.append(first)
            break
        second = storage_stack.pop()
        stack.append(second)
        stack.append(first)
    return stack


def second_switch_pairs(stack):
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
    # Swap pairs by appending the 2nd value before appending 1st value
    for i in range(len(q)):
        if len(q) == 0:
            break
        first = q.pop()
        if len(q) == 0:                 # case: odd number of values in stack
            stack.append(first)
            break
        second = q.pop()
        stack.append(second)
        stack.append(first)

    return stack
