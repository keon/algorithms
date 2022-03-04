import math

def validate_bst(root):
    """ Visits node through inorder dfs, and validates that the tree is a BST
    :type root: Node
    :rtype: bool
    """
    def in_order(root, prev):

        if root == None:
            return True
        if not in_order(root.left, prev):
            return False
        if root.data <= prev:
            return False
        prev = root.data
        return in_order(root.right, prev)
    prev = -math.inf
    return in_order(root, prev)
