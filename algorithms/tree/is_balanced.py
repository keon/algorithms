
def is_balanced(root):
    """
    O(N) solution
    """
    return -1 != get_depth(root)

def get_depth(root):
    """
    return 0 if unbalanced else depth + 1
    """
    if not root:
        return 0
    left  = get_depth(root.left)
    right = get_depth(root.right)
    if abs(left-right) > 1 or left == -1 or right == -1:
        return -1
    return 1 + max(left, right)

################################

def is_balanced(root):
    """
    O(N^2) solution
    """
    left = max_height(root.left)
    right = max_height(root.right)
    return abs(left-right) <= 1 and is_balanced(root.left) and is_balanced(root.right)

def max_height(root):
    if not root:
        return 0
    return max(max_height(root.left), max_height(root.right)) + 1
