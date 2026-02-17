"""
Invert Binary Tree

Inverts a binary tree by swapping the left and right children of every node.

Reference: https://en.wikipedia.org/wiki/Binary_tree

Complexity:
    Time:  O(n)
    Space: O(n) due to recursion stack
"""

from __future__ import annotations

from algorithms.tree.tree import TreeNode


def reverse(root: TreeNode | None) -> None:
    """Invert a binary tree in-place by swapping left and right children.

    Args:
        root: The root of the binary tree to invert.

    Examples:
        >>> reverse(None)
    """
    if root is None:
        return
    root.left, root.right = root.right, root.left
    if root.left:
        reverse(root.left)
    if root.right:
        reverse(root.right)
