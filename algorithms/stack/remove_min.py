"""
Given a stack, a function remove_min accepts a stack as a parameter
and removes the smallest value from the stack.

For example:
bottom [2, 8, 3, -6, 7, 3] top
After remove_min(stack):
bottom [2, 8, 3, 7, 3] top

"""
def remove_min(stack):
    storage_stack = []
    if len(stack) == 0:  # Stack is empty
        return stack
    # Find the smallest value
    min_index = stack.index(min(stack))
    stack.pop(min_index)
    return stack
