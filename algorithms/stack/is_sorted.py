"""
Given a stack, a function is_sorted accepts a stack as a parameter and returns
true if the elements in the stack occur in ascending increasing order from
bottom, and false otherwise. That is, the smallest element should be at bottom

For example:
bottom [6, 3, 5, 1, 2, 4] top
The function should return false
bottom [1, 2, 3, 4, 5, 6] top
The function should return true
"""
def is_sorted(stack):
    storage_stack = []
    for i in range(len(stack)):
        if len(stack) == 0:
            break
        first_val = stack.pop()
        if len(stack) == 0:
            break
        second_val = stack.pop()
        if first_val < second_val:
            return False
        storage_stack.append(first_val)
        stack.append(second_val)

    # Backup stack
    for i in range(len(storage_stack)):
        stack.append(storage_stack.pop())

    return True
