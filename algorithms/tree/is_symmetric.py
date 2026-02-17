"""
Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (i.e., symmetric
around its center). Provides both recursive and iterative solutions.

Reference: https://en.wikipedia.org/wiki/Binary_tree

Complexity:
    Time:  O(n)
    Space: O(n)
"""

from __future__ import annotations

from algorithms.tree.tree import TreeNode


def is_symmetric(root: TreeNode | None) -> bool:
    """Check whether a binary tree is symmetric using recursion.

    Args:
        root: The root of the binary tree.

    Returns:
        True if the tree is symmetric, False otherwise.

    Examples:
        >>> is_symmetric(None)
        True
    """
    if root is None:
        return True
    return _helper(root.left, root.right)


def _helper(p: TreeNode | None, q: TreeNode | None) -> bool:
    """Recursively check whether two subtrees are mirrors of each other.

    Args:
        p: The root of the left subtree.
        q: The root of the right subtree.

    Returns:
        True if the subtrees are mirror images, False otherwise.
    """
    if p is None and q is None:
        return True
    if p is not None or q is not None or q.val != p.val:
        return False
    return _helper(p.left, q.right) and _helper(p.right, q.left)


def is_symmetric_iterative(root: TreeNode | None) -> bool:
    """Check whether a binary tree is symmetric using iteration.

    Args:
        root: The root of the binary tree.

    Returns:
        True if the tree is symmetric, False otherwise.

    Examples:
        >>> is_symmetric_iterative(None)
        True
    """
    if root is None:
        return True
    stack: list[list[TreeNode | None]] = [[root.left, root.right]]
    while stack:
        left, right = stack.pop()
        if left is None and right is None:
            continue
        if left is None or right is None:
            return False
        if left.val == right.val:
            stack.append([left.left, right.right])
            stack.append([left.right, right.left])
        else:
            return False
    return True
