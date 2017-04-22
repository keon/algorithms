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
    flag = True
    while flag == True:
        while root:
            stack.append(root)
            root = root.left
        if len(stack) > 0:
            root = stack.pop()
            res.append(root.data)
            root = root.right
        else:
            flag = False
    return res
