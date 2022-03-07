'''
Time complexity : O(n)
'''


class Node:
    """ This is a class of Node """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root):
    """ Function to Preorder """
    res = []
    if not root:
        return res
    stack = []
    stack.append(root)
    while stack:
        root = stack.pop()
        res.append(root.val)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
    return res

def preorder_rec(root, res=None):
    """ Recursive Implementation """
    if root is None:
        return []
    if res is None:
        res = []
    res.append(root.val)
    preorder_rec(root.left, res)
    preorder_rec(root.right, res)
    return res
