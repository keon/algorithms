"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes
with keys less than the node's key.
The right subtree of a node contains only nodes
with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
"""


def is_bst(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True
    stack = []
    pre = None
    while root and stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if pre and root.val <= pre.val:
            return False
        pre = root
        root = root.right
    return True
