def is_balanced(root):
    return __is_balanced_recursive(root)


def __is_balanced_recursive(root):
    """
    O(N) solution
    """
    return -1 != __get_depth(root)


def __get_depth(root):
    """
    return 0 if unbalanced else depth + 1
    """
    if root is None:
        return 0
    left = __get_depth(root.left)
    right = __get_depth(root.right)
    if abs(left-right) > 1 or -1 in [left, right]:
        return -1
    return 1 + max(left, right)


# def is_balanced(root):
#     """
#     O(N^2) solution
#     """
#     left = max_height(root.left)
#     right = max_height(root.right)
#     return abs(left-right) <= 1 and is_balanced(root.left) and
#     is_balanced(root.right)

# def max_height(root):
#     if root is None:
#         return 0
#     return max(max_height(root.left), max_height(root.right)) + 1
