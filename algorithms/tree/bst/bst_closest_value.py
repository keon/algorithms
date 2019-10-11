# Given a non-empty binary search tree and a target value,
# find the value in the BST that is closest to the target.

# Note:
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST
# that is closest to the target.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def closest_value(root, target):
    """
    :type root: TreeNode
    :type target: float
    :rtype: int
    """
    a = root.val
    kid = root.left if target < a else root.right
    if not kid:
        return a
    b = closest_value(kid, target)
    return min((a,b), key=lambda x: abs(target-x))
