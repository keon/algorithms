"""
Balanced Binary Tree

Determines whether a binary tree is height-balanced, meaning the depth of the
left and right subtrees of every node differ by at most one.

Reference: https://en.wikipedia.org/wiki/AVL_tree

Complexity:
    Time:  O(n)
    Space: O(n) due to recursion stack
"""

from __future__ import annotations

from algorithms.tree.tree import TreeNode


def is_balanced(root: TreeNode | None) -> bool:
    """Check whether a binary tree is height-balanced.

    Args:
        root: The root of the binary tree.

    Returns:
        True if the tree is balanced, False otherwise.

    Examples:
        >>> is_balanced(None)
        True
    """
    return _get_depth(root) != -1


def _get_depth(root: TreeNode | None) -> int:
    """Compute the depth of a tree, returning -1 if unbalanced.

    Args:
        root: The root of the subtree.

    Returns:
        The depth of the subtree, or -1 if it is unbalanced.
    """
    if root is None:
        return 0
    left = _get_depth(root.left)
    right = _get_depth(root.right)
    if abs(left - right) > 1 or -1 in [left, right]:
        return -1
    return 1 + max(left, right)
