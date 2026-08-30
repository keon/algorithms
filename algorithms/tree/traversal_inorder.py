"""Time complexity : O(n)."""


class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def inorder(root):
    """In order function."""
    res = []
    if not root:
        return res
    stack = []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.append(root.val)
        root = root.right
    return res


def inorder_rec(root, res=None):
    """Recursive Implementation."""
    if root is None:
        return []
    if res is None:
        res = []
    inorder_rec(root.left, res)
    res.append(root.val)
    inorder_rec(root.right, res)
    return res
