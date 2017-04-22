"""
Given a binary tree, the following function performs iterative inorder
traversal of the tree.

T(n)- O(n)
S(n)- O(n)
"""

def inorder(root):
    res = []
    if not root:
        return res
    stack = []
    while root and stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.add(root.val)
        root = root.right
    return res
